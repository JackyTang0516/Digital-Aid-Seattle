import json
from datetime import datetime

class DonationManagement:
    def __init__(self):
        # Initialize the donations and distributions lists to store donation records and distribution records respectively.
        self.donations = []
        self.distributions = []

    def safe_input_integer(self, prompt, min_value=1):
        # Continuously prompt the user for an integer input until a valid integer that meets the min_value condition is entered.
        while True:
            try:
                value = int(input(prompt))
                if value >= min_value:
                    return value
                else:
                    print(f"Please enter a number greater than or equal to {min_value}.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    def register_donation(self, date=None):
        # Register a new donation with the donor's details and the donation specifics.
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        donor_name = input("Enter donor name: ")
        donation_type = input("Enter donation type: ")
        quantity = self.safe_input_integer("Enter quantity/amount: ")
        donation = {
            "donor_name": donor_name,
            "donation_type": donation_type,
            "quantity": quantity,
            "date": date
        }
        self.donations.append(donation)
        print("Donation registered successfully.")

    def get_inventory_quantity(self, donation_type):
        # Calculate the current inventory of a given donation type by subtracting the distributed amount from the donated amount.
        total_donations = sum(donation["quantity"] for donation in self.donations if donation["donation_type"] == donation_type)
        total_distributions = sum(distribution["quantity"] for distribution in self.distributions if distribution["donation_type"] == donation_type)
        return total_donations - total_distributions

    def get_known_donation_types(self):
        # Retrieve a set of all known donation types recorded so far.
        known_types = set(donation["donation_type"] for donation in self.donations)
        return known_types

    def distribute_donation(self, date=None):
        # Manage the distribution of donations ensuring the requested quantity does not exceed the available inventory.
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        known_types = self.get_known_donation_types()

        donation_type = input("Enter donation type: ")
        while donation_type not in known_types:
            print("Invalid donation type. Known types are: " + ", ".join(known_types))
            donation_type = input("Please re-enter a valid donation type: ")
        quantity = self.safe_input_integer(f"Enter quantity/amount to distribute for {donation_type}: ")

        available_quantity = self.get_inventory_quantity(donation_type)
        while quantity > available_quantity:
            print(f"Insufficient inventory for {donation_type}. Available quantity: {available_quantity}")
            quantity = self.safe_input_integer(f"Enter a new quantity for {donation_type} (available {available_quantity}): ")
        distribution = {
            "donation_type": donation_type,
            "quantity": quantity,
            "date": date
        }
        self.distributions.append(distribution)
        print("Distribution logged successfully.")

    def generate_inventory_report(self):
        # Generate a report of the current inventory for each donation type including the date it was last updated.
        inventory = {}
        last_updated = {}
        for donation in self.donations:
            donation_type = donation["donation_type"]
            if donation_type not in inventory:
                inventory[donation_type] = 0
                last_updated[donation_type] = donation["date"]
            inventory[donation_type] += donation["quantity"]
            if donation["date"] > last_updated[donation_type]:
                last_updated[donation_type] = donation["date"]

        for distribution in self.distributions:
            donation_type = distribution["donation_type"]
            if donation_type in inventory:
                inventory[donation_type] -= distribution["quantity"]
            if distribution["date"] > last_updated.get(donation_type, ''):
                last_updated[donation_type] = distribution["date"]

        print("Inventory Report:")
        for donation_type, quantity in inventory.items():
            if quantity > 0:
                print(f"{donation_type}: {quantity} (Last Updated: {last_updated[donation_type]})")



    def generate_donator_report(self):
        # Generate a report detailing all donations made by each donor including the type, quantity, and date of each donation.
        donator_report = {}
        for donation in self.donations:
            donor_name = donation["donor_name"]
            donation_type = donation["donation_type"]
            quantity = donation["quantity"]
            date = donation["date"]
            if donor_name not in donator_report:
                donator_report[donor_name] = {}
            if donation_type not in donator_report[donor_name]:
                donator_report[donor_name][donation_type] = []
            donator_report[donor_name][donation_type].append((quantity, date))

        print("Donator Report:")
        for donor_name, donations in donator_report.items():
            print(f"{donor_name}:")
            for donation_type, details in donations.items():
                for quantity, date in details:
                    print(f"  {donation_type}: {quantity} on {date}")


def main():
    donation_manager = DonationManagement()

    while True:
        print("\nDonation Management System")
        print("1. Register a donation")
        print("2. Log a distribution")
        print("3. Generate inventory report")
        print("4. Generate donator report")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            donation_manager.register_donation()
        elif choice == "2":
            donation_manager.distribute_donation()
        elif choice == "3":
            donation_manager.generate_inventory_report()
        elif choice == "4":
            donation_manager.generate_donator_report()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

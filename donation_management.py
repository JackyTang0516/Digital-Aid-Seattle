import json
from datetime import datetime

class DonationManagement:
    def __init__(self):
        self.donations = []
        self.distributions = []

    def register_donation(self, donor_name, donation_type, quantity, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        donation = {
            "donor_name": donor_name,
            "donation_type": donation_type,
            "quantity": quantity,
            "date": date
        }
        self.donations.append(donation)
        print("Donation registered successfully.")

    def distribute_donation(self, donation_type, quantity, date=None):
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
        distribution = {
            "donation_type": donation_type,
            "quantity": quantity,
            "date": date
        }
        self.distributions.append(distribution)
        print("Distribution logged successfully.")

    def generate_inventory_report(self):
        inventory = {}
        for donation in self.donations:
            donation_type = donation["donation_type"]
            if donation_type not in inventory:
                inventory[donation_type] = 0
            inventory[donation_type] += donation["quantity"]

        for distribution in self.distributions:
            donation_type = distribution["donation_type"]
            if donation_type in inventory:
                inventory[donation_type] -= distribution["quantity"]

        print("Inventory Report:")
        for donation_type, quantity in inventory.items():
            print(f"{donation_type}: {quantity}")

    def generate_donator_report(self):
        donator_report = {}
        for donation in self.donations:
            donor_name = donation["donor_name"]
            if donor_name not in donator_report:
                donator_report[donor_name] = 0
            donator_report[donor_name] += donation["quantity"]

        print("Donator Report:")
        for donor_name, total_donation in donator_report.items():
            print(f"{donor_name}: {total_donation}")

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
            donor_name = input("Enter donor name: ")
            donation_type = input("Enter donation type: ")
            quantity = int(input("Enter quantity/amount: "))
            donation_manager.register_donation(donor_name, donation_type, quantity)
        elif choice == "2":
            donation_type = input("Enter donation type: ")
            quantity = int(input("Enter quantity/amount: "))
            donation_manager.distribute_donation(donation_type, quantity)
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

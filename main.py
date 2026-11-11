# Smart Grocery Inventory Manager

from inventory_pkg import *

while True:

    print("\n--- SMART GROCERY ---")
    print("1. Add Stock")
    print("2. Update Stock")
    print("3. Low Stock Report")
    print("4. Display Inventory")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        add_stock(name, quantity)

    elif choice == "2":

        name = input("Enter product name: ")
        quantity = int(input("Enter sold quantity: "))
        update_stock(name, quantity)

    elif choice == "3":

        low_stock_report()

    elif choice == "4":

        display_inventory()

    elif choice == "5":

        print("Thank you!")
        break

    else:
        print("Invalid choice")

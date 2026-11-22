
from inventory import Inventory
from db_connection import connection

# Create Inventory object
inventory = Inventory()

try:
    while True:
        print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Products")
        print("4. Update Products")
        print("5. Delete Products")
        print("6. Low Stock Alert")
        print("7. EXIT")

        choice = input("Enter your choice: ")

        if choice == "1":
            inventory.create_product()

        elif choice == "2":
            inventory.display_products()

        elif choice == "3":
            inventory.search_product()

        elif choice == "4":
            inventory.update_product()

        elif choice == "5":
            inventory.delete_product()

        elif choice == "6":
            inventory.low_stock_alert()

        elif choice == "7":
            print("Thank you for using Inventory Management System!")
            break

        else:
            print("Invalid Choice! Please try again.")

finally:
    cursor = connection.cursor()
    cursor.close()
    connection.close()
    print("Database connection closed!")


from db_connection import connection, cursor


class Inventory:

    # 1. Display Products
    def display_products(self):
        query = "SELECT * FROM products"

        cursor.execute(query)
        products = cursor.fetchall()

        if products:
            print("\n===== PRODUCT DETAILS =====")

            for item in products:
                print("----------------------------")
                print("Product ID:", item[0])
                print("Name:", item[1])
                print("Price:", item[2])
                print("Quantity:", item[3])
                print("Category:", item[4])
        else:
            print("No Products Found!")

    # 2. Add Product
    def create_product(self):
        try:
            product_id = int(input("Enter Product ID: "))

            query = "SELECT * FROM products WHERE product_id = %s"
            values = (product_id,)

            cursor.execute(query, values)
            existing_product = cursor.fetchone()

            if existing_product:
                print("Product ID already exists!")
                return

            name = input("Enter Product Name: ").strip()

            if name == "":
                print("Product name cannot be empty!")
                return

            price = float(input("Enter Product Price: "))

            if price < 0:
                print("Price cannot be negative!")
                return

            quantity = int(input("Enter Quantity: "))

            if quantity < 0:
                print("Quantity cannot be negative!")
                return

            category = input("Enter Category: ").strip()

            query = """
            INSERT INTO products
            (product_id, name, price, quantity, category)
            VALUES (%s, %s, %s, %s, %s)
            """

            values = (product_id, name, price, quantity, category)

            cursor.execute(query, values)
            connection.commit()

            print("Product Added Successfully!")

        except ValueError:
            print("Invalid input! Please enter correct values.")

    # 3. Search Product
    def search_product(self):
        try:
            search_id = int(input("Enter Product ID to search: "))

            query = "SELECT * FROM products WHERE product_id = %s"
            values = (search_id,)

            cursor.execute(query, values)
            product = cursor.fetchone()

            if product:
                print("\nProduct Found!")
                print("Product ID:", product[0])
                print("Name:", product[1])
                print("Price:", product[2])
                print("Quantity:", product[3])
                print("Category:", product[4])
            else:
                print("Product Not Found!")

        except ValueError:
            print("Invalid input! Please enter a valid Product ID.")

    # 4. Update Product
    def update_product(self):
        try:
            search_id = int(input("Enter Product ID to update: "))

            query = "SELECT * FROM products WHERE product_id = %s"
            values = (search_id,)

            cursor.execute(query, values)
            product = cursor.fetchone()

            if product:
                new_name = input("Enter New Product Name: ").strip()

                if new_name == "":
                    print("Cannot update empty product name!")
                    return

                new_price = float(input("Enter New Price: "))

                if new_price < 0:
                    print("Cannot update negative price!")
                    return

                new_quantity = int(input("Enter New Quantity: "))

                if new_quantity < 0:
                    print("Cannot update negative quantity!")
                    return

                new_category = input("Enter New Category: ").strip()

                query = """
                UPDATE products
                SET name = %s,
                    price = %s,
                    quantity = %s,
                    category = %s
                WHERE product_id = %s
                """

                values = (
                    new_name,
                    new_price,
                    new_quantity,
                    new_category,
                    search_id
                )

                cursor.execute(query, values)
                connection.commit()

                print("Product Updated Successfully!")

            else:
                print("Product Not Found!")

        except ValueError:
            print("Invalid input! Please enter correct values.")

    # 5. Delete Product
    def delete_product(self):
        try:
            search_id = int(input("Enter Product ID to delete: "))

            query = "DELETE FROM products WHERE product_id = %s"
            values = (search_id,)

            cursor.execute(query, values)
            connection.commit()

            if cursor.rowcount > 0:
                print("Product Deleted Successfully!")
            else:
                print("Product Not Found!")

        except ValueError:
            print("Invalid input! Please enter a valid Product ID.")

    # 6. Low Stock Alert
    def low_stock_alert(self):
        query = "SELECT * FROM products WHERE quantity < 5"

        cursor.execute(query)
        products = cursor.fetchall()

        if products:
            print("\n===== LOW STOCK ALERT =====")

            for item in products:
                print("----------------------------")
                print("Product ID:", item[0])
                print("Product:", item[1])
                print("Available Quantity:", item[3])
        else:
            print("No Low Stock Found!")

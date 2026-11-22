
from flask import Flask, render_template, request, redirect, url_for
from db_connection import connection, cursor

app = Flask(__name__)


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html")


# DISPLAY ALL PRODUCTS
@app.route("/products")
def products():

    query = "SELECT * FROM products"
    cursor.execute(query)

    product_list = cursor.fetchall()
    message = request.args.get("message", "")

    return render_template(
        "products.html",
        products=product_list,
        message=message
    )


# ADD PRODUCT
@app.route("/add_product", methods=["POST"])
def add_product():

    try:
        product_id = int(request.form["product_id"])
        name = request.form["name"]
        price = float(request.form["price"])
        quantity = int(request.form["quantity"])
        category = request.form["category"]

        query = """
        INSERT INTO products
        (product_id, name, price, quantity, category)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (product_id, name, price, quantity, category)

        cursor.execute(query, values)
        connection.commit()

        return redirect(url_for("products", message="Product added successfully!"))

    except Exception:
        connection.rollback()
        return redirect(url_for("products", message="Unable to add product. Check the Product ID and details."))


# SEARCH PRODUCT
@app.route("/search_product", methods=["POST"])
def search_product():

    product_id = int(request.form["product_id"])

    query = "SELECT * FROM products WHERE product_id = %s"
    values = (product_id,)

    cursor.execute(query, values)
    product_list = cursor.fetchall()

    message = "" if product_list else "Product not found!"

    return render_template(
        "products.html",
        products=product_list,
        message=message
    )


# UPDATE PRODUCT
@app.route("/update_product", methods=["POST"])
def update_product():

    product_id = int(request.form["product_id"])
    price = float(request.form["price"])
    quantity = int(request.form["quantity"])

    query = """
    UPDATE products
    SET price = %s, quantity = %s
    WHERE product_id = %s
    """

    values = (price, quantity, product_id)

    cursor.execute(query, values)
    connection.commit()

    if cursor.rowcount > 0:
        message = "Product updated successfully!"
    else:
        message = "Product not found or no changes made!"

    return redirect(url_for("products", message=message))


# DELETE PRODUCT
@app.route("/delete_product", methods=["POST"])
def delete_product():

    product_id = int(request.form["product_id"])

    query = "DELETE FROM products WHERE product_id = %s"
    values = (product_id,)

    cursor.execute(query, values)
    connection.commit()

    if cursor.rowcount > 0:
        message = "Product deleted successfully!"
    else:
        message = "Product not found!"

    return redirect(url_for("products", message=message))


# LOW STOCK ALERT
@app.route("/low_stock")
def low_stock():

    query = "SELECT * FROM products WHERE quantity <= %s"
    values = (5,)

    cursor.execute(query, values)
    product_list = cursor.fetchall()

    message = "" if product_list else "No low-stock products found!"

    return render_template(
        "products.html",
        products=product_list,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)

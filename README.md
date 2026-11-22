# Inventory Management System

A Python Flask-based Inventory Management System integrated with a MySQL database. This application helps users manage products, track stock quantities, and perform inventory operations through a simple web interface.

## Features

- Add new products
- View all products
- Search products using Product ID
- Update product price and quantity
- Delete products
- Low Stock Alert for products with quantity of 5 or less
- MySQL database integration
- User-friendly web interface

## Technologies Used

- **Programming Language:** Python
- **Backend Framework:** Flask
- **Database:** MySQL
- **Frontend:** HTML, CSS
- **Libraries:** MySQL Connector, Python-dotenv

## Project Structure

```text
Inventory_Management_System/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── products.html
│
├── app.py
├── main.py
├── inventory.py
├── db_connection.py
├── .env.example
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd Inventory-Management-System
```

### 3. Install Required Packages

```bash
pip install flask mysql-connector-python python-dotenv
```

### 4. Create the MySQL Database

Open MySQL Workbench and execute:

```sql
CREATE DATABASE inventory_db;

USE inventory_db;

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2),
    quantity INT,
    category VARCHAR(50)
);
```

### 5. Configure Environment Variables

Create a `.env` file in the project root directory:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=YOUR_MYSQL_PASSWORD
DB_NAME=inventory_db
```

Replace `YOUR_MYSQL_PASSWORD` with your MySQL password.

### 6. Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Learning Outcomes

- Python application development
- Flask web application development
- MySQL database connectivity
- CRUD operations
- HTML and CSS integration
- Environment variable management

## Author

**Thaha S**

GitHub: @TikTok00001

LinkedIn: www.linkedin.com/in/thaha2004

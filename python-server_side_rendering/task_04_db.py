from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

def load_products_from_json():
    try:
        with open('products.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def load_products_from_csv():
    products = []
    try:
        with open('products.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except FileNotFoundError:
        return None

def load_products_from_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM products")
        rows = cursor.fetchall()
        conn.close()
        return [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]
    except sqlite3.Error:
        return None

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error_message = None

    if source == 'json':
        products = load_products_from_json()
        if products is None:
            error_message = "JSON data source not found."
    elif source == 'csv':
        products = load_products_from_csv()
        if products is None:
            error_message = "CSV data source not found."
    elif source == 'sql':
        products = load_products_from_sql()
        if products is None:
            error_message = "SQLite database error or data not found."
    else:
        error_message = "Wrong source specified. Use 'json', 'csv', or 'sql'."

    if products and product_id:
        products = [product for product in products if product["id"] == product_id]
        if not products:
            error_message = "Product not found"

    return render_template('product_display.html', products=products, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
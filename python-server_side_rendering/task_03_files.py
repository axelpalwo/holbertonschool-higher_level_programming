from flask import Flask, render_template, request
import json
import csv

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
    else:
        error_message = "Wrong source specified. Use 'json' or 'csv'."

    if products and product_id:
        products = [product for product in products if product["id"] == product_id]
        if not products:
            error_message = f"Product with ID {product_id} not found."

    return render_template('product_display.html', products=products, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
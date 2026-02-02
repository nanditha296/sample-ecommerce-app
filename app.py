from flask import Flask, render_template, jsonify

# Create Flask app instance
app = Flask(__name__)

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Sample API route
@app.route('/api/products')
def products():
    return jsonify([
        {"id": 1, "name": "Laptop", "price": 750},
        {"id": 2, "name": "Smartphone", "price": 500},
        {"id": 3, "name": "Headphones", "price": 100}
    ])

# Run locally (Azure will use gunicorn in production)
if __name__ == '__main__':
    app.run(debug=True)

from flask import render_template, request, redirect, url_for
from . import app

# Existing routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/sales')
def sales():
    return render_template('sales.html')

# New routes for handling sales data
@app.route('/sales/data')
def sales_data():
    # Sample sales data, ideally fetched from a database
    all_sales = [
        {'id': 1, 'monthly_amount': 1000, 'date': '2024-01-01', 'region': 'North'},
        {'id': 2, 'monthly_amount': 1500, 'date': '2024-02-05', 'region': 'East'},
        {'id': 3, 'monthly_amount': 2000, 'date': '2024-03-10', 'region': 'South'},
    ]
    return render_template('sales_data.html', all_sales=all_sales)

@app.route('/sales/add', methods=['GET', 'POST'])
def add_sales():
    if request.method == 'POST':
        # Logic to add new sales record
        monthly_amount = request.form['monthly_amount']
        date = request.form['date']
        region = request.form['region']
        # Add to database here
        return redirect(url_for('sales_data'))
    return render_template('add_sales_data.html')

@app.route('/edit/<int:sales_data_id>', methods=['GET', 'POST'])
def edit_sale(sales_data_id):
    if request.method == 'POST':
        # Logic for editing the sales record
        monthly_amount = request.form['monthly_amount']
        date = request.form['date']
        region = request.form['region']
        # Update the database with the new information
        return redirect(url_for('sales_data'))
    # Fetch the sales data for the given sale_id
    sale = {'id': sales_data_id, 'monthly_amount': 1000, 'date': '2024-01-01', 'region': 'North'}
    return render_template('edit_sales_data.html', sale=sale)

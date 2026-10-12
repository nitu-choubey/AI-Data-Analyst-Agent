import sqlite3
import random
from datetime import datetime, timedelta

def create_sales_database():
    # 1. Database Connection (Yeh local sales.db file bana dega)
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()

    # 2. Tables Create Karna
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        category TEXT,
        price REAL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sales (
        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER,
        quantity INTEGER,
        sale_date TEXT,
        region TEXT,
        FOREIGN KEY (product_id) REFERENCES products (product_id)
    )
    ''')

    # 3. Dummy Products Insert Karna
    products_data = [
        ('Wireless Mouse', 'Electronics', 25.00),
        ('Mechanical Keyboard', 'Electronics', 75.00),
        ('Gaming Headset', 'Electronics', 50.00),
        ('Running Shoes', 'Apparel', 60.00),
        ('Cotton Hoodie', 'Apparel', 40.00),
        ('Water Bottle', 'Accessories', 15.00),
        ('Smart Watch', 'Electronics', 120.00)
    ]
    
    cursor.executemany("INSERT OR IGNORE INTO products (product_name, category, price) VALUES (?, ?, ?)", products_data)

    # 4. Dummy Sales Data Generate Karna
    regions = ['North', 'South', 'East', 'West']
    start_date = datetime(2025, 1, 1)
    
    sales_data = []
    for _ in range(500): # 500 sample transactions
        product_id = random.randint(1, 7)
        quantity = random.randint(1, 5)
        random_days = random.randint(0, 600)
        sale_date = (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')
        region = random.choice(regions)
        
        sales_data.append((product_id, quantity, sale_date, region))

    cursor.executemany("INSERT INTO sales (product_id, quantity, sale_date, region) VALUES (?, ?, ?, ?)", sales_data)

    conn.commit()
    conn.close()
    print("✅ Database 'sales.db' successfully ban gaya aur sample data insert ho gaya!")

if __name__ == "__main__":
    create_sales_database()
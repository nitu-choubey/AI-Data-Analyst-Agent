import sqlite3
import pandas as pd

def run_query(query):
    # sales.db database se connect karna
    conn = sqlite3.connect('sales.db')
    
    # Pandas ka use karke SQL query run karna aur result ko table format mein lana
    df = pd.read_sql_query(query, conn)
    
    conn.close()
    return df

if __name__ == "__main__":
    print("--- 1. Top 5 Products ki List ---")
    query_products = "SELECT * FROM products LIMIT 5;"
    print(run_query(query_products))
    
    print("\n--- 2. Total Sales Transactions ---")
    query_sales_count = "SELECT COUNT(*) as total_transactions FROM sales;"
    print(run_query(query_sales_count))
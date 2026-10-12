import sqlite3
import pandas as pd
from google import genai

# Apni bilkul sahi API key yahan inverted commas ke andar paste karein
API_KEY = os.getenv("GEMINI_API_KEY", "")

client = genai.Client(api_key=API_KEY)

def get_sql_from_ai(natural_language_query):
    schema = """
    Database Schema:
    Table 1: products
    - product_id (INTEGER)
    - product_name (TEXT)
    - category (TEXT)
    - price (REAL)

    Table 2: sales
    - sale_id (INTEGER)
    - product_id (INTEGER)
    - quantity (INTEGER)
    - sale_date (TEXT - Format: YYYY-MM-DD)
    - region (TEXT - Values: North, South, East, West)
    """
    
    prompt = f"""
    You are an expert SQLite SQL writer. Given the database schema below, write a clean, executable SQL query for SQLite based on the user's question. 
    Return ONLY the raw SQL query inside a markdown code block, nothing else. No explanation.
    
    {schema}
    
    User Question: {natural_language_query}
    """
    
    # Google ke kehne ke anusaar yahan gemini-3.8-flash use kiya hai
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt,
    )
    
    sql_query = response.text.strip()
    if sql_query.startswith("```sql"):
        sql_query = sql_query[6:]
    if sql_query.endswith("```"):
        sql_query = sql_query[:-3]
        
    return sql_query.strip()

def run_query(query):
    conn = sqlite3.connect('sales.db')
    try:
        df = pd.read_sql_query(query, conn)
    except Exception as e:
        df = pd.DataFrame({'Error': [str(e)]})
    conn.close()
    return df

if __name__ == "__main__":
    user_question = "Show total sales quantity by region"
    print(f"💬 User Question: {user_question}")
    
    generated_sql = get_sql_from_ai(user_question)
    print(f"🔍 Generated SQL: {generated_sql}")
    
    print("\n📊 Query Result:")
    result_df = run_query(generated_sql)
    print(result_df)
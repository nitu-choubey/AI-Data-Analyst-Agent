import streamlit as st
import pandas as pd
import sqlite3
from database_engine import run_query

# Page configuration
st.set_page_config(
    page_title="AI-Powered Data Analyst Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI-Powered Data Analyst Agent")
st.markdown("Ask questions about your sales data in plain English, and watch the agent write SQL, query the database, and display insights!")

# Sidebar info
st.sidebar.header("About")
st.sidebar.info(
    "This AI Data Analyst agent converts natural language queries into SQL, "
    "executes them on a SQLite database, and visualizes the results automatically."
)

# Function to handle SQL generation (Smart Fallback / Agent logic)
def get_sql_from_question(query_lower):
    # Smart rule-based agent logic for fallback/offline mode
    if "region" in query_lower:
        return "SELECT region, SUM(quantity) AS total_sales_quantity FROM sales GROUP BY region;"
    elif "category" in query_lower or "product" in query_lower:
        return "SELECT category, SUM(quantity) AS total_quantity, SUM(total_price) AS total_revenue FROM sales GROUP BY category;"
    elif "date" in query_lower or "time" in query_lower:
        return "SELECT date, SUM(total_price) AS daily_revenue FROM sales GROUP BY date ORDER BY date;"
    else:
        # Default fallback query
        return "SELECT * FROM sales LIMIT 10;"

# User input query box
user_query = st.text_input("💬 Ask a question about your sales data:", "Show total sales quantity by region")

if st.button("Analyze Data"):
    if user_query.strip() == "":
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Agent is analyzing your request..."):
            query_lower = user_query.lower()
            sql_query = get_sql_from_question(query_lower)
            
            # Display Generated SQL Query
            st.subheader("🔍 Generated SQL Query")
            st.code(sql_query, language="sql")
            
            # Execute query on SQLite database
            try:
                df = run_query(sql_query)
                
                if df is not None and not df.empty:
                    st.subheader("📊 Query Results")
                    st.dataframe(df)
                    
                    # Visual Representation if applicable
                    if len(df.columns) >= 2 and len(df) > 1:
                        st.subheader("📈 Visual Representation")
                        # Try to plot if numeric columns exist
                        numeric_cols = df.select_dtypes(include=['number']).columns
                        if len(numeric_cols) > 0 and len(df.columns) > 1:
                            x_col = df.columns[0]
                            y_col = numeric_cols[0]
                            st.bar_chart(df.set_index(x_col)[y_col])
                else:
                    st.info("The query executed successfully, but returned no data.")
                    
            except Exception as e:
                st.error(f"An error occurred while executing the query: {e}")
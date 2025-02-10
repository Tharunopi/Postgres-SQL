import streamlit as st
import psycopg2

db_params = {
    "host": "localhost",
    "database": "svt_base",
    "user": "postgres",
    "password": "admin123",
    "port": "5433"
}

def connect_to_db():
    return psycopg2.connect(**db_params)

def exe_query(conn, query):
    cursor = conn.cursor()

    cursor.execute(query)
    result = cursor.fetchall()

    conn.commit()
    cursor.close()

    return result

conn = connect_to_db()

products = exe_query(conn, "SELECT * FROM products")
product_list = [i[1] for i in products]

stores = exe_query(conn, "SELECT * FROM stores")
store_list = [i[1] for i in stores]

st.title("Orders creation page")

st.subheader("Product")
pr = st.selectbox("Enter product", product_list, placeholder="Select from below", index=None)

st.subheader("Store")
sr = st.selectbox("Enter store", store_list, placeholder="Select from below", index=None)
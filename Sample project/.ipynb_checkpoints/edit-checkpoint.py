import streamlit as st
import psycopg2
import pandas as pd
    
db_params = {
    "host": "localhost",
    "database": "svt_base",
    "user": "postgres",
    "password": "admin123",
    "port": "5433"
}

def connect_to_db():
    return psycopg2.connect(**db_params)

def fetch_data(table):
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table}", (table))
        columns = [desc[0] for desc in cur.description]
        data = cur.fetchall()
        cur.close()
        conn.close()
        return pd.DataFrame(data, columns=columns)
    except psycopg2.Error as e:
        st.error(f"Error fetching data: {e}")
        return None

def insert_new(product_name, product_price):

    conn = connect_to_db()
    cur = conn.cursor()
    query = """
        INSERT INTO products (product_name, product_price)
        VALUES
            (%s, %s)
    """
    cur.execute(query, (product_name, product_price))
    conn.commit()
    cur.close()
    conn.close()
    st.success("successfully added")

def delete_rows(product_name):
    conn = connect_to_db()
    cur = conn.cursor()
    query = "DELETE FROM products WHERE product_name = %s"  
    cur.execute(query, (product_name,))
    conn.commit()
    cur.close()
    conn.close()
    st.success("successfully deleted")

def get_prod_name():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM products"
    cursor.execute(query)
    result = cursor.fetchall()

    conn.commit()
    cursor.close()

    return [i[1] for i in result]
    
st.title("Edit Products / Stores")

value = st.selectbox("Select DataBase to edit", ("Products", "Stores"))

if value == "Products":
    st.subheader("Products")
    df = fetch_data('products')

    if df is not None:
        st.dataframe(df)
    pt_value = st.selectbox("Select operation", ("Insert", "Delete"))
    
    if pt_value == "Insert":
        pt_name = st.text_input("Enter product name")
        pt_price = st.number_input("Enter product price")

        if pt_name and pt_price:
            if st.button("Insert"):
                insert_new(pt_name, pt_price)

    if pt_value == "Delete":
        pt_del_name = st.text_input("Enter product name")

        if pt_del_name:
            if pt_del_name not in get_prod_name():
                st.error("enter valid product name")
            if st.button("Delete"):
                delete_rows(pt_del_name)
    

if value == "Stores":
    st.subheader("Stores")
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

def update_rows(product_name, price):
    conn = connect_to_db()
    cur = conn.cursor()
    query = "UPDATE products SET product_price = %s WHERE product_name = %s"  
    cur.execute(query, (price, product_name))
    conn.commit()
    cur.close()
    conn.close()
    st.success("successfully updated")

def get_prod_name():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM products"
    cursor.execute(query)
    result = cursor.fetchall()

    conn.commit()
    cursor.close()

    return [i[1] for i in result]

def get_detail():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM products"
    cursor.execute(query)
    result = cursor.fetchall()

    conn.commit()
    cursor.close()

    return result

def get_detail_store():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM stores"
    cursor.execute(query)
    result = cursor.fetchall()

    conn.commit()
    cursor.close()

    return result
    
st.title("Edit Products / Stores")

value = st.selectbox("Select DataBase to edit", ("Products", "Stores"))

if value == "Products":
    st.subheader("Products")
    df = fetch_data('products')
    already_in_products = [i[1] for i in get_detail()]

    if df is not None:
        st.dataframe(df)
    pt_value = st.radio("Select an operation", ("Insert", "Update"), captions=["Insert new data to table.", "Update already existing table."])
    
    if pt_value == "Insert":
        pt_name = st.text_input("Enter product name")
        if pt_name in already_in_products:
            st.error("Product name already exists!!")
        else:
            pt_price = st.number_input("Enter product price")

            if pt_name and pt_price:
                if st.button("Insert"):
                    insert_new(pt_name, pt_price)

    if pt_value == "Update":
        pt_up_name = st.text_input("Enter product name")
        pt_up_price = st.number_input("Enter product price", min_value=1)

        if pt_up_name and pt_up_price:
            if pt_up_name not in already_in_products:
                st.error("Product doesn't exists!!")
            else:
                if st.button("Update"):
                    update_rows(pt_up_name, pt_up_price)
                

def insert_new_store(pt_name, pt_loc, pt_amt):
    conn = connect_to_db()
    cur = conn.cursor()
    query = """
        INSERT INTO stores (store_name, store_loc, amount)
        VALUES
            (%s, %s, %s)
    """
    cur.execute(query, (pt_name, pt_loc, pt_amt))
    conn.commit()
    cur.close()
    conn.close()
    st.success("successfully added")

def update_rows_store(product_name, price):
    conn = connect_to_db()
    cur = conn.cursor()
    query = "UPDATE stores SET amount = %s WHERE store_name = %s"  
    cur.execute(query, (price, product_name))
    conn.commit()
    cur.close()
    conn.close()
    st.success("successfully updated")

if value == "Stores":
    st.subheader("Stores")
    df = fetch_data('stores')
    already_in_stores = [i[1] for i in get_detail_store()]

    if df is not None:
        st.dataframe(df, hide_index=True, width=20000)
    pt_value = st.radio("Select an operation", ("Insert", "Update"), captions=["Insert new data to table.", "Update already existing table."])
    
    if pt_value == "Insert":
        pt_name = st.text_input("Enter Store name")
        if pt_name in already_in_stores:
            st.error("Store already exists!!")
        else:
            pt_loc = st.text_input("Enter store location")
            pt_amt = st.number_input("Enter pre existing balance", min_value=0)

            if pt_name and pt_loc and pt_amt:
                if st.button("Insert"):
                    insert_new_store(pt_name, pt_loc, pt_amt)

    if pt_value == "Update":
        pt_up_name = st.text_input("Enter store name")
        pt_up_amt = st.number_input("Enter amount", min_value=1)

        if pt_up_name and pt_up_amt:
            if pt_up_name not in already_in_stores:
                st.error("Store doesn't exists!!")
            else:
                if st.button("Update"):
                    update_rows_store(pt_up_name, pt_up_amt)
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

def exe_query_spe(query):
    
    cvu = connect_to_db()
    cursor =cvu.cursor()

    cursor.execute(query)
    result = cursor.fetchall()

    cvu.commit()
    cursor.close()

    return result    

def insert_query(conn, store_id, product_id, quantity, total_inr):

    cursor = conn.cursor()
    query = """
        INSERT INTO orders(store_id, product_id, quantity, total_inr, time_stamp)
        VALUES
            (%s, %s, %s, %s, CURRENT_TIMESTAMP)
    """

    values = (store_id, product_id, quantity, total_inr)
    cursor.execute(query, values)

    conn.commit()
    cursor.close()
    conn.close()

def get_price(item, product_list, products):
    inde = product_list.index(item)
    return float(products[inde][2])

def insert_amount(st_id, tl_amt):
    cvu = connect_to_db()
    cursor =cvu.cursor()

    query = f"UPDATE stores SET amount = amount + {tl_amt} WHERE store_id = {st_id}"
    cursor.execute(query, (tl_amt, st_id))
    
    cvu.commit()
    cursor.close()
    cvu.close()

conn = connect_to_db()

products = exe_query(conn, "SELECT * FROM products")
product_list = [i[1] for i in products]

stores = exe_query(conn, "SELECT * FROM stores")
store_list = [i[1] for i in stores]

price = 0

st.title("Orders creation page")

st.subheader("Product")
pr = st.selectbox("Enter product", product_list, placeholder="Select from below", index=None)
p_id = product_list.index(pr) + 1

st.subheader("Store")
sr = st.selectbox("Enter store", store_list, placeholder="Select from below", index=None)
s_id = store_list.index(sr) + 1

if pr:
    st.subheader("Quantity")
    qt = st.number_input("Enter quantity", placeholder="Type it...0", min_value=0.1, step=5.0)

    price = get_price(pr, product_list, products)
if pr:
    st.subheader("Grand total")
    tl = st.number_input("Enter amount", min_value=price*qt, step=price)

if tl:
    if st.button("Insert"):
        insert_query(conn, s_id, p_id, qt, tl)
        st.success("Data inserted successfully!")

        final_order = exe_query_spe("SELECT * FROM orders")[-1]
        st.write(final_order)

        st_id = final_order[1]
        tl_amt = final_order[4]
        insert_amount(st_id, tl_amt)

        
        

        
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

def get_last_order():
    cvu = connect_to_db()
    cursor = cvu.cursor()
    query = "SELECT * FROM orders ORDER BY order_id DESC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchone()  
    
    cursor.close()
    cvu.close()
    return result

conn = connect_to_db()

products = exe_query(conn, "SELECT * FROM products")
product_list = [i[1] for i in products]
product_ids = [i[0] for i in products]
product_price = [i[2] for i in products]

stores = exe_query(conn, "SELECT * FROM stores")
store_list = [i[1] for i in stores]
store_ids = [i[0] for i in stores]

query_orders = []

st.title("Orders creation page")

st.subheader("Store")
sr = st.selectbox("Enter store", store_list, placeholder="Select from below", index=None)
if sr:
    s_id = store_list.index(sr)
    s_id = store_ids[s_id]

st.subheader("Product")
pr = st.pills("Choose products", product_list, selection_mode="multi")
pr_len = len(pr)
if pr and sr:  
    for i in pr:
        with st.form(f"order session {i}"):
            p = product_list.index(i)
            p_id = product_ids[p]
            p_price = product_price[p]
            
            qty = st.number_input(f"Enter {i} qty", min_value=1)
            tl = qty * p_price
            st.caption(f"Grand total: :blue[{tl}]")

            submit = st.form_submit_button("Insert")
            if submit:
                query_orders.append([s_id, p_id, qty, tl])
                st.success(f"{i} form submitted")

    if query_orders:
        st.write(len(query_orders))
                
        

        
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

def get_data_table(table):
    conn = connect_to_db()
    cursor = conn.cursor()

    query = f"SELECT * FROM {table}"
    cursor.execute(query, (table,))
    result = cursor.fetchall()

    conn.commit()
    cursor.close()
    return result

def update_payment_table(st_id, payment_method, payment_amount):
    conn = connect_to_db()
    cursor = conn.cursor()

    query = """
    INSERT INTO payments(store_id, payment_method, payment_amount, paymment_timestamp)
    VALUES 
        (%s, %s, %s, CURRENT_TIMESTAMP)
    """
    cursor.execute(query, (st_id, payment_method, payment_amount))

    conn.commit()
    cursor.close()
    st.success("Payment compelete")
    
    return True

def update_store_table(st_id, amt_paid):
    conn = connect_to_db()
    cursor = conn.cursor()

    query = "UPDATE stores SET amount = amount - %s WHERE store_id = %s"
    cursor.execute(query, (amt_paid, st_id))

    conn.commit()
    cursor.close()
    st.success("Stores balance updated$$")
    

st.title("Create payment")

stores = get_data_table("stores")
stores_name = [i[1] for i in stores]
stores_id = [i[0] for i in stores]
store_amt = [i[3] for i in stores]

st_name = st.selectbox("Enter store name", stores_name, index=None, placeholder="Type or select store")
st_name_value = False
if st_name:
    if st_name in stores_name:
        st_id = stores_id[stores_name.index(st_name)]
        st_max_amt = store_amt[stores_name.index(st_name)]
        st.write(f"Max payable amount :blue-background[{st_max_amt}]")
        st_name_value = True
    else:
        st.error("Store doesn't exists!!")

if st_name_value:
    payment_method = st.radio("Select payment method", ["Cash", "UPI", "IMPS", "Bank Transfer"])

    if payment_method:
        payment_amount = st.number_input("Enter amount", min_value=0, max_value=int(st_max_amt), step=500, value=int(st_max_amt))
        st.write(f"Amount payable :blue-background[{payment_amount}]/-  via :blue-background[{payment_method}].")

        if payment_amount >= 1:
            if st.button("Make payment"):
                if update_payment_table(st_id, payment_method, payment_amount):
                    update_store_table(st_id, payment_amount)
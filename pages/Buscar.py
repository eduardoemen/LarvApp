import streamlit as st 
import pandas as pd
import mysql.connector
conn = st.connection('mysql', type='sql')
cursor = conn.cursor()
cursor.execute("SELECT * FROM larva")
data = cursor.fetchall()
df = pd.DataFrame(data, columns=["id","fecha","hora","tanque","dia","estadio","actividad natatoria"])
st.dataframe(df) 

import streamlit as st 
import pandas as pd
import sqlite3

conn=sqlite3.connect("lv.db")
c=conn.cursor()

sql_query = pd.read_sql_query ('SELECT * FROM clientes', conn)
df = pd.DataFrame(sql_query, columns = ["ID","nombre","apellido","direccion","telefono","tipo"])





st.write("Busca cliente")
apellido=st.text_input("Ingresa apellido: ")
if st.button("Buscar"):
    df[df['apellido'].str.contains(apellido)]

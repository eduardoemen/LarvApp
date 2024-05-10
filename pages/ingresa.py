import streamlit as st 
import pandas as pd
import sqlite3


conn=sqlite3.connect("lv.db")
c=conn.cursor()

def add_data(ID,nombre,apellido,direccion,telefono,tipo):
    c.execute("INSERT INTO clientes(ID,nombre,apellido,direccion,telefono,tipo) VALUES (?,?,?,?,?,?)",(ID,nombre,apellido,direccion,telefono,tipo))
    conn.commit()


st.write("Ingresa nuevo cliente")
id=st.text_input("Ingresa ID: ")
population=st.text_input("Ingresa nombre: ")
generaciones=st.text_input("Ingresa apellido: ")
strain=st.text_input("Ingresa dirección: ")
type=st.text_input("Ingresa teléfono: ")
posicion=st.text_input("Ingresa tipo: ")
if st.button("ADD"):
    add_data(id,population,generaciones,strain,type,posicion)
    st.success("Datos ingresados")

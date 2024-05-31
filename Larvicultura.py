if st.sidebar.checkbox("OK"):
    if password == '12345'and username=="edu":
        st.success("Logged In as {}".format(username))
else:
        st.write("Usuario o contraseña incorrectos")               







import streamlit as st 
import pandas as pd
import sqlite3


conn = sqlite3.connect('pages/larvicultura.db')
c = conn.cursor()

bl = st.sidebar.selectbox(
    "Opciones",
    ("Control de Calidad","Parámetros", "Alimento")
)

if bl=="Control de Calidad":
    
    def add_data(fecha,hora,dia,tanque,estadio,act):
        c.execute("INSERT INTO larvas(fecha,hora,dia,tanque,estadio,act) VALUES (?,?,?,?,?,?)",(fecha,hora,dia,tanque,estadio,act))
        conn.commit()
        
    fecha=st.date_input("Ingresa fecha: ")
    
    hora=st.time_input("Ingresa hora: ")
    dia=st.text_input("Día# :   ")
    tanque=st.text_input("Tanque # :   ")
    estadio=st.text_input("Ingresa estadío: ")
    st.write("Actividad Natatoria")
    st.write("Si observamos que el >95% de las larvas nadan activamente, entonces son puntuadas con un 10; si están activas del 70-95%, se puntúa 5; y si son <70% las activas entonces se puntúa 0 (FAO, 2004).")
    actnat=st.text_input("Actividad natatoria: ")
    if st.button("ADD"):
        add_data(fecha,hora,tanque,dia,estadio,actnat)
        st.success("Datos ingresados")

         



     
    
        
        

        
        


import streamlit as st 
import pandas as pd
import mysql.connector
conn = st.connection('mysql', type='sql')
cursor = conn.cursor()

bl = st.sidebar.selectbox(
    "Opciones",
    ("Control de Calidad","Parámetros", "Alimento")
)

if bl=="Control de Calidad":
    
    def add_data(fecha,hora,tanque,dia,estadio,actnat):
        cursor.execute("INSERT INTO larva(fecha,hora,tanque,dia,estadio,actnat) VALUES (%s, %s, %s, %s, %s, %s)",(fecha,hora,tanque,dia,estadio,actnat))
        conn.commit()
        
    hora=st.time_input("Ingresa hora: ")
    fecha=st.date_input("Ingresa fecha: ")
    tanque=st.text_input("Tanque # :   ")
    dia=st.text_input("Día# :   ")
    estadio=st.text_input("Ingresa estadío: ")
    st.write("Actividad Natatoria")
    st.write("Si observamos que el >95% de las larvas nadan activamente, entonces son puntuadas con un 10; si están activas del 70-95%, se puntúa 5; y si son <70% las activas entonces se puntúa 0 (FAO, 2004).")
    actnat=st.text_input("Actividad natatoria: ")
    if st.button("ADD"):
        add_data(fecha,hora,tanque,dia,estadio,actnat)
        st.success("Datos ingresados")

         



     
    
        
        

        
        


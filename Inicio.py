import sqlite3
import streamlit as st 
import datetime
import pandas as pd
from streamlit_navigation_bar import st_navbar


st.sidebar.title ("LarvApp")
st.sidebar.header("App de Gestión para Larvicultura")
st.sidebar.subheader("Laboratorio de Larvas San Pedro")

st.sidebar.write("Inicia Sesión")

username = st.sidebar.text_input("User Name")
password = st.sidebar.text_input("Password",type='password')
if st.sidebar.checkbox("OK"):
    if password == '12345'and username=="edu":
        page = st_navbar(["Algas", "Artemia", "Larvas", "Maduración", "Microbiología", "Buscar","Estadísticas"])
        st.sidebar.success("Logged In as {}".format(username))
        
        if page=="Larvas":
            opcioneslarvas=st.selectbox("Selecciona:",("Control de Calidad","Parámetros","Alimento"),index=None)
            if opcioneslarvas=="Control de Calidad":
                dia=st.text_input("Día# :   ")
                tanque=st.text_input("Tanque # :   ")
                estadio=st.text_input("Ingresa estadío: ")
                st.write("Actividad Natatoria")
                st.write("Si observamos que el >95% de las larvas nadan activamente, entonces son puntuadas con un 10; si están activas del 70-95%, se puntúa 5; y si son <70% las activas entonces se puntúa 0 (FAO, 2004).")
                actnat=st.text_input("Actividad natatoria: ")
                
                if st.button("ADD"):
                    ct = datetime.datetime.now()
                    connection = sqlite3.connect('cclarvas.db',detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
                    cursor = connection.cursor()
                    insertQuery = """INSERT INTO cclarvas VALUES (?, ?,?, ?, ?);"""
                    cursor.execute(insertQuery, (ct,dia,tanque,estadio,actnat))
                    connection.commit()
                    st.success("Datos ingresados")
        if page=="Buscar":
            connection = sqlite3.connect('cclarvas.db',detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
            cursor = connection.cursor()
            cursor.execute("SELECT * from cclarvas")
            fetchedData = cursor.fetchall()
            df=pd.DataFrame(fetchedData,columns = ["fecha y hora","dia","tanque","estadio","act"])
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write("Busca por tanque")
                tanque=st.text_input("Ingresa tanque: ")
                if st.button("Buscar",key="1"):
                    st.dataframe(df[df['tanque'].str.contains(tanque)])
            with col2:
                st.write("Busca por dia")
                dia=st.text_input("Ingresa dia: ")
                if st.button("Buscar",key="2"):
                    st.dataframe(df[df['dia'].str.contains(dia)])
            with col3:
                st.write("Busca por estadio")
                estadio=st.text_input("Ingresa estadio: ")
                if st.button("Buscar",key="3"):
                    st.dataframe(df[df['estadio'].str.contains(estadio)])
             
            

   
    else:
        st.write("Usuario o contraseña incorrectos")               
 
            
            
            
            
            
            
#st.write("Desarrollada por BioPythonic. Todos los derechos reservados. Copyright 2024")
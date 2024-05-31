import sqlite3
import streamlit as st 
import datetime
import pandas as pd
from streamlit_navigation_bar import st_navbar
import yaml


import streamlit_authenticator as stauth

from yaml.loader import SafeLoader
with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
        authenticator = stauth.Authenticate(config['credentials'],config['cookie']['name'],config['cookie']['key'],config['cookie']['expiry_days'])
        authenticator.login()
if st.session_state["authentication_status"]:
        #st.write(f'Bienvenido *{st.session_state["name"]}*') 
        page = ["Algas", "Artemia", "Larvas", "Maduración", "Microbiología", "Buscar","Estadísticas","Salir"]
        
        styles = {
        "nav": {
        "background-color": "#7BD192",
        },
        "div": {
        "max-width": "1050px",
        },
        "span": {
        "border-radius": "0.5rem",
        "padding": "0.4375rem 0.625rem",
        "margin": "0 0.125rem",
        },
        "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
        },
        "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
        },
        }

        page = st_navbar(page, styles=styles)
        
        if page=="Larvas":
            opcioneslarvas=st.selectbox("Selecciona:",("Control de Calidad","Parámetros","Alimento"),index=None)
            if opcioneslarvas=="Control de Calidad":
                dia=st.text_input("Día# :   ")
                tanque=st.text_input("Tanque # :   ")
                estadio=st.text_input("Ingresa estadío: ")
                st.write("Actividad Natatoria")
                st.write("Si observamos que el >95% de las larvas nadan activamente, entonces son puntuadas con un 10; si están activas del 70-95%, se puntúa 5; y si son <70% las activas entonces se puntúa 0 (FAO, 2004).")
                actnat=st.text_input("Actividad natatoria: ")
                

        
        if page=="Salir":
            authenticator.logout()
       

elif st.session_state["authentication_status"] is False:
    st.error('Usuário/Senha is inválido')
elif st.session_state["authentication_status"] is None:
    st.warning('Por Favor, utilize seu usuário e senha!')


                
            
                   
             
            

   
    
            
            
            
            
#st.write("Desarrollada por BioPythonic. Todos los derechos reservados. Copyright 2024")

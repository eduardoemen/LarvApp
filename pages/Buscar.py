import streamlit as st 
import pandas as pd
import mysql.connector


conn = mysql.connector.connect( host="localhost",
                                    port="3306",
                                    user="root",
                                    passwd="0912853207",
                                    db="larvapp"
                                  )



cursor = conn.cursor()
cursor.execute("SELECT * FROM larva")
data = cursor.fetchall()
df = pd.DataFrame(data, columns=["id","fecha","hora","tanque","dia","estadio","actividad natatoria"])
st.dataframe(df) 

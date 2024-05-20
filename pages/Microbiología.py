import streamlit as st
import pandas as pd
import mysql.connector


conn = mysql.connector.connect( host="localhost",
                                    port="3306",
                                    user="root",
                                    passwd="0912853207",
                                    db="larvapp"
                                  )

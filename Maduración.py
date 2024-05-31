import streamlit as st 
import pandas as pd
import sqlite3

import datetime


if st.button("ok"): 
# get the current datetime and store it in a variable
    ct = datetime.datetime.now()
    st.write(ct)
 
import streamlit as st
import pandas as pd
import sqlite3
import os
#fonction de connection et d'excution de requête à la base de donnée

def connect(chemin):
    return sqlite3.connect(chemin)

def sql_executor(raw_code ,conn):
    c = conn.cursor()
    c.execute(raw_code)
    data = c.fetchall()
    return data

st.title("SQLITE with streamlit") 
chemain =st.text_input(" entrer le chemain  vers votre fichier SQLite : ")
if chemain :
    if not os.path.exists(chemain):
        st.error('Le fichier n\'existe pas')
    else:
        conn=connect(chemain)
        st.success('connexion etabli')
        sql = "SELECT name FROM sqlite_master WHERE type='table';"
        with st.expander("liste des tables : "):
            sql = "SELECT name FROM sqlite_master WHERE type='table';"
            tables =sql_executor(sql,conn)
            st.write(tables)

"""import streamlit as st
import pandas as pd
import sqlite3
import requests
import os

def download_database_from_github(github_url, save_path):
    response = requests.get(github_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return True
    else:
        return False

def sql_executor(raw_code, conn):
    c = conn.cursor()
    c.execute(raw_code)
    data = c.fetchall()
    return data

def get_table_names(conn):
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    return [table[0] for table in tables]

def Home():
    st.title("SQLite with Streamlit and Python")
    # GitHub Database Link
    github_link = st.text_input("Enter GitHub Database Link")
    if github_link:
        # Download Database from GitHub
        db_filename = "database.db"
        if download_database_from_github(github_link, db_filename):
            st.success("Database downloaded successfully.")
        else:
            st.error("Failed to download the database. Please check the link.")
            return

        # Connect to the database
        conn = sqlite3.connect(db_filename)
        st.success("Database connected successfully.")
        st.subheader("Database details")
        with st.expander("List of tables"):
            tables = get_table_names(conn)
            sql = "SELECT name as name_of_the_table FROM sqlite_master WHERE type='table';"
            df_table = pd.read_sql(sql, conn)
            st.write("Tables:", df_table)
        st.subheader("Table Details")
        if tables:
            for table in tables:
                with st.expander(f"{table}", expanded=False):
                    sql = f"PRAGMA table_info({table});"
                    df_t = pd.read_sql(sql, conn)
                    st.write(df_t)
        else:
            st.write("No tables found in the database.")
        st.subheader("SQL Query")
        # Columns/Layout
        col1, col2 = st.columns(2)

        with col1:
            with st.form(key='query_form'):
                raw_code = st.text_area("SQL Code Here")
                submit_code = st.form_submit_button("Execute")

        # Results Layouts
        with col2:
            if submit_code:
                st.info("Query Submitted")
                st.code(raw_code)

        # Results

        with st.expander("Result of the query"):
            try:
                query_results = sql_executor(raw_code, conn)
                query_df = pd.DataFrame(query_results)
                st.dataframe(query_df)
            except:
                st.error("Syntax error")

        # Close the database connection
        conn.close()
        os.remove(db_filename)  # Remove the downloaded file after use to clean up

def About():
    st.subheader("About John Doe")
    st.write("Nom: Doe")
    st.write("Prénom: John")
    st.write("Groupe: Groupe X")

def main():
    # Menu
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice == "Home":
        Home()
    elif choice == "About":
        About()

if __name__ == '__main__':
    main()
"""
"""import streamlit as st
import pandas as pd
import os 
import 
plotly.express
 as px

csv_file_path = st.secrets["csv_file_path"]
# Chargement du fichier CSV en nettoyant les espaces dans la colonne Email
df = pd.read_csv(csv_file_path, delimiter=";", converters={"Email": lambda x: x.strip()})

# Titre de l'application
st.title("NOTES DU DS PYTHON")
st.header("1LM A.U 2023-2024")
# Champ de saisie pour l'email de l'étudiant
email = st.text_input("Saisissez votre email")
def categorize_notes(note):
    if note < 10:
        return "Insuffisant (<10)"
    elif 10 <= note < 12:
        return "Passable (10-12)"
    elif 14 <= note < 16:
        return "Bien (14-16)"
    else:
        return "Très bien (>16)"
df["Note"] = pd.to_numeric(df["Note"], errors='coerce').fillna(0)
df["Catégorie de notes"] = df["Note"].apply(categorize_notes)
# Vérification si l'email existe dans le fichier CSV
if email:
    if email in df["Email"].values:
        # Récupération des informations de l'étudiant correspondant à l'email
        etudiant = df[df["Email"] == email]
        nom = etudiant["Name"].values[0]
        groupe = etudiant["GROUP"].values[0]
        note = etudiant["Note"].values[0]
        # Affichage des informations de l'étudiant
        st.success(f"Nom de l'étudiant : {nom}")
        st.success(f"Groupe de l'étudiant : {groupe}")
        st.success(f"La note de l'étudiant est : {note}")

    else:
        st.error("Email non trouvé")






# Calculer les statistiques des notes pour le pie chart
stats_notes = df["Catégorie de notes"].value_counts()

# Créer le pie chart avec Plotly
fig = px.pie(values=stats_notes, names=stats_notes.index, title="Statistiques des notes")
st.plotly_chart(fig) """
import streamlit as st 
import pandas as pd
import sqlite3 
import os

def sql_executor(raw_code, conn):
    c = conn.cursor()
    c.execute(raw_code)
    data = c.fetchall()
    return data 

def get_table_names(conn):
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    return [table[0] for table in tables]

def Home():
    st.title("SQLlite with Streamlit and Python")
    # Select Database
    db_file_path = st.text_input("Enter Database File Path😊")
    if db_file_path:
        # Check if file exists
        if not os.path.exists(db_file_path):
            st.error("Le fichier spécifié n'existe pas.")
            return

        # Display the selected file path
        st.write("Selected Database Path:", db_file_path)

        # Connect to the database
        conn = sqlite3.connect(db_file_path)
        st.success("Database connected successfully.")
        st.subheader("Database details")
        with st.expander("List of tables"):
            tables = get_table_names(conn)
            sql = "SELECT name as name_of_the_table FROM sqlite_master WHERE type='table';"
            df_table = pd.read_sql(sql, conn)
            st.write("Tables:", df_table) 
        st.subheader("Table Details")
        if tables:
            for table in tables:
                with st.expander(f"{table}", expanded=False):
                   sql = f"PRAGMA table_info({table});"
                   df_t =pd.read_sql(sql, conn)
                   st.write(df_t)
        else:
            st.write("No tables found in the database.")
        st.subheader("SQL Query")
        # Columns/Layout
        col1,col2 = st.columns(2)

        with col1:
            with st.form(key='query_form'):
                raw_code = st.text_area("SQL Code Here")
                submit_code = st.form_submit_button("Execute")

        # Results Layouts
        with col2:
            if submit_code:
                
                st.info("Query Submitted")
                st.code(raw_code)

        # Results

        with st.expander("Result of the query"):
            try:
                query_results = sql_executor(raw_code, conn) 
                query_df = pd.DataFrame(query_results)
                st.dataframe(query_df)
            except:
                st.error("Syntax error")
        
        # Table of Info
        
        # Close the database connection
        conn.close()
def About():
    st.subheader("About John Doe")
    st.write("Nom: Doe")
    st.write("Prénom: John")
    st.write("Groupe: Groupe X")
def main():
    # Menu
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice =="Home":
        Home()
    elif choice =="About":
        About()
    
if __name__ == '__main__':
    main() 

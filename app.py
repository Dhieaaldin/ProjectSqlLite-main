import streamlit as st
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

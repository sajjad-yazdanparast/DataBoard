import pandas as pd
import streamlit as st
import mysql.connector

def get_connection(user, password, host, db = None, *args, **kwargs) :
    cnx = mysql.connector.connect(
        user=user,
        host=host,
        password=password,
        database=db
    )
    return cnx


def get_database_names(cnx) :
    cursor = cnx.cursor()
    cursor.execute('SHOW DATABASES;')
    return cursor.fetchall()


def get_all_tables_in_database(cnx, db_name) :
    cursor = cnx.cursor()
    cursor.execute(f"USE {db_name};")
    cursor.execute('SHOW TABLES;')
    return cursor.fetchall()

def get_table_in_database(cnx, db_name, table_name) :
    cursor = cnx.cursor()
    cursor.execute(f"USE {db_name};")
    cursor.execute(f"SELECT * from {table_name}")
    return pd.DataFrame(cursor.fetchall(), columns = [i[0] for i in cursor.description])

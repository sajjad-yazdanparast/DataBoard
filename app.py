import streamlit as st
import os
import matplotlib.pyplot as plt
from database_interface.utils import *
st.set_page_config(
    page_title='DataBoard' ,
    page_icon= plt.imread(os.path.abspath('static/logo.png')),
)


if st.checkbox('Use remote database?') :
    cnx = get_connection(user=st.secrets.db_username, password=st.secrets.db_password, host=st.secrets.db_host)
    databases = [db[0] for db in get_database_names(cnx)]
    st.session_state.databases = databases
else :
    cnx = get_connection(user='sajjad_quera', password="P@ssword1401", host='localhost')
    databases = [db[0] for db in get_database_names(cnx)]
    st.session_state.databases = databases


def on_table_radio_change(db_name) :
    if db_name in st.session_state :
        table_selected = st.session_state.get(db_name)
        st.subheader(f'{table_selected} table from {db_name} database dashboarding')
        st.dataframe(get_table_in_database(cnx,db_name = db_name, table_name= table_selected))


st.sidebar.title('DataBases')
with st.sidebar:
    for db in st.session_state.databases :
        with st.expander(db) :
            tables = get_all_tables_in_database(cnx, db)
            tables = [table[0] for table in tables]

            table_selected = st.radio(
                label = 'tables',
                options= tables,
                label_visibility='collapsed' ,
                key = db  ,
                on_change = on_table_radio_change,
                kwargs={"db_name" : db}

            )



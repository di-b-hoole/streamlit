import streamlit as st
#from gsheetsdb import connect
from shillelagh.backends.apsw.db import connect

conn = connect(":memory:")
cursor = conn.cursor()

@st.cache(ttl=600)
def run_query(query):
    rows = cursor.execute(query)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

for row in cursor.execute(query):
    st.write(row)
#sheet_url = st.secrets["public_gsheets_url"]
#
## Create a connection object.
#connection = connect(f'{sheet_url}')
#cursor = connection.cursor()
#
#
#query = f'SELECT * FROM "{sheet_url}"'
#for row in cursor.execute(query):
#    print(row)





#conn = connect()
#
## Perform SQL query on the Google Sheet.
## Uses st.cache to only rerun when the query changes or after 10 min.
#@st.cache(ttl=600)
#def run_query(query):
#    rows = conn.execute(query, headers=1)
#    rows = rows.fetchall()
#    return rows
#
#sheet_url = st.secrets["public_gsheets_url"]
#rows = run_query(f'SELECT * FROM "{sheet_url}"')
#
## Print results.
#for row in rows:
#    st.write(f"{row.Client} has a :{row.Value}:")

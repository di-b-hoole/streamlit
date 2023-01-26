import streamlit as st
#from gsheetsdb import connect
from shillelagh.backends.apsw.db import connect

conn = connect(":memory:")
cursor = conn.cursor()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = cursor.execute(query)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

query = f'SELECT * FROM "{sheet_url}"'

# Print results.
for row in cursor.execute(query):
    st.write(row)
    st.write(f"{row[0]} has a :{row[1]}:")

query = (
    f'UPDATE "{sheet_url}"'
    " SET Client = 'Brydon'"
    " WHERE Client = 'Bravo'"
)

st.write(query)

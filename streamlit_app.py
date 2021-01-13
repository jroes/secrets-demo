import time

#time.sleep(10)

import streamlit as st
import os
import os.path

from gsheetsdb import connect

st.title("Hello!")

try:
    with open(".streamlit/secrets.toml") as f:
        st.text(f.read())
except FileNotFoundError:
    st.text('No secrets file found, probably not ready yet, or running locally!')

secret_url = os.environ['SECRET_URL']
secret_url

conn = connect()
result = conn.execute(f"""
    SELECT
      *
    FROM
        "{secret_url}"
""", headers=1)

st.json(list(result))

#st.json(dict(os.environ))

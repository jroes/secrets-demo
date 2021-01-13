import time

#time.sleep(10)

import streamlit as st
import os
import os.path
import secrets_beta

from gsheetsdb import connect

st.title("Hello!")

secret_url = st.secrets["SECRET_URL"]
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

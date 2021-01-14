import streamlit as st
import os
import os.path
import secrets_beta
import pandas as pd

from gsheetsdb import connect

def download_spreadsheet(url):
    conn = connect()
    result = conn.execute(f'SELECT * FROM "{url}"', headers=1)
    return pd.DataFrame(list(result))

st.title("[Secrets Demo] Nuclear Launch Codes")

password = st.text_input('What is the secret password?')
if password == st.secrets["SECRET_PASSWORD"]:
    secret_url = st.secrets["SECRET_URL"]

    st.subheader("Codes")
    st.write(download_spreadsheet(secret_url))

    if st.button("Launch"):
        st.balloons()

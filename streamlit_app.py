import streamlit as st
import os
import os.path
import secrets_beta
import pandas as pd

from gsheetsdb import connect

st.title("2021 Engineering OKRs")

secret_url = st.secrets["SECRET_URL"]
with st.beta_expander('Secret value'):
    secret_url

conn = connect()
result = conn.execute(f'SELECT Category, Description FROM "{secret_url}"', headers=1)

df = pd.DataFrame(list(result), columns=['Category', 'Description'])
with st.beta_expander('Raw data'):
    st.table(df)

st.subheader("Count by category")
st.bar_chart(df.groupby("Category").count())

st.subheader("Word frequency")
freq = pd.Series(' '.join(df.Description).split()).value_counts()[:25]
st.bar_chart(freq)

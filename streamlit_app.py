import pandas as pd
import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Demo Mario",
    page_icon="	:snake:",
    layout="wide",
    initial_sidebar_state='collapsed'
)
col1, col2, col3 = st.columns([1,4,1])

col1.image('https://github.com/andrejarenkow/PainelOvitrampas/blob/main/logo_cevs%20(1).png?raw=true', width=200)
col2.title('Demo mario')
col3.image('https://github.com/andrejarenkow/PainelOvitrampas/blob/main/logo_estado%20(3).png?raw=true', width=300)


dados = pd.read_table('https://docs.google.com/spreadsheets/d/e/2PACX-1vSdSfuuSRSruaUrc7zpPqWzbPBeTKDGB-Y5xgfIhZND_gityoaYJp-_ja_P5hBBKyFbHA_5y70zPRpt/pub?gid=1357651511&single=true&output=tsv')

dados

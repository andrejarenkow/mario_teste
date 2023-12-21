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

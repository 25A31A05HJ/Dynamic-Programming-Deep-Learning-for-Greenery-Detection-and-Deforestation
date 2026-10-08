import streamlit as st
from pathlib import Path
st.set_page_config(page_title='GeoAI Change Analysis',layout='wide')
st.title('GeoAI: Lakes, Roads & Urban Drainage')
st.caption('Project dashboard scaffold based on the supplied four-document specification.')
cols=st.columns(4)
for c,t in zip(cols,['Module A — Lakes','Module B — Roads','Module C — Drainage','Module D — Change']): c.metric(t,'Ready for data')
st.subheader('Project status')
for p in ['data/raw','data/interim','data/processed','models','reports']:
    st.write(f'**{p}** — {len(list(Path(p).glob("*")))} item(s)')
st.info('Add processed rasters, reference labels and model outputs to populate maps, metrics and time-series panels.')

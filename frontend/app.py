import streamlit as st
from streamlit import components
import folium


st.set_page_config(page_title="Spaziergang in Berlin", layout="wide")
st.title("Spaziergang in Berlin")

st.sidebar.header("Einstellungen")
col1, col2 = st.sidebar.columns(2)
start_lat = col1.number_input("Start Lat", value=52.52, format="%.6f")
start_lon = col2.number_input("Start Lon", value=13.405, format="%.6f")
minutes = st.sidebar.number_input("Zeit (Minuten)", min_value=5, max_value=240, value=60, step=5)
ice_end = st.sidebar.checkbox("Eis am Ende", value=False)

# Placeholder map: center on Berlin
center = (52.52, 13.405)
m = folium.Map(location=center, zoom_start=12, control_scale=True, tiles="cartodbpositron")

# Optionally show start marker if provided
folium.Marker(location=(start_lat, start_lon), tooltip="Start").add_to(m)

st.subheader("Karte")
components.v1.html(m._repr_html_(), height=600)

# Show current inputs (for debugging/demo)
st.write({
    "start": (start_lat, start_lon),
    "minutes": minutes,
    "ice_at_end": ice_end,
})


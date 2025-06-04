import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
import plotly.express as px

# Configuración inicial de la app
st.set_page_config(page_title="MetaLytics AI Dashboard", layout="wide")
st.title("🧠 MetaLytics AI - Gestión Integral de Relaves")

# Sidebar para carga y filtros de datos
st.sidebar.header("📂 Carga y Filtros")
archivo = st.sidebar.file_uploader("Sube archivo CSV de relaves SERNAGEOMIN", type="csv")

if archivo:
    df = pd.read_csv(archivo)

    # Filtros dinámicos
    regiones = df['Region'].dropna().unique()
    region_seleccionada = st.sidebar.selectbox("Selecciona Región", ["Todas"] + list(regiones))

    if region_seleccionada != "Todas":
        df = df[df['Region'] == region_seleccionada]

    # Mapa interactivo
    st.subheader("📍 Mapa de Depósitos de Relaves")
    mapa = folium.Map(location=[-33.45, -70.66], zoom_start=5)

    for _, row in df.iterrows():
        if pd.notnull(row['Latitud']) and pd.notnull(row['Longitud']):
            folium.Marker(
                location=[row['Latitud'], row['Longitud']],
                popup=f"{row['Nombre']} ({row['Estado']})",
                icon=folium.Icon(color="green" if row['Estado'] == "Activo" else "red")
            ).add_to(mapa)

    folium_static(mapa, width=1000)

    # Análisis de estado operativo
    st.subheader("📊 Estado Operativo de Relaves")
    estado_counts = df['Estado'].value_counts()
    fig_estado = px.pie(names=estado_counts.index, values=estado_counts.values,
                        title="Distribución por Estado Operativo")
    st.plotly_chart(fig_estado, use_container_width=True)

    # Espacio para futuras integraciones
    st.markdown("---")
    st.subheader("🔬 Integraciones en Desarrollo")
    st.info("Aquí se mostrarán módulos de biorremediación, modelado predictivo, monitoreo con sensores, entre otros.")

else:
    st.warning("Por favor, sube un archivo CSV válido para iniciar el análisis.")

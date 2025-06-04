# metalytics_dashboard.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from streamlit_folium import folium_static

# Configuración inicial
st.set_page_config(page_title="Meta4.0 – Minería Digital Integral", layout="wide")

# Sidebar
with st.sidebar:
    st.header("🔧 Filtros y Configuración")
    selected_category = st.selectbox(
        "Selecciona una categoría",
        [
            "🏠 Panel Principal",
            "🌐 Digitalización y Monitoreo",
            "🧬 Biotecnología y Remediation",
            "♻️ Minería Circular",
            "🤖 Modelos Predictivos",
            "🌍 Planificación Territorial",
            "☀️ Energía Sostenible",
            "📈 Visualización de Resultados"
        ]
    )

# Panel Principal – Vista General
if selected_category == "🏠 Panel Principal":
    st.title("📊 Meta4.0 – Minería Digital Integral")
    st.markdown("🔍 Transformando residuos mineros en activos económicos y ecológicos.")
    
    relave_data = {
        "Empresa": "CIA. CONTRACTUAL MINERA CANDELARIA",
        "Región": "III – Atacama",
        "Comuna": "Copiapó",
        "Tipo de Relave": "Tranque de Relave",
        "Estado Actual": "Inactivo",
        "Volumen autorizado": "18,900,000 m³",
        "Ley oro residual": "132 g/t",
        "Ley cobre residual": "1,028 g/t",
        "pH promedio": "4.06",
        "Mineralogía dominante": "Calcopirita",
        "Riesgo ambiental": "Medio-Alto (DAM/PGA)",
        "Valor recuperable estimado": "$2,147,400,000 USD",
        "Score de Estabilidad Final": "0.87",
        "Score de LSO": "0.85",
        "NPV": "$987,246 USD",
        "ROI esperado": "58%"
    }

    df_relave = pd.DataFrame([relave_data])
    st.table(df_relave)

    # Gráfico de barras de metales recuperables
    metal_data = pd.DataFrame({
        "Metal": ["Cobre", "Oro"],
        "Valor Estimado (USD)": [649_100_000, 1_498_300_000]
    })
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='Metal', y='Valor Estimado (USD)', data=metal_data, palette='magma')
    plt.title("Valor Metálico Recuperable Estimado")
    plt.xlabel("Metal")
    plt.ylabel("Valor Estimado (USD)")
    plt.grid(True)
    st.pyplot(fig)

    # Mapa geoestadístico interactivo
    st.subheader("🗺️ Mapa Geoestadístico")
    m = folium.Map(location=[-26.8237, -69.6584], zoom_start=15)
    folium.Marker([-26.8237, -69.6584], popup="Relave 0161-3N – Gigante Norte").add_to(m)
    folium_static(m)

# PANEL 1: DIGITALIZACIÓN Y MONITOREO INTELIGENTE
elif selected_category == "🌐 Digitalización y Monitoreo":
    st.title("🌐 Panel 1: Digitalización y Monitoreo Inteligente")
    st.markdown("""
    - Dashboards operativos en tiempo real  
    - Mapas geoestadísticos interactivos  
    - Alertas automatizadas de subsidencia y contaminación  
    - Gemelos digitales y simulación predictiva  
    """)
    
    stability_data = pd.DataFrame({
        "Tipo": ["Antes", "Después"],
        "Score Estabilidad": [0.60, 0.87]
    })
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='Tipo', y='Score Estabilidad', data=stability_data, palette='viridis')
    plt.title("Mejora en Score de Estabilidad Geomecánica")
    plt.ylabel("Score de Estabilidad")
    plt.grid(True)
    st.pyplot(fig)

# PANEL 2: BIOTECNOLOGÍA APLICADA Y REMEDIATION
elif selected_category == "🧬 Biotecnología y Remediation":
    st.title("🧬 Panel 2: Biotecnología Aplicada y Remediation")
    st.markdown("""
    - Recomendación de cepas microbianas optimizadas  
    - Phytoremediation con plantas nativas chilenas  
    - Bio-backfilling y pasivación ambiental  
    - Biorremediación usando biofilm  
    """)
    
    recovery_data = pd.DataFrame({
        "Metal": ["Cobre", "Oro", "Níquel", "Vanadio", "Molibdeno"],
        "Eficiencia (%)": [82.5, 74.2, 80.0, 85.0, 83.0]
    })
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='Metal', y='Eficiencia (%)', data=recovery_data, palette='magma')
    plt.title("Eficiencia de Recuperación Metálica")
    plt.xlabel("Metal")
    plt.ylabel("Eficiencia (%)")
    plt.xticks(rotation=45, ha='right')
    plt.grid(True)
    st.pyplot(fig)

# PANEL 3: MINERÍA CIRCULAR Y VALORIZACIÓN
elif selected_category == "♻️ Minería Circular":
    st.title("♻️ Panel 3: Minería Circular y Valorización")
    st.markdown("""
    - Valorización de metales secundarios y subproductos  
    - Backfill biológico y cemento con relaves tratados  
    - Reciclaje industrial de cenizas y lodos  
    - Rutas de cierre de ciclo minero  
    """)
    
    revenue_data = pd.DataFrame({
        "Mes": range(1, 13),
        "Ingresos Circulares (USD)": [120_000, 130_000, 150_000, 170_000, 190_000, 200_000, 210_000, 220_000, 230_000, 240_000, 250_000, 260_000]
    })
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.lineplot(x='Mes', y='Ingresos Circulares (USD)', data=revenue_data, marker='o', color='green')
    plt.title("Ingresos Circulares Mensuales")
    plt.xlabel("Mes")
    plt.ylabel("Ingresos (USD)")
    plt.grid(True)
    st.pyplot(fig)

# PANEL 4: MODELOS PREDICTIVOS CON IA
elif selected_category == "🤖 Modelos Predictivos":
    st.title("🤖 Panel 4: Modelos Predictivos con IA")
    st.markdown("""
    - Redes Neuronales Artificiales (ANNs)  
    - Simulación de procesos metalúrgicos  
    - Análisis de sensibilidad y riesgos  
    - Generación de escenarios económicos y ambientales  
    """)
    
    model_error_data = pd.DataFrame({
        "Modelo": ["ANN", "XGBoost", "Random Forest", "Linear Regression"],
        "Error (MSE)": [0.002, 0.003, 0.004, 0.005]
    })
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='Modelo', y='Error (MSE)', data=model_error_data, palette='coolwarm')
    plt.title("Comparación de Error entre Modelos Predictivos")
    plt.ylabel("Error Cuadrático Medio (MSE)")
    plt.grid(True)
    st.pyplot(fig)

# PANEL 5: PLANIFICACIÓN GEOESTADÍSTICA Y TERRITORIAL
elif selected_category == "🌍 Planificación Territorial":
    st.title("🌍 Panel 5: Planificación Geoestadística y Territorial")
    st.markdown("""
    - Teledetección multispectral y big data  
    - Estabilidad geomecánica con FEA y GPR  
    - Mapeo de subsidencias y estabilización  
    - Cumplimiento regulatorio y ODS  
    """)
    
    subsidence_data = pd.DataFrame({
        "Mes": range(1, 13),
        "Subsidencia (mm)": [0.5, 0.6, 0.8, 1.0, 1.2, 1.4, 1.5, 1.3, 1.2, 1.1, 0.9, 0.7]
    })
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.lineplot(x='Mes', y='Subsidencia (mm)', data=subsidence_data, marker='x', color='blue')
    plt.title("Subsidencia Detectada con Teledetección")
    plt.xlabel("Mes")
    plt.ylabel("Subsidencia (mm)")
    plt.grid(True)
    st.pyplot(fig)

# PANEL 6: ENERGÍA SOSTENIBLE
elif selected_category == "☀️ Energía Sostenible":
    st.title("☀️ Panel 6: Energía Sostenible y Transición Energética")
    st.markdown("""
    - Uso de energía solar térmica  
    - Captación de agua lluvia  
    - Gasificación rápida de residuos  
    - Sistemas de energía distribuida  
    """)
    
    co2_reduction_data = pd.DataFrame({
        "Tipo": ["Conventional", "Solar Thermal", "Gasification", "Water Recycling"],
        "Reducción CO₂ (%)": [0, 30, 40, 20]
    })
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='Tipo', y='Reducción CO₂ (%)', data=co2_reduction_data, palette='Greens')
    plt.title("Reducción de Huella de Carbono")
    plt.ylabel("Porcentaje de Reducción")
    plt.grid(True)
    st.pyplot(fig)

# PANEL 7: VISUALIZACIÓN DE RESULTADOS
elif selected_category == "📈 Visualización de Resultados":
    st.title("📈 Panel 7: Visualización de Resultados")
    st.markdown("""
    - Dashboards interactivos con Streamlit  
    - Gráficos dinámicos con Matplotlib y Seaborn  
    - Exportación automática a PDF, CSV, HTML  
    - UI/UX profesional basada en estándares médicos  
    """)
    
    phase_data = pd.DataFrame({
        "Fase": ["Evaluación", "Diseño", "Simulación", "Implementación"],
        "Duración (días)": [7, 15, 30, 90]
    })
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x='Fase', y='Duración (días)', data=phase_data, palette='Pastel1')
    plt.title("Duración Estimada por Fase del Proyecto")
    plt.ylabel("Duración (días)")
    plt.grid(True)
    st.pyplot(fig)

else:
    st.warning("Por favor selecciona una categoría desde el menú lateral.")
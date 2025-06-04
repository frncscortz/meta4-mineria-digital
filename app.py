import streamlit as st

st.set_page_config(page_title="Meta4.0 – Minería Digital Integral", layout="wide")

# Título y descripción
st.title("📊 Meta4.0 – Minería Digital Integral")
st.markdown("🔍 Transformando residuos mineros en activos económicos y ecológicos.")

# Sidebar con opciones
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


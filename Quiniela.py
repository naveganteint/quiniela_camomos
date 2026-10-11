import streamlit as st


from utils.styles import aplicar_estilos
from pathlib import Path
import streamlit as st

aplicar_estilos()


BASE_DIR = Path(__file__).resolve().parent
LOGO = BASE_DIR / "utils" / "images" / "logo-quiniela.png"
icon = BASE_DIR / "utils" / "images" / "favicon.ico"

st.set_page_config(
    page_title="Comprobador de La Quiniela",
    page_icon=icon,
    layout="wide"
)



st.markdown("""

<div style="text-align: center;">

<h1> Comprobador de La Quiniela</h1>

<h2>Bienvenido a la Quiniela Camomos</h2>

<p>
Esta aplicación permite introducir una quiniela y comprobar
los resultados de los partidos.
</p>

</div>
""", unsafe_allow_html=True)


col1,col2,col3= st.columns([3, 1.2, 3])

with col2:
    st.image("utils/images/logo-quiniela.png")





st.markdown("""

<div style="text-align: center;">




<h3>Opciones disponibles</h3>

<p>🎯 Introducir Quiniela con 7 dobles</p>
<p>🎯 Introducir Quiniela con 8 dobles</p>
<p>📊 Comprobación de resultados</p>

<p><i>Utiliza el menú lateral para comenzar.</i></p>

</div>
""", unsafe_allow_html=True)
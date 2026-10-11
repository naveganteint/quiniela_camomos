import streamlit as st
from pathlib import Path
from utils.styles import aplicar_estilos
from datetime import datetime

aplicar_estilos()

# ---------------------------------------------------------
# CONFIGURACIÓN
# ---------------------------------------------------------



# Directorio del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Fichero donde guardaremos la quiniela
FICHERO = BASE_DIR / "utils" / "datos" / "7_dobles.txt"


# ---------------------------------------------------------
# CREAR CARPETA DE DATOS SI NO EXISTE
# ---------------------------------------------------------

FICHERO.parent.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------
# TÍTULO
# ---------------------------------------------------------

st.markdown("""
<style>
.block-container {
    padding-top: 1.7rem !important;
}
</style>
""", unsafe_allow_html=True)




st.markdown(
    """
    <div style="text-align: center;">

    <h3 style="
    background-color: #ff9997;
    padding: 8px 15px;
    border-radius: 8px;
    display: inline-block;
    font-weight: bold;">Introducir Quiniela - 7 Dobles</h3>
    
    <p>
    Selecciona el pronóstico de cada partido.
    Puedes marcar uno o dos resultados por partido.
    </p>

    <p style="
    background-color: #d9f0ff;
    padding: 8px 15px;
    border-radius: 8px;
    display: inline-block;
    font-weight: bold;
    ">
    Debes seleccionar 7 dobles.
    </p>




    </div><br>
    """,
    unsafe_allow_html=True
)

simples = 0
dobles=0
triples=0
errores = []


# ---------------------------------------------------------
# CABECERA
# ---------------------------------------------------------




esp1,col_partido, col_1, col_x, col_2,esp2 = st.columns([3,2, 0.3, 0.3, 0.3,3])

with col_partido:
    st.markdown("<div style=''><b>Partido</b></div>", unsafe_allow_html=True)

with col_1:
    st.markdown("<div style='text-align: center;'><b>1</b></div>", unsafe_allow_html=True)

with col_x:
    st.markdown("<div style='text-align: center;'><b>X</b></div>", unsafe_allow_html=True)

with col_2:
    st.markdown("<div style='text-align: center;'><b>2</b></div>", unsafe_allow_html=True)


# Línea solo en la zona central
with col_partido:
    st.markdown(
        "<hr style='margin-top: 2px; margin-bottom: 2px;'>",
        unsafe_allow_html=True
    )

with col_1:
    st.markdown(
        "<hr style='margin-top: 2px; margin-bottom: 2px;'>",
        unsafe_allow_html=True
    )

with col_x:
    st.markdown(
        "<hr style='margin-top: 2px; margin-bottom: 2px;'>",
        unsafe_allow_html=True
    )

with col_2:
    st.markdown(
        "<hr style='margin-top: 2px; margin-bottom: 2px;'>",
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# 14 PARTIDOS
# ---------------------------------------------------------

pronosticos = []

st.markdown("""
<style>
div[data-testid="column"] {
    padding-top: 0px !important;
    padding-bottom: 0px !important;
}

div[data-testid="stCheckbox"] {
    margin-top: -8px !important;
    margin-bottom: -8px !important;
}
</style>
""", unsafe_allow_html=True)


for partido in range(1, 15):

    esp1,col_partido, col_1, col_x, col_2,esp2 = st.columns([3,2, 0.3, 0.3, 0.3,3])

    with col_partido:
        
        st.markdown(f"<div style=''><b>Partido {partido}</b></div>", unsafe_allow_html=True)


    with col_1:
         col_c1, col_c2, col_c3 = st.columns([ 2, 1, 2])

         with col_c2:
                resultado_1 = st.checkbox(
                    "1",
                    key=f"partido_{partido}_1",
                    label_visibility="collapsed"
                )


    with col_x:
         col_c1, col_c2, col_c3 = st.columns([ 2, 1, 2])

         with col_c2:
                resultado_x = st.checkbox(
                    "X",
                    key=f"partido_{partido}_x",
                    label_visibility="collapsed"
                )

    with col_2:
         col_c1, col_c2, col_c3 = st.columns([ 2, 1, 2])

         with col_c2:
            resultado_2 = st.checkbox(
                "2",
                key=f"partido_{partido}_2",
                label_visibility="collapsed"
            )

    seleccionados = []

    if resultado_1:
        seleccionados.append("1")

    if resultado_x:
        seleccionados.append("X")

    if resultado_2:
        seleccionados.append("2")

    pronosticos.append(seleccionados)




partidos_marcados = sum(
    1 for p in pronosticos
    if len(p) > 0
)




# ---------------------------------------------------------
# COMPROBAR PRONÓSTICOS
# ---------------------------------------------------------



for numero, seleccionados in enumerate(pronosticos, start=1):

    cantidad = len(seleccionados)

    if cantidad == 1:
        simples += 1

    elif cantidad == 2:
        dobles += 1

    elif cantidad == 3:
        errores.append(
            f"El partido {numero} tiene marcado un triple.")
        triples += 1 
           

    elif cantidad == 0:
        errores.append(
            f"El partido {numero} no tiene ningún pronóstico."
        )


# ---------------------------------------------------------
# INFORMACIÓN
# ---------------------------------------------------------

st.markdown(
    """
    <hr style="
        width: 75%;
        margin: 10px auto;
        border: none;
        border-top: 1px solid #999;
    ">
    """,
    unsafe_allow_html=True
)

esp1,col1, col2, col3, col4,esp2 = st.columns([3,1,1,1,1,3])

with col1:
    st.metric("simples", f"{simples} ")

with col2:
    st.metric("Dobles", f"{dobles} ")


with col3:
    st.metric("Triple", f"{triples} ")

with col4:

    st.metric("Partidos marcados", f"{partidos_marcados}")


# ---------------------------------------------------------
# BOTÓN GUARDAR
# ---------------------------------------------------------

st.markdown(
    """
    <hr style="
        width: 75%;
        margin: 10px auto;
        border: none;
        border-top: 1px solid #999;
    ">
    """,
    unsafe_allow_html=True
)

st.write("")

col1, col2, col3= st.columns([3,2,3])
with col2:
    if st.button("💾 Guardar Quiniela", type="primary",use_container_width=True):

        if errores:
            st.error("Hay errores en la quiniela:")

            for error in errores:
                st.write(f"❌ {error}")

        elif dobles != 7:
            st.error(
                f"Debes seleccionar exactamente 7 dobles. "
                f"Actualmente tienes {dobles}."
            )

        elif simples != 7:
            st.error(
                f"Debes tener exactamente 7 simples. "
                f"Actualmente tienes {simples}."
            )

        else:

            # Fecha del día
            fecha = datetime.now().strftime("%d/%m/%Y")

            # Crear el contenido del fichero
            lineas = []

            for numero, seleccionados in enumerate(
                pronosticos,
                start=1
            ):

                pronostico = "".join(seleccionados)

                lineas.append(
                    f"{numero}|{pronostico}"
                )

            # Primera línea = fecha
            contenido = fecha + "\n" + "\n".join(lineas)

            # Guardar
            FICHERO.write_text(
                contenido,
                encoding="utf-8"
            )

            st.success(
                "✅ Quiniela guardada correctamente."
            )

            st.write(
                f"Fichero: `{FICHERO}`")

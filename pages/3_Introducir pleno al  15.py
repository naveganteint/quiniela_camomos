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

# Fichero donde guardaremos el Pleno al 15
FICHERO = BASE_DIR / "utils" / "datos" / "pleno_15.txt"


# ---------------------------------------------------------
# CREAR CARPETA DE DATOS SI NO EXISTE
# ---------------------------------------------------------

FICHERO.parent.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------
# FUNCIÓN PARA DEJAR SOLO UN CHECKBOX MARCADO
# ---------------------------------------------------------

def seleccionar_resultado(equipo, resultado_seleccionado):

    resultados = ["0", "1", "2", "M"]

    for resultado in resultados:

        if resultado != resultado_seleccionado:

            st.session_state[
                f"equipo_{equipo}_{resultado}"
            ] = False


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
    font-weight: bold;">
    Introducir Pleno al 15
    </h3>

    <p>
    Selecciona el pronóstico del resultado de este partido.
    </p>

    <p style="
    background-color: #d9f0ff;
    padding: 8px 15px;
    border-radius: 8px;
    display: inline-block;
    font-weight: bold;
    ">
    ¿Cuántos goles marcará cada equipo?
    </p>

    </div><br>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# CABECERA
# ---------------------------------------------------------

esp1, col_partido, col_1, col_2, col_3, col_4, esp2 = st.columns(
    [3, 2, 1, 1, 1, 1, 3]
)


with col_partido:
    st.markdown(
        "<div><b>Partido</b></div>",
        unsafe_allow_html=True
    )


with col_1:
    st.markdown(
        "<div style='text-align: center;'><b>0</b></div>",
        unsafe_allow_html=True
    )


with col_2:
    st.markdown(
        "<div style='text-align: center;'><b>1</b></div>",
        unsafe_allow_html=True
    )


with col_3:
    st.markdown(
        "<div style='text-align: center;'><b>2</b></div>",
        unsafe_allow_html=True
    )


with col_4:
    st.markdown(
        "<div style='text-align: center;'><b>M</b></div>",
        unsafe_allow_html=True
    )


# ---------------------------------------------------------
# LÍNEA DE SEPARACIÓN
# ---------------------------------------------------------

for columna in [col_partido, col_1, col_2, col_3, col_4]:

    with columna:

        st.markdown(
            "<hr style='margin: 2px 0;'>",
            unsafe_allow_html=True
        )


# ---------------------------------------------------------
# ESPACIO
# ---------------------------------------------------------

st.write("")
st.write("")


# ---------------------------------------------------------
# PRONÓSTICOS
# ---------------------------------------------------------

pronosticos = []


for equipo in range(1, 3):

    esp1, col_partido, col_1, col_2, col_3, col_4, esp2 = st.columns(
        [3, 2, 1, 1, 1, 1, 3]
    )


    # -----------------------------------------------------
    # NOMBRE DEL EQUIPO
    # -----------------------------------------------------

    with col_partido:

        st.markdown(
            f"<div><b>Equipo {equipo}</b></div>",
            unsafe_allow_html=True
        )


    # -----------------------------------------------------
    # RESULTADO 0
    # -----------------------------------------------------

    with col_1:

        col_c1, col_c2, col_c3 = st.columns([2, 1, 2])

        with col_c2:

            resultado_0 = st.checkbox(
                "0",
                key=f"equipo_{equipo}_0",
                label_visibility="collapsed",
                on_change=seleccionar_resultado,
                args=(equipo, "0")
            )


    # -----------------------------------------------------
    # RESULTADO 1
    # -----------------------------------------------------

    with col_2:

        col_c1, col_c2, col_c3 = st.columns([2, 1, 2])

        with col_c2:

            resultado_1 = st.checkbox(
                "1",
                key=f"equipo_{equipo}_1",
                label_visibility="collapsed",
                on_change=seleccionar_resultado,
                args=(equipo, "1")
            )


    # -----------------------------------------------------
    # RESULTADO 2
    # -----------------------------------------------------

    with col_3:

        col_c1, col_c2, col_c3 = st.columns([2, 1, 2])

        with col_c2:

            resultado_2 = st.checkbox(
                "2",
                key=f"equipo_{equipo}_2",
                label_visibility="collapsed",
                on_change=seleccionar_resultado,
                args=(equipo, "2")
            )


    # -----------------------------------------------------
    # RESULTADO M
    # -----------------------------------------------------

    with col_4:

        col_c1, col_c2, col_c3 = st.columns([2, 1, 2])

        with col_c2:

            resultado_M = st.checkbox(
                "M",
                key=f"equipo_{equipo}_M",
                label_visibility="collapsed",
                on_change=seleccionar_resultado,
                args=(equipo, "M")
            )


    # -----------------------------------------------------
    # GUARDAR RESULTADO DEL EQUIPO
    # -----------------------------------------------------

    seleccionados = []


    if resultado_0:
        seleccionados.append("0")


    if resultado_1:
        seleccionados.append("1")


    if resultado_2:
        seleccionados.append("2")


    if resultado_M:
        seleccionados.append("M")


    pronosticos.append(seleccionados)


# ---------------------------------------------------------
# BOTÓN GUARDAR
# ---------------------------------------------------------

st.write("")


# ---------------------------------------------------------
# BOTÓN GUARDAR
# ---------------------------------------------------------

st.markdown(
    """
    <hr style="
        width: 60%;
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





    if st.button(
        "💾 Guardar Pleno al 15",
        use_container_width=True,
        type="primary"
    ):

        # Comprobar que los dos equipos tienen resultado
        equipos_completos = all(
            len(seleccionados) == 1
            for seleccionados in pronosticos
        )


        if not equipos_completos:

            st.error(
                "⚠️ Debes seleccionar un resultado para los dos equipos."
            )


        else:

            # -------------------------------------------------
            # FECHA
            # -------------------------------------------------

            fecha = datetime.now().strftime("%d/%m/%Y")


            # -------------------------------------------------
            # CREAR CONTENIDO
            # -------------------------------------------------

            lineas = []


            for numero, seleccionados in enumerate(
                pronosticos,
                start=1
            ):

                pronostico = "".join(seleccionados)

                lineas.append(
                    f"Equipo {numero}|{pronostico}"
                )


            # Primera línea = fecha
            contenido = fecha + "\n" + "\n".join(lineas)


            # -------------------------------------------------
            # GUARDAR FICHERO
            # -------------------------------------------------

            FICHERO.write_text(
                contenido,
                encoding="utf-8"
            )


            # -------------------------------------------------
            # MENSAJE
            # -------------------------------------------------

            st.success(
                "✅ Pleno al 15 guardado correctamente."
            )


            st.write(
                f"Fichero: `{FICHERO}`"
            )







import streamlit as st
from pathlib import Path
from utils.styles import aplicar_estilos
from datetime import datetime
from utils.datos.scrapea_la_web import scrapea_la_web
from utils.datos.desarrollo import *

aplicar_estilos()



equipos = []

if not equipos:
    jornada, resultados = scrapea_la_web()
    equipos = [partido["equipos"] for partido in resultados]
    equipos.pop()


        # Directorio del proyecto
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Fichero donde guardaremos la quiniela
    FICHERO_7 = BASE_DIR / "utils" / "datos" / "7_dobles.txt"
    FICHERO_8 = BASE_DIR / "utils" / "datos" / "8_dobles.txt"



        # ---------------------------------
    # LEER 7 DOBLES
    # ---------------------------------

    lineas = FICHERO_7.read_text(
        encoding="utf-8"
    ).splitlines()

    fecha_7_dobles = lineas[0].strip()

    apuestas_7 = {}

    for linea in lineas[1:]:

        partes = linea.split("|")

        if len(partes) != 2:
            continue

        partido = int(partes[0])
        pronostico = partes[1]

        apuestas_7[partido] = pronostico


    # ---------------------------------
    # LEER 8 DOBLES **********************
    # ---------------------------------

    lineas = FICHERO_8.read_text(
        encoding="utf-8"
    ).splitlines()

    fecha_8_dobles = lineas[0].strip()

    apuestas_8 = {}

    for linea in lineas[1:]:

        partes = linea.split("|")

        if len(partes) != 2:
            continue

        partido = int(partes[0])
        pronostico = partes[1]

        apuestas_8[partido] = pronostico













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
    font-weight: bold;">Introducir tu prediccion</h3>
    
    <p>
    Selecciona tu columna ganadora
    y luego observa cual sería los resultados obtenidos según la apuestas realizadas.
    </p>

    <p style="
    background-color: #d9f0ff;
    padding: 8px 15px;
    border-radius: 8px;
    display: inline-block;
    font-weight: bold;
    ">
    Indica la columna ganadora deseada.
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
        
        st.markdown(f"<div style=''><b>  {equipos[partido-1]}</b></div>", unsafe_allow_html=True)


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


columna_ganadora = "".join(
    "".join(seleccionados) if seleccionados else " "
    for seleccionados in pronosticos
)








# ---------------------------------------------------------
# COMPROBAR PRONÓSTICOS
# ---------------------------------------------------------

partidos_sin_pronostico = []

for numero, seleccionados in enumerate(pronosticos, start=1):

    cantidad = len(seleccionados)

    if cantidad == 1:
        simples += 1

    elif cantidad == 2:
        dobles += 1
        errores.append(
                    f"La columna ganadora solo puede tener simples. El partido {numero} tiene marcado un doble.")

    elif cantidad == 3:
        errores.append(
            f"La columna ganadora solo puede tener simples. El partido {numero} tiene marcado un triple.")
        triples += 1 
           

          
    elif cantidad == 0:
        partidos_sin_pronostico.append(str(numero))


if partidos_sin_pronostico:
    if len(partidos_sin_pronostico) == 1:
        errores.append(
            f"El partido {partidos_sin_pronostico[0]} "
            "no tiene ningún pronóstico."
        )
    else:
        errores.append(
            f"Los partidos {', '.join(partidos_sin_pronostico)} "
            "no tienen ningún pronóstico."
        )





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


esp1, col, esp2 = st.columns([2, 5, 2])

with col:

    st.markdown(
    """
    <div style="
        text-align: center;
        font-size: 14px;
        margin-top: 5px;
        font-weight: bold;
    ">
        ERRORES
        
    </div>
    """,
    unsafe_allow_html=True
    )





    if errores:
        for error in errores:
            st.markdown(
                f"""
                <div style="
                    background-color: #FCE4E4;
                    color: #8B2525;
                    text-align: center;
                    padding: 10px;
                    border-radius: 8px;
                    margin-bottom: 8px;
                ">
                    {error}
                </div>
                """,
                unsafe_allow_html=True
            )
    else:


        esp3, colin, esp4 = st.columns([2, 5, 2])

        with colin:

            
            st.markdown(
        """
        <div style="
            background-color: #D4EDDA;
            color: #155724;
            text-align: center;
            padding: 10px;
            border-radius: 8px;
            margin-bottom: 8px;
        ">
            No hay errores. La columna es correcta.
        </div>
        """,
        unsafe_allow_html=True
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



    st.write("")


    #****************************************************
    # ------------------DESARROLLO-----------------------
    #****************************************************


#columna_ganadora=
#st.write (columna_ganadora)





desarrollo_7=rellena_columnas_7(apuestas_7)
desarrollo_8=rellena_columnas_8(apuestas_8)




aciertos_7=contar_aciertos(columna_ganadora,desarrollo_7)
aciertos_8=contar_aciertos(columna_ganadora,desarrollo_8)

 

st.write("")
st.write("")
st.markdown(
    """
    <div style="
        text-align: center;
        font-size: 14px;
        margin-top: 5px;
        font-weight: bold;
    ">
        ACIERTOS CON LAS COLUMNAS DESARROLLADAS
        
    </div>
    """,
    unsafe_allow_html=True
    )

aciertos_7.reverse()
aciertos_8.reverse()

st.write("")



st.html("""
    <style>
    .tabla_aciertos7 th,
    .tabla_aciertos7 td {
        border: 1px solid #d9d9d9 !important;
        padding: 5px;
        text-align: center;
    }
    </style>
    """)



st.html("""
    <style>
    .tabla_aciertos8 th,
    .tabla_aciertos8 td {
        border: 1px solid #d9d9d9 !important;
        padding: 5px;
        text-align: center;
    }
    </style>
    """)





col_1, col_2, col_3 = st.columns([1,4,1])

with col_2:

        f_1,in_2, in_3, f_4 = st.columns([1,2,2,1])  

        with in_2:
            html_tabla = """
            <table class="tabla_aciertos7" style="border-collapse: collapse; text-align: center;margin:auto;">
                <tr>
                    <th style="border: 1px solid #d9d9d9; padding: 5px;background-color: #e6ccff; font-weight: bold;">Aciertos Q7</th>
                    <th style="border: 1px solid #d9d9d9; padding: 5px;background-color: #e6ccff; font-weight: bold;">Columnas</th>
                </tr>
            """

            for i, elemento in enumerate(aciertos_7):
                valor = 14 - i

                html_tabla += f"""
                <tr>
                    <td style="border: 1px solid #d9d9d9; padding: 5px;background-color: #D9EAF7;">{valor}</td>
                    <td style="border: 1px solid #d9d9d9; padding: 5px;;font-weight: bold;">{elemento}</td>
                </tr>
                """

            html_tabla += "</table>"

            st.html(html_tabla)
        
        with in_3:
            html_tabla = """
            <table class="tabla_aciertos8" style="border-collapse: collapse; text-align: center;margin:auto;">
                <tr>
                    <th style="border: 1px solid #d9d9d9; padding: 5px;background-color: #e6ccff; font-weight: bold;">Aciertos Q8</th>
                    <th style="border: 1px solid #d9d9d9; padding: 5px;background-color: #e6ccff; font-weight: bold;">Columnas</th>
                </tr>
            """

            for i, elemento in enumerate(aciertos_8):
                valor = 14 - i

                html_tabla += f"""
                <tr>
                    <td style="border: 1px solid #d9d9d9; padding: 5px;background-color: #D9EAF7;">{valor}</td>
                    <td style="border: 1px solid #d9d9d9; padding: 5px;font-weight: bold;">{elemento}</td>
                </tr>
                """

            html_tabla += "</table>"

            st.html(html_tabla)
        






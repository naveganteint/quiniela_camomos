import streamlit as st
from pathlib import Path
from utils.styles import aplicar_estilos
from datetime import datetime
from utils.datos.scrapea_la_web import scrapea_la_web
from utils.datos.desarrollo import *
import pandas as pd


aplicar_estilos()

# ---------------------------------------------------------
# CONFIGURACIÓN
# ---------------------------------------------------------



# Directorio del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Fichero donde guardaremos la quiniela
FICHERO_7 = BASE_DIR / "utils" / "datos" / "7_dobles.txt"
FICHERO_8 = BASE_DIR / "utils" / "datos" / "8_dobles.txt"
FICHERO_15 = BASE_DIR / "utils" / "datos" / "pleno_15.txt"



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
    font-weight: bold;">Comprobar la Quiniela</h3>
    
    <p>
    Suerte a los camomos y compañia!!!. Firmado La Cúpula.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)



jornada, resultados = scrapea_la_web()







df_resultados = pd.DataFrame(resultados)


# ---------------------------------
# GUARDAR PLENO AL 15
# ---------------------------------

pleno_15 = df_resultados[
    df_resultados["partido"] == 15
].to_dict("records")


# ---------------------------------
# ELIMINAR PLENO AL 15
# ---------------------------------

df_resultados = df_resultados[
    df_resultados["partido"] != 15
].copy()


# CREAR TABLA COMPARATIVA DEL RESULTADO***************************************************************


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
# AÑADIR 7 DOBLES
# ---------------------------------

df_resultados["7_dobles"] = (
    df_resultados["partido"]
    .map(apuestas_7)
    .fillna("")
)





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


# ---------------------------------
# AÑADIR 8 DOBLES
# ---------------------------------

df_resultados["8_dobles"] = (
    df_resultados["partido"]
    .map(apuestas_8)
    .fillna("")
)



# ---------------------------------
# Acertado 7 DOBLES
# ---------------------------------

df_resultados["Acertado 7 dobles"] = df_resultados.apply(
    lambda fila:
        "-"
        if not fila["signo"]
        else (
            "Si"
            if fila["signo"] in fila["7_dobles"]
            else "No"
        ),
    axis=1
)

aciertos_7_dobles = (
    df_resultados["Acertado 7 dobles"] == "Si"
).sum()

# ---------------------------------
# Acertado 8 DOBLES
# ---------------------------------

df_resultados["Acertado 8 dobles"] = df_resultados.apply(
    lambda fila:
        "-"
        if not fila["signo"]
        else (
            "Si"
            if fila["signo"] in fila["8_dobles"]
            else "No"
        ),
    axis=1
)

aciertos_8_dobles = (
    df_resultados["Acertado 8 dobles"] == "Si"
).sum()

# ---------------------------------
# Partidos por finalizar
# ---------------------------------

partidos_finalizados = (
    df_resultados["estado"] == "Finalizado"
).sum()

partidos_pendientes = 14 - partidos_finalizados



st.markdown(
    f"""
    <div style="text-align: center;">

    <p style="
    background-color: white;
    padding: 8px 15px;
    border-radius: 8px;
    display: inline-block;
    font-weight: bold;
    font-size: 20px"
    >
    Jornada:&nbsp;&nbsp;&nbsp;&nbsp; &nbsp; {jornada}
    </p>

    </div>
    """,
    unsafe_allow_html=True
)




col_1, col_2, col_3 = st.columns([1,4,1])

with col_2:

    col_7, col_8 = st.columns(2)

    with col_7:

        st.markdown(
            f"""
                <div style="background-color: #d9f0ff;
                padding: 15px;
                border-radius: 10px;
                ">
                
                
                
                
                <div style="
                font-weight: bold;
                font-size: 18px;
                margin-bottom: 10px;
                text-align: center;
                ">
                Quiniela 7 dobles
                </div>

                
                <div style="margin-bottom: 8px;text-align: center; font-size: 20px; ">
                Fecha Introducción:
                <span style="
                    background-color: #fff2a8;
                    padding: 3px 6px;
                    border-radius: 5px;
                ">{fecha_7_dobles}</span>
                </div>

                
                <div style="
                    margin-bottom: 8px;text-align: center; font-size: 20px;
                ">
                    Partidos por finalizar:
                    <span style="
                        background-color: #fff2a8;
                        padding: 3px 6px;
                        border-radius: 5px;
                        font-weight: bold;
                    ">
                        {partidos_pendientes}
                    </span>
                </div>
             

                <div style="font-size: 18px;text-align: center; font-size: 20px;">
                Aciertos:
                <span style="
                    background-color: #fff2a8;
                    padding: 3px 6px;
                    border-radius: 5px;
                    font-weight: bold;
                ">{aciertos_7_dobles}</span>
                </div>

            """,
            unsafe_allow_html=True
        )




   

    with col_8:
        st.markdown(
            f"""
                <div style="background-color: #ffe0e0;
                padding: 15px;
                border-radius: 10px;
                ">
                
                
                
                
                <div style="
                font-weight: bold;
                font-size: 18px;
                margin-bottom: 10px;
                text-align: center;
                ">
                Quiniela 8 dobles
                </div>

                
                <div style="margin-bottom: 8px;text-align: center; font-size: 20px; ">
                Fecha Introducción:
                <span style="
                    background-color: #fff2a8;
                    padding: 3px 6px;
                    border-radius: 5px;
                ">{fecha_8_dobles}</span>
                </div>

                
                <div style="
                    margin-bottom: 8px;text-align: center; font-size: 20px;
                ">
                    Partidos por finalizar:
                    <span style="
                        background-color: #fff2a8;
                        padding: 3px 6px;
                        border-radius: 5px;
                        font-weight: bold;
                    ">
                        {partidos_pendientes}
                    </span>
                </div>
             

                <div style="font-size: 18px;text-align: center; font-size: 20px;">
                Aciertos:
                <span style="
                    background-color: #fff2a8;
                    padding: 3px 6px;
                    border-radius: 5px;
                    font-weight: bold;
                ">{aciertos_8_dobles}</span>
                </div>

            """,
            unsafe_allow_html=True
        )



    #--------------------------------
    # CONSTRUIR TABLAS DE RESULTADOS
    #-----------------------------------

    df_resultados = df_resultados.rename(
        columns={
            "estado": "Situacion",
            "signo": "Signo",
            "goles": "Goles",
            "partido": "Nº",
            "equipos": "Equipos",
            "7_dobles": "Q7",
            "8_dobles": "Q8",
            "Acertado 7 dobles": "Ac_Q7",
            "Acertado 8 dobles": "Ac_Q8",
        }
    )   





    df_resultados[""] = ""
    df_resultados[" "] = ""

    df_resultados = df_resultados[
    [
        "Nº",
        "Equipos",
        "Goles",
        "Signo",

        "",
        "Q7",
        "Ac_Q7",
        " ",
        "Q8",
        "Ac_Q8",
        "Situacion"
        
        
    ]
    ]

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
        COLUMNAS
        
    </div>
    """,
    unsafe_allow_html=True
)





    st.write("")

    html_tabla = f""" 
    
    <style>
        table, tr, th, td {{
            border: none !important;
        }}



        td {{
            border-bottom: 2px solid #d9d9d9 !important;
        }}


    </style>

    



    <table style=" 
        width: auto; 
        margin: 0 auto; 
        text-align: center; 
        border-collapse: collapse; 
        border: none;
    "> 
    <tr> 
        <th style="background-color: #e6ccff; font-weight: bold;width: 45px;">  {df_resultados.columns[0]}</th> 
        <th style="background-color: #e6ccff; font-weight: bold;">{df_resultados.columns[1]}</th> 
        <th style="background-color: #e6ccff; font-weight: bold;width: 65px;">{df_resultados.columns[2]}</th> 
        <th style="background-color: #e6ccff; font-weight: bold;width: 65px;">{df_resultados.columns[3]}</th> 
        <th style="background-color: #e6ccff; font-weight: bold;width: 45px">{df_resultados.columns[5]}</th>
        <th style="background-color: #e6ccff; font-weight: bold;width: 45px;">{df_resultados.columns[8]}</th> 
        <th style="background-color: #e6ccff; font-weight: bold;">{df_resultados.columns[10]}</th> 

    </tr> 
    
    """

    for _, fila in df_resultados.iterrows():
        if _ % 2 == 0:
         html_tabla += '<tr style="background-color: #f2faff;">'
        else:
         html_tabla += '<tr style="background-color: white;">'  




        html_tabla += f"<td style=''>{fila['Nº']}</td>"
        html_tabla += f"<td style='text-align: left;'>{fila['Equipos']}</td>"
        html_tabla += f"<td>{fila['Goles']}</td>"
        html_tabla += f"<td>{fila['Signo']}</td>"
    
        
        #******q7
        
        if fila["Ac_Q7"] == "Si":
            html_tabla += f"<td style=' color: #008000; font-weight: bold;'>{fila['Q7']}</td>"

        elif fila["Ac_Q7"] == "No":
            html_tabla += f"<td style=' color: #c00000; '>{fila['Q7']}</td>"
        else:
            html_tabla += f"<td>{fila['Q7']}</td>"
        


   
        
        
        #******q8
        if fila["Ac_Q8"] == "Si":
            html_tabla += f"<td style=' color: #008000; font-weight: bold;'>{fila['Q8']}</td>"

        elif fila["Ac_Q8"] == "No":
            html_tabla += f"<td style=' color: #c00000; '>{fila['Q8']}</td>"
        else:
            html_tabla += f"<td>{fila['Q8']}</td>"



        
 
        html_tabla += f"<td>{fila['Situacion']}</td>"
        
        
        
        html_tabla += "</tr>"




    html_tabla += "</table>"

    st.markdown(
    html_tabla,
    unsafe_allow_html=True
)

#------------------------
#********fuente de datos
#-----------------------
st.markdown(
    """
    <div style="
        text-align: center;
        font-size: 12px;
        margin-top: 5px;
    ">
        *Datos tomados de la web:
        <a href="https://www.quiniela15.com/resultados-quiniela" target="_blank">
            quiniela15.com
        </a>
    </div>
    """,
    unsafe_allow_html=True
)



#-----------------------------------------
#                PLENO AL 15
#--------------------------------------

st.write("")
st.write("")
st.write("")

col_1, col_2, col_3 = st.columns([1,4,1])

with col_2:

    lineas_15 = FICHERO_15.read_text(
        encoding="utf-8"
    ).splitlines()

    pronostico_pleno_15 = f"{lineas_15[-2][-1]}-{lineas_15[-1][-1]}"


    st.markdown(
    """
    <div style="
        text-align: center;
        font-size: 14px;
        margin-top: 5px;
        font-weight: bold;
    ">
        PLENO AL 15
        
    </div>
    """,
    unsafe_allow_html=True
)


    html_tabla = f""" <table style="margin: 0 auto; border-collapse: collapse; text-align: center;">
        <tr>
         <td colspan="5" style="height: 8px; border-bottom: 2px solid #d9d9d9;"></td>
           </tr> <tr> 
           <td style="width: 45px;">15</td>
            <td>{pleno_15[0]["equipos"]}</td>
            <td style="width: 65px;">{pleno_15[0]["goles"]}</td> """
    if pronostico_pleno_15 == pleno_15[0]["goles"]:
         html_tabla += f"<td style='color: #008000; font-weight: bold; width: 65px;'>{pronostico_pleno_15}</td>"
    else: html_tabla += f"<td style='color: #c00000; font-weight: bold; width: 65px;'>{pronostico_pleno_15}</td>"
    html_tabla += f""" <td>{pleno_15[0]["estado"]}</td>
      </tr>
     </table> """ 
    
    st.markdown(html_tabla, unsafe_allow_html=True)

     
    st.write("")


    #****************************************************
    # ------------------DESARROLLO-----------------------
    #****************************************************


    #columna_ganadora=
    columna_ganadora = [partido["signo"] for partido in resultados[:-1]]



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
        






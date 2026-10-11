import requests
from bs4 import BeautifulSoup
import re


URL = "https://www.quiniela15.com/resultados-quiniela"


def scrapea_la_web():

    respuesta = requests.get(
        URL,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=10
    )

    respuesta.raise_for_status()

    soup = BeautifulSoup(
        respuesta.text,
        "html.parser"
    )

    # ---------------------------------
    # BUSCAR LA JORNADA
    # ---------------------------------

    jornada = None

    texto_pagina = soup.get_text(
        " ",
        strip=True
    )

    coincidencia_jornada = re.search(
        r"Jornada\s+(\d+)",
        texto_pagina,
        re.IGNORECASE
    )

    if coincidencia_jornada:

        jornada = int(
            coincidencia_jornada.group(1)
        )

    # ---------------------------------
    # BUSCAR LOS PARTIDOS
    # ---------------------------------

    resultados = []

    filas = soup.find_all("tr")

    for fila in filas:

        columnas = fila.find_all("td")

        if len(columnas) < 3:
            continue

        textos = [
            columna.get_text(
                " ",
                strip=True
            )
            for columna in columnas
        ]

        #print("TEXTOS COMPLETOS:", textos)

        # ---------------------------------
        # NÚMERO DEL PARTIDO
        # ---------------------------------

        numero_texto = textos[0].strip()

        if not numero_texto.isdigit():
            continue

        numero = int(numero_texto)

        if numero < 1 or numero > 15:
            continue

        # ---------------------------------
        # EQUIPOS
        # ---------------------------------

        equipos = textos[1].strip()

        if not equipos:
            continue

        # Quitamos las puntuaciones
        # que aparecen entre paréntesis

        equipos = re.sub(
            r"\s*\(\d+(?:\.\d+)?\)",
            "",
            equipos
        )

        equipos = re.sub(
            r"\s+",
            " ",
            equipos
        ).strip()

        # ---------------------------------
        # INFORMACIÓN DEL RESULTADO
        # ---------------------------------

        informacion = textos[2].strip()

        goles = ""
        signo = ""
        estado = ""

        # ---------------------------------
        # BUSCAR GOLES
        # ---------------------------------

        coincidencia_goles = re.search(
            r"(\d+)\s*-\s*(\d+)",
            informacion
        )

        if coincidencia_goles:

            goles_local = int(
                coincidencia_goles.group(1)
            )

            goles_visitante = int(
                coincidencia_goles.group(2)
            )

            goles = (
                f"{goles_local}-{goles_visitante}"
            )

            # ---------------------------------
            # CALCULAR SIGNO
            # ---------------------------------

            if goles_local > goles_visitante:

                signo = "1"

            elif goles_local < goles_visitante:

                signo = "2"

            else:

                signo = "X"

            # ---------------------------------
            # COMPROBAR MINUTO
            # ---------------------------------



            if len(textos) > 3 and textos[3]:
                estado = textos[3]

                if estado in ("1", "X", "2"):
                    estado = "Finalizado"
            else:
                estado = "Finalizado"


                
        # ---------------------------------
        # PARTIDO SUSPENDIDO
        # ---------------------------------

        elif "Suspendido" in informacion:

            estado = "Suspendido"

        # ---------------------------------
        # PARTIDO PENDIENTE
        # ---------------------------------

        else:

            estado = informacion

        # ---------------------------------
        # GUARDAR RESULTADO
        # ---------------------------------

        resultados.append({
            "partido": numero,
            "equipos": equipos,
            "goles": goles,
            "signo": signo,
            "estado": estado
        })

    # ---------------------------------
    # ORDENAR
    # ---------------------------------

    resultados.sort(
        key=lambda x: x["partido"]
    )

    # ---------------------------------
    # ELIMINAR DUPLICADOS
    # ---------------------------------

    resultados_unicos = []

    partidos_vistos = set()

    for resultado in resultados:

        numero = resultado["partido"]

        if numero in partidos_vistos:
            continue

        partidos_vistos.add(numero)

        resultados_unicos.append(
            resultado
        )

    # ---------------------------------
    # RETURN
    # ---------------------------------

    return jornada, resultados_unicos
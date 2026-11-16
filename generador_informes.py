
import json
from datetime import datetime
from pathlib import Path


RUTA_INFORMES = Path(__file__).parent / "reports"
ARCHIVO_JSON = RUTA_INFORMES / "informe_web.json"


def contabilizador(tests):

    resultados = []

    for test in tests:

        try:
            resultado = test()

            # Cada prueba devuelve un diccionario
            estado = resultado["estado"]
            url = resultado["url"]
            descripcion = resultado["descripcion"]

            if estado not in ("PASS", "FAIL", "ERROR", "SKIPPED"):
                estado = "ERROR"
                descripcion = "Resultado inesperado"

        except Exception as e:
            estado = "ERROR"
            url = "Desconocida"
            descripcion = str(e)

        resultados.append({
            "test": test.__name__,
            "fecha": datetime.now().isoformat(timespec="seconds"),
            "url": url,
            "resultado": estado,
            "descripcion": descripcion
        })

    # Contabilizar resultados
    contador = {
        "PASS": 0,
        "FAIL": 0,
        "ERROR": 0,
        "SKIPPED": 0
    }

    for resultado in resultados:
        contador[resultado["resultado"]] += 1

    total = sum(contador.values())
    ejecutados = total - contador["SKIPPED"]

    porcentaje = (
        contador["PASS"] / ejecutados * 100
        if ejecutados > 0 else 0
    )

    resumen = {
        "total": total,
        **contador,
        "porcentaje_exito": round(porcentaje, 2)
    }

    # Preparar informe
    informe = {
        "fecha_ejecucion": datetime.now().isoformat(timespec="seconds"),
        "resumen": resumen,
        "resultados": resultados
    }

    # Crear carpeta si no existe
    RUTA_INFORMES.mkdir(parents=True, exist_ok=True)

    # Leer informes anteriores
    if ARCHIVO_JSON.exists():
        with open(ARCHIVO_JSON, "r", encoding="utf-8") as archivo:
            informes = json.load(archivo)
    else:
        informes = []

    # Añadir nueva ejecución
    informes.append(informe)

    # Guardar archivo JSON
    with open(ARCHIVO_JSON, "w", encoding="utf-8") as archivo:
        json.dump(informes, archivo, indent=4, ensure_ascii=False)

    print("Informe generado correctamente")
    print(resumen)

    return resumen

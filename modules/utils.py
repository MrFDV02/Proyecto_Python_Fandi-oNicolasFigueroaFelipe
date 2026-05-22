import time
import json
import os

def borrar_pantalla():
    os.system("clear")

def pausar_pantalla():
    input("Presione Enter para continuar...")

RUTA_JSON = os.path.join(os.path.dirname(__file__), "..", "data", "agenda.json")

def cargar_datos():
    with open(RUTA_JSON, "r") as ca:
        datos = json.load(ca)
    return datos

def guardar_datos(datos):
    with open(RUTA_JSON, "w") as gu:
        json.dump(datos, gu, indent=4)
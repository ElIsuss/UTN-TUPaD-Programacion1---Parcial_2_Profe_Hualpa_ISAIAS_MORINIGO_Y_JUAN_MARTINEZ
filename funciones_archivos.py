import os
import csv


# UTILIDADES DE ARCHIVOS
def construir_ruta(n1, n2, n3):
    return os.path.join("datos", n1, n2, n3)

def guardar_item_en_csv(ruta, item):
    os.makedirs(ruta, exist_ok=True)
    archivo = os.path.join(ruta, "items.csv")
    try:
        existe = os.path.exists(archivo)
        with open(archivo, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=item.keys())
            if not existe:
                writer.writeheader()
            writer.writerow(item)
    except Exception as e:
        print(f"Error al guardar: {e}")

def sobrescribir_csv(ruta, items):
    try:
        if not items:
            fieldnames = ["id", "nombre", "nivel1", "nivel2", "nivel3", "poblacion", "superficie"]
        else:
            fieldnames = items[0].keys()

        with open(ruta, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(items)
    except Exception as e:
        print(f"Error al sobrescribir: {e}")


# FUNCIÓN RECURSIVA
def leer_todos_los_items(ruta_actual="datos", items_totales=None):
    if items_totales is None:
        items_totales = []

    csv_path = os.path.join(ruta_actual, "items.csv")
    if os.path.isfile(csv_path):
        try:
            with open(csv_path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for fila in reader:
                    ubicacion_relativa = ruta_actual.replace("datos" + os.sep, "")
                    fila["ubicacion"] = ubicacion_relativa
                    items_totales.append(fila)
        except Exception as e:
            print(f"Error al leer {csv_path}: {e}")

    if os.path.isdir(ruta_actual):
        try:
            for nombre in os.listdir(ruta_actual):
                ruta_hija = os.path.join(ruta_actual, nombre)
                if os.path.isdir(ruta_hija):
                    leer_todos_los_items(ruta_hija, items_totales)
        except Exception as e:
            print(f"Error al acceder al directorio {ruta_actual}: {e}")

    return items_totales

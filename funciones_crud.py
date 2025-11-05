import uuid
import os
import csv
import funciones_archivos  # type: ignore

# Jerarquía global
NIVEL_JERARQUICO = ("Continente", "País", "Ciudad")

# VALIDACIONES
def validar_texto_no_vacio(texto, nombre_campo):
    if not texto.strip():
        print(f"Error: El campo {nombre_campo} no puede estar vacío.")
        return None
    return texto.strip().capitalize()

def validar_entero_positivo(valor, nombre_campo):
    try:
        valor = int(valor)
        if valor <= 0:
            print(f"Error: {nombre_campo} debe ser mayor a cero.")
            return None
        return valor
    except ValueError:
        print(f"Error: {nombre_campo} debe ser un número entero.")
        return None

def validar_flotante_positivo(valor, nombre_campo):
    try:
        valor = float(valor)
        if valor <= 0:
            print(f"Error: {nombre_campo} debe ser mayor a cero.")
            return None
        return valor
    except ValueError:
        print(f"Error: {nombre_campo} debe ser un número decimal.")
        return None

# CRUD
def crear_registro():
    print("\n--- Crear nuevo registro ---")
    nombre_str = input("Nombre del Ítem: ")
    n1_str = input(f"{NIVEL_JERARQUICO[0]}: ")
    n2_str = input(f"{NIVEL_JERARQUICO[1]}: ")
    n3_str = input(f"{NIVEL_JERARQUICO[2]}: ")
    poblacion_str = input("Población: ")
    superficie_str = input("Superficie: ")

    nombre = validar_texto_no_vacio(nombre_str, "Nombre")
    n1 = validar_texto_no_vacio(n1_str, NIVEL_JERARQUICO[0])
    n2 = validar_texto_no_vacio(n2_str, NIVEL_JERARQUICO[1])
    n3 = validar_texto_no_vacio(n3_str, NIVEL_JERARQUICO[2])
    poblacion = validar_entero_positivo(poblacion_str, "Población")
    superficie = validar_flotante_positivo(superficie_str, "Superficie")

    if None in [nombre, n1, n2, n3, poblacion, superficie]:
        print("Registro cancelado por datos inválidos.")
        return

    item = {
        "id": uuid.uuid4().hex[:8],
        "nombre": nombre,
        "nivel1": n1,
        "nivel2": n2,
        "nivel3": n3,
        "poblacion": str(poblacion),
        "superficie": str(superficie)
    }

    ruta = funciones_archivos.construir_ruta(n1, n2, n3)
    funciones_archivos.guardar_item_en_csv(ruta, item)
    print("Éxito: Registro creado.")


def listar_registros():
    print("\n--- Listado de registros ---")
    lista = funciones_archivos.leer_todos_los_items()
    if not lista:
        print("No hay registros.")
        return

    print(f"{NIVEL_JERARQUICO[0]}/{NIVEL_JERARQUICO[1]}/{NIVEL_JERARQUICO[2]}")
    print("-" * 40)
    for r in lista:
        print(f"ID: {r['id']} | {r['nombre']} ({r['nivel1']}/{r['nivel2']}/{r['nivel3']}) | Población: {r['poblacion']} | Superficie: {r['superficie']}")
    print(f"\nTotal: {len(lista)} registros.")


def buscar_por_id(id_buscado):
    id_buscado = id_buscado.strip().lower()
    lista = funciones_archivos.leer_todos_los_items()
    for r in lista:
        if r["id"].lower().startswith(id_buscado):
            return r
    return None


def modificar_registro():
    print("\n--- Modificar registro ---")
    id_buscado = input("ID (o inicio de ID) a modificar: ").strip()
    objetivo = buscar_por_id(id_buscado)
    if not objetivo:
        print("Error: Registro no encontrado.")
        return

    print(f"Modificando: {objetivo['nombre']} (ID: {objetivo['id']})")

    campo = input("Campo a modificar (nombre, poblacion, superficie): ").strip().lower()
    nuevo = input(f"Nuevo valor para {campo}: ").strip()

    valor = None
    if campo == "nombre":
        valor = validar_texto_no_vacio(nuevo, "Nombre")
    elif campo == "poblacion":
        valor = validar_entero_positivo(nuevo, "Población")
    elif campo == "superficie":
        valor = validar_flotante_positivo(nuevo, "Superficie")
    else:
        print("Error: Campo inválido o no editable.")
        return

    if valor is None:
        return

    objetivo[campo] = str(valor)
    ruta_csv = os.path.join("datos", objetivo["ubicacion"], "items.csv")

    try:
        with open(ruta_csv, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for i, r in enumerate(items):
            if r["id"] == objetivo["id"]:
                items[i] = objetivo
                break

        funciones_archivos.sobrescribir_csv(ruta_csv, items)
        print("Éxito: Modificado.")

    except Exception as e:
        print(f"Error al modificar: {e}")


def eliminar_registro():
    print("\n--- Eliminar registro ---")
    id_buscado = input("ID (o inicio de ID) a eliminar: ").strip()
    objetivo = buscar_por_id(id_buscado)
    if not objetivo:
        print("Error: Registro no encontrado.")
        return

    confirmar = input(f"¿Eliminar '{objetivo['nombre']}' ({objetivo['id']})? (s/n): ").strip().lower()
    if confirmar != "s":
        print("Operación cancelada.")
        return

    ruta_csv = os.path.join("datos", objetivo["ubicacion"], "items.csv")
    try:
        with open(ruta_csv, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            items = [r for r in reader if r["id"] != objetivo["id"]]
        funciones_archivos.sobrescribir_csv(ruta_csv, items)
        print("Éxito: Eliminado.")
    except Exception as e:
        print(f"Error al eliminar: {e}")


def estadisticas():
    print("\n--- Estadísticas ---")
    lista = funciones_archivos.leer_todos_los_items()
    if not lista:
        print("No hay datos.")
        return

    total = len(lista)
    try:
        suma_poblacion = sum(int(r["poblacion"]) for r in lista)
        suma_superficie = sum(float(r["superficie"]) for r in lista)
        promedio_superficie = suma_superficie / total if total > 0 else 0
    except ValueError:
        print("Error: Algunos campos numéricos tienen formato inválido.")
        return

    conteo_nivel1 = {}
    for r in lista:
        clave = r["nivel1"]
        conteo_nivel1[clave] = conteo_nivel1.get(clave, 0) + 1

    print(f"Total ítems: {total}")
    print(f"Suma población: {suma_poblacion}")
    print(f"Promedio superficie: {promedio_superficie:.2f}")
    print(f"\nCantidad por {NIVEL_JERARQUICO[0]}:")
    for k, v in conteo_nivel1.items():
        print(f"  {k}: {v}")


def ordenar():
    print("\n--- Ordenar registros ---")
    lista = funciones_archivos.leer_todos_los_items()
    if not lista:
        print("No hay datos.")
        return

    campo = input("Campo para ordenar (nombre, poblacion, superficie): ").strip().lower()
    if campo not in ["nombre", "poblacion", "superficie"]:
        print("Error: Campo inválido.")
        return

    try:
        if campo == "nombre":
            lista.sort(key=lambda x: x.get(campo, "").lower())
        else:
            lista.sort(key=lambda x: float(x.get(campo) or 0))

        print("\n--- Resultado Ordenado ---")
        for r in lista:
            print(f"Nombre: {r['nombre']:<20} | {r['poblacion']:<10} | {r['superficie']:<10} | Ubicación: {r['ubicacion']}")

    except Exception as e:
        print(f"Error al ordenar: {e}")

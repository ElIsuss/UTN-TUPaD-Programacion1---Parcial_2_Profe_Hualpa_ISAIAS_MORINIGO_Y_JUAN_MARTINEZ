import os
import funciones_crud  # type: ignore

def main():
    while True:
        print("\n" + "="*45)
        print("   GESTOR JERÁRQUICO DE REGISTROS   ")
        print(f"Jerarquía: {funciones_crud.NIVEL_JERARQUICO[0]} / {funciones_crud.NIVEL_JERARQUICO[1]} / {funciones_crud.NIVEL_JERARQUICO[2]}")
        print("="*45)
        print("1) Crear nuevo registro")
        print("2) Listar todos los registros")
        print("3) Modificar registro (por ID)")
        print("4) Eliminar registro (por ID)")
        print("-" * 45)
        print("5) Estadísticas globales")
        print("6) Ordenar registros")
        print("0) Salir")
        print("="*45)

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                funciones_crud.crear_registro()
            elif opcion == 2:
                funciones_crud.listar_registros()
            elif opcion == 3:
                funciones_crud.modificar_registro()
            elif opcion == 4:
                funciones_crud.eliminar_registro()
            elif opcion == 5:
                funciones_crud.estadisticas()
            elif opcion == 6:
                funciones_crud.ordenar()
            elif opcion == 0:
                print("Saliendo del programa. ¡Hasta pronto!")
                break
            elif opcion > 6:
                print("Por favor, elija una opción válida del menú.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    try:
        os.makedirs("datos", exist_ok=True)
        print("Carpeta 'datos/' asegurada.")
        main()
    except KeyboardInterrupt:
        print("\nOperación interrumpida por el usuario.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

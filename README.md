# UTN-TUPaD-Programacion1---Parcial_2_Profe_Hualpa_ISAIAS_MORINIGO_Y_JUAN_MARTINEZ

INTEGRANTES: ISAIAS MORINIGO Y JUAN MARTINEZ


 Gestor Jerárquico de Registros

Este proyecto consiste en un sistema de gestión jerárquica desarrollado en Python. Su objetivo es almacenar, organizar y filtrar información dentro de una estructura de carpetas que representa tres niveles jerárquicos: Continente → País → Ciudad. Cada nivel se crea automáticamente en el sistema de archivos y dentro de la última carpeta se genera un archivo CSV que contiene los ítems correspondientes.

La estructura de datos se basa en diccionarios, donde cada registro posee un identificador único, nombre, continente, país, ciudad, población y superficie. Todos los datos se guardan en formato CSV, permitiendo un acceso directo y transparente a la información sin necesidad de una base de datos externa.

La lógica principal del programa se apoya en una función recursiva encargada de recorrer toda la jerarquía de carpetas, leer los archivos CSV existentes y consolidar la información en una lista global de registros. Gracias a esta implementación, el sistema puede acceder a todos los datos de manera dinámica, sin importar cuántos niveles o carpetas existan dentro del directorio raíz.

El programa cuenta con distintas funcionalidades accesibles desde un menú principal. Entre ellas se incluyen: crear nuevos registros, listar la información completa, modificar datos existentes, eliminar registros, generar estadísticas generales y ordenar la información según distintos criterios como nombre, población o superficie. Además, existe un módulo dedicado al filtrado, que permite mostrar los datos por continente, por cantidad de habitantes o por superficie, facilitando el análisis de la información almacenada.

La estructura del proyecto se organiza en varios archivos para mantener una división clara de responsabilidades: el archivo principal (main.py) contiene el menú general y coordina las acciones; el módulo de funciones CRUD gestiona la creación, lectura, modificación y eliminación de los registros; el módulo de archivos maneja la lógica de guardado y lectura desde el sistema de directorios; y el módulo de filtrado aplica las diferentes condiciones de búsqueda.

El funcionamiento general es el siguiente → el usuario interactúa con el menú principal → el programa redirige la acción al módulo correspondiente → las funciones acceden a los archivos del sistema para leer o modificar la información → y finalmente muestran los resultados por pantalla.

En resumen, este proyecto implementa un modelo de gestión de datos que combina una estructura jerárquica real del sistema operativo con la simplicidad de manejo de archivos CSV. Permite comprender conceptos de programación modular, recursividad, persistencia de datos y filtrado de información, aplicados en un entorno práctico y organizado.

VIDEO EXPLICATIVO DEL PROGRAMA: https://www.youtube.com/watch?v=rqbxF8iN2aw

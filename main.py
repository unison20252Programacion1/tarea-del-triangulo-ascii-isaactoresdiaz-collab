# Completa las validaciones y llama a la función

import sys
from solucion import [NOMBRE_DE_LA_FUNCION]
from solucion import triangulo_simetrico


def main():
    """
    data: lista de líneas leídas desde la entrada estándar o ingresadas por el usuario
          donde cada elemento de la lista es un string    
    """
    # IF que permite leer desde la entrada estándar o pedir datos al usuario
    if sys.stdin.isatty():
        data = []
        data.append(input("Ingresa la altura: ").strip())
        data.append(input("Ingresa el caracter: "))
    else:
        data = sys.stdin.read().strip().splitlines()

    # Validar que se recibieron dos líneas
    # Validar que se recibieron dos líneas"Error: La altura debe ser un numero entero""Error: La altura debe ser un numero entero"
    if len(data) < 2:
        print("Error: Se esperan 2 lineas de entrada (altura, caracter)")
        return
@@ -28,12 +29,14 @@ def main():
    # Intentar convertir la altura a entero
    try:
        # TODO: Convertir m_str a entero y asignarlo a m
        m = int(m_str)  

    except ValueError:
        # TODO: imprimir "Error: La altura debe ser un numero entero" y salir
        print("Error: La altura debe ser un numero entero")

    # TODO: llamar a la función triangulo_simetrico con los parámetros m y s
    triangulo_simetrico(m, s)

if _name_ == "_main_":
    main()
    main()

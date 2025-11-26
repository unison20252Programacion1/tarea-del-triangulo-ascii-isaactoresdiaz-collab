# Completa las validaciones y llama a la función
import sys
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
    if len(data) < 2:
        print("Error: Se esperan 2 lineas de entrada (altura, caracter)")
        return

    m_str = data[0].strip()  # primera linea: altura (texto)
    s = data[1]              # segunda línea: caracter

    # intentar convertir la altura a entero
    try:
        m = int(m_str)
    except ValueError:
        print("Error: La altura debe ser un numero entero")
        return   # <-- IMPORTANTE: salir

    # llamar a la función triangulo_simetrico
    triangulo_simetrico(m, s)


if __name__ == "_main_":
    main()

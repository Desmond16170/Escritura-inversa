def invertir_palabras(cadena):
    """
    Invierte cada palabra en una cadena y devuelve la cadena invertida.

    Parameters:
    - cadena (str): Cadena de palabras a invertir.

    Returns:
    - str: Cadena invertida.
    """
    palabras = cadena.split()
    palabras_invertidas = [palabra[::-1] for palabra in palabras]
    return ' '.join(palabras_invertidas)


def procesar_archivo(archivo_entrada):
    """
    Procesa un archivo de entrada que contiene oraciones,
    invierte las palabras y muestra las oraciones invertidas.

    Parameters:
    - archivo_entrada (str): Nombre del archivo de entrada.

    Returns:
    - None
    """
    with open(archivo_entrada, 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            cadena_invertida = invertir_palabras(linea.lower().strip())
            print(cadena_invertida)


def encontrar_cadena_oracion(oraciones, cadena):
    """
    Busca si una cadena dada puede formarse
    con los caracteres de alguna oración invertida.

    Parameters:
    - oraciones (list): Lista de oraciones invertidas.
    - cadena (str): Cadena de caracteres a buscar.

    Returns:
    - str or None: La oración con los caracteres de la cadena,
    en mayúscula, o None si no se encuentra.
    """
    caracteres_cadena = set(char for char in cadena)
    for oracion in oraciones:
        caracteres_oracion = set(char for char in ''.join(oracion.split()))
        # Verifica si la oración contiene todos los caracteres de la cadena
        if caracteres_cadena.issubset(caracteres_oracion):
            # Formatea la oración con mayúsculas
            # para los caracteres de la cadena
            oracion_formateada = ''.join([char.upper()
                                          if char in caracteres_cadena
                                          else char.lower()
                                          for char in oracion])
            print(f"La cadena \"{cadena}\" puede")
            print(" formarsa partir de la oración:")
            print(oracion_formateada)
            return oracion_formateada
    print(f"No se encontró ninguna oración que pueda formarse \"{cadena}\".")
    return None


if __name__ == "__main__":
    archivo_entrada = "entrada.txt"

    # Muestra las oraciones invertidas
    procesar_archivo(archivo_entrada)

    # Solicita al usuario ingresar una cadena
    cadena_usuario = input("Ingrese una cadena: ").lower().replace(" ", "")

    # Procesa las oraciones invertidas
    oraciones_procesadas = [invertir_palabras(linea.lower().strip())
                            for linea in open(
                                archivo_entrada, 'r').readlines()]

    # Busca si la cadena se puede formar con alguna oración
    oracion_encontrada = encontrar_cadena_oracion(
        oraciones_procesadas, cadena_usuario)

    if oracion_encontrada:
        print("La cadena se puede formar con los caracteres"
              "de la siguiente oración:")
        print(oracion_encontrada)
    else:
        print("Error: No se encontró ninguna oración"
              "que pueda formarse con los caracteres ingresados.")

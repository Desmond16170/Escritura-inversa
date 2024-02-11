# Invertir Palabras y Buscar Cadena en Oraciones

Este programa en Python procesa múltiples cadenas de caracteres o oraciones para encontrar su versión invertida, donde cada palabra se invierte. Además, permite al usuario ingresar una cadena para buscar si se puede formar con los caracteres de alguna de las oraciones procesadas.

## Uso

1. Coloca las oraciones en un archivo llamado `entrada.txt`, una por línea.
2. Ejecuta el script `invertir_palabras.py`.

```bash
python invertir_palabras.py

Observa las versiones invertidas de las oraciones en la salida estándar.
Ingresa una cadena cuando se solicite y el programa buscará si se puede formar con los caracteres de alguna oración invertida.

Funciones
invertir_palabras(cadena)
Toma una cadena de palabras, la divide en palabras individuales, invierte cada palabra y devuelve la cadena invertida.

procesar_archivo(archivo_entrada)
Lee un archivo de entrada con oraciones, aplica la inversión de palabras y muestra las oraciones invertidas en minúscula en la salida estándar.

encontrar_cadena_oracion(oraciones, cadena)
Busca si una cadena dada puede formarse con los caracteres de alguna de las oraciones invertidas y devuelve la oración correspondiente en mayúscula si se encuentra.

python invertir_palabras.py


Ingrese una cadena: aseasacseajoreja

La cadena se puede formar con los caracteres de la siguiente oración:
ASE ASAC SE AJOR


Contribuir
Siéntete libre de contribuir o informar problemas creando un issue.


Espero que esto te sea útil. ¡No dudes en personalizarlo según tus necesidades!


# ///////////////////////////////////////// Cifrado Bifido /////////////////////////////////////////
def cifrado_bífido(palabra, cifrar):
    def indexación(coordenadas_cifrado):
        palabra_indexada = ""
        for coord in coordenadas_cifrado:
            fila, columna = coord
            letra_cifrada = tabla_polybius[fila][columna]
            palabra_indexada += letra_cifrada
        return palabra_indexada
    
    tabla_polybius = [['A', 'B', 'C', 'D', 'E'],
                      ['F', 'G', 'H', '(I/J)', 'K'],
                      ['L', 'M', 'N', 'O', 'P'],
                      ['Q', 'R', 'S', 'T', 'U'],
                      ['V', 'W', 'X', 'Y', 'Z']]

    palabra = palabra.upper()
    palabra_cifrada = ""
    coordenadas = []

    for letra in palabra:
        for i in range(5):
            for j in range(5):
                if letra in tabla_polybius[i][j]:
                    coordenadas.append(i)
                    coordenadas.append(j)

    mitad = len(coordenadas) // 2

    if cifrar:
        coordenadas_cifrado = [(coordenadas[:mitad][i], coordenadas[mitad:][i]) for i in range(mitad)]
        palabra_cifrada = indexación(coordenadas_cifrado)
    else:
        coordenadas_descifrado = coordenadas[::2] + coordenadas[1::2]
        palabra_cifrada = indexación([(coordenadas_descifrado[i], coordenadas_descifrado[i + 1]) for i in range(0, len(coordenadas_descifrado), 2)])
    return palabra_cifrada

# ///////////////////////////////////////// Input Cifrado Bifido /////////////////////////////////////////
def método_bífido(cifrar):
    while True:
        input_word = input(f"› Ingrese la palabra a {'cifrar' if cifrar else 'descifrar'}: ")
        if validar_input_excepción(input_word):
            break

    palabra_resultado = cifrado_bífido(input_word, cifrar = cifrar)

    print("\n========================== Resultado ==========================\n" +
          f"Palabra {'Original' if cifrar else 'Cifrada'}: {input_word}\n" +
          f"Palabra {'Cifrada' if cifrar else 'Descifrada'}: {palabra_resultado}")
    
# ///////////////////////////////////////// Validaciones /////////////////////////////////////////
def validar_input(palabra):
    if not all(c.isalpha() or c.isspace() for c in palabra):
        print("╔══════════════════════════════════════════════╗\n" +
              "║ Error: La palabra debe contener solo letras. ║\n" +
              "║ Por favor, ingrese una palabra válida.       ║\n" +
              "╚══════════════════════════════════════════════╝")
        return False
    return True

def validar_input_excepción(palabra):
    if not all(c.isalpha() or c.isspace() for c in palabra) or 'Ñ' in palabra.upper():
        print("╔═════════════════════════════════════════════════════════════════════════════╗\n" + 
              "║ Error: La palabra debe contener solo letras y no debe incluir la letra 'Ñ'. ║\n" +
              "║ Por favor, ingrese una palabra válida.                                      ║\n" +
              "╚═════════════════════════════════════════════════════════════════════════════╝")
        return False
    return True

# ///////////////////////////////////////// Corregir /////////////////////////////////////////
# Al ingresar una palabra el programa se detiene por un error
def validar_posición(posición):
    if not str(posición).isdigit() or int(posición) <= 0:
        print("╔═════════════════════════════════════════════════════════╗\n" + 
              "║ Error: La posición debe ser un valor numérico positivo. ║\n" +
              "║ Por favor, ingrese una posición válida.                 ║\n" +
              "╚═════════════════════════════════════════════════════════╝")
        return False
    return True

# ///////////////////////////////////////// Menú /////////////////////////////////////////
opciones = {
    # "1": lambda: método_cesar(cifrar = True),
    # "2": lambda: método_cesar(cifrar = False),
    "3": lambda: método_bífido(cifrar = True),
    "4": lambda: método_bífido(cifrar = False),
    # "5": cifrado_Vigenere,
    # "6": descifrado_Vigenere,
    "0": lambda: print("Saliendo del programa.")
}

while True:
    print("╔════════════════════════════════════════════════╗\n" +
          "║            Seleccione una operación            ║\n" +
          "╠════════════════════════════════════════════════╣\n" +
          "║ 1.- Cifrado César    | 2.- Descifrado César    ║\n" +
          "║ 3.- Cifrado Bifido   | 4.- Descifrado Bifido   ║\n" +
          "║ 5.- Cifrado Vigenere | 6.- Descifrado Vigenere ║\n" +
          "║ 0.- Salir                                      ║\n" +
          "╚════════════════════════════════════════════════╝")

    opción = input("› Ingrese el número de la opción: ")

    if opción == "0":
        break

    if opción in opciones:
        opciones[opción]()
    else:
        print("Opción no válida. Inténtelo de nuevo.")
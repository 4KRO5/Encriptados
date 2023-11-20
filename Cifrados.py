# ///////////////////////////////////////// Cifrado Cesar /////////////////////////////////////////
def cifrado_cesar(palabra, pos, cifrar = True):
    pos %= 26
    resultado = ""

    for char in palabra.upper():
        if char.isalpha() and char != 'Ñ':
            if cifrar:
                resultado += chr((ord(char) - 65 + pos) % 26 + 65)
            else:
                resultado += chr((ord(char) - 65 - pos) % 26 + 65)
        else:
            resultado += char

    return resultado

# ///////////////////////////////////////// Input Cifrado Cesar /////////////////////////////////////////
def método_cesar(cifrar = True):
    while True:
        input_word = input(f"› Ingrese la palabra a {'cifrar' if cifrar else 'descifrar'}: ")
        if validar_input_excepción(input_word):
            break

    while True:
        posición = int(input(f"› Ingrese la posición de {'cifrado' if cifrar else 'descifrado'}: "))
        if validar_posición(posición):
            break

    palabra_resultado = cifrado_cesar(input_word, posición, cifrar = cifrar)
    
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

# def validar_posición(posición):
#     try:
#         posición = int(posición)
#         if posición <= 0:
#             print("╔═════════════════════════════════════════════════════════╗\n" + 
#                   "║ Error: La posición debe ser un valor numérico positivo. ║\n" +
#                   "║ Por favor, ingrese una posición válida.                 ║\n" +
#                   "╚═════════════════════════════════════════════════════════╝")
#             return False
#         return True
#     except ValueError:
#         print("╔═════════════════════════════════════════════════════════╗\n" + 
#               "║ Error: La posición debe ser un valor numérico positivo. ║\n" +
#               "║ Por favor, ingrese una posición válida.                 ║\n" +
#               "╚═════════════════════════════════════════════════════════╝")
#         return False

# ///////////////////////////////////////// Menú /////////////////////////////////////////
opciones = {
    "1": lambda: método_cesar(cifrar = True),
    "2": lambda: método_cesar(cifrar = False),
    # "3": cifrado_Bifido,
    # "4": descifrado_Bifido,
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
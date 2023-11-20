# ///////////////////////////////////////// Cifrado Cesar /////////////////////////////////////////
def cifrar_cesar(palabra, pos):
    pos %= 26
    resultado = ""

    for char in palabra.upper():
        if char.isalpha() and char != 'Ñ':
            resultado += chr((ord(char) - 65 + pos) % 26 + 65)
        else:
            resultado += char

    return resultado

def descifrar_cesar(palabra, pos):
    pos %= 26
    resultado = ""

    for char in palabra.upper():
        if char.isalpha() and char != 'Ñ':
            resultado += chr((ord(char) - 65 - pos) % 26 + 65)
        else:
            resultado += char

    return resultado

# ///////////////////////////////////////// Input Cifrado Cesar /////////////////////////////////////////
def cifrado_Cesar():
    while True:
        palabra_original = input("Ingrese la palabra a cifrar: ")
        if validar_input(palabra_original):
            break

    while True:
        posición_cifrado = int(input("Ingrese la posición de cifrado: "))
        if validar_posición(posición_cifrado):
            break

    palabra_cifrada = cifrar_cesar(palabra_original, posición_cifrado)
    
    print("\n============= Resultado ===============\n" +
         f"Palabra Original: {palabra_original}\n" +
         f"Palabra Cifrada: {palabra_cifrada}")

def descifrado_Cesar():
    while True:
        palabra_original = input("Ingrese la palabra a descifrar: ")
        if validar_input_excepción(palabra_original):
            break

    while True:
        posición_descifrado = int(input("Ingrese la posición de descifrado: "))
        if validar_posición(posición_descifrado):
            break

    palabra_descifrada = descifrar_cesar(palabra_original, posición_descifrado)
    
    print("\n============= Resultado ===============\n" +
         f"Palabra Original: {palabra_original}\n" +
         f"Palabra Cifrada: {palabra_descifrada}")

# ///////////////////////////////////////// Validaciones /////////////////////////////////////////
def validar_input_excepción(palabra):
    if not all(c.isalpha() or c.isspace() for c in palabra) or 'Ñ' in palabra.upper():
        print("Error: La palabra debe contener solo letras y no debe incluir la letra 'Ñ'.\n" +
              "Por favor, ingrese una palabra válida.\n" +
              "---------------------------------------")
        return False
    return True

def validar_input(clave):
    if not all(c.isalpha() or c.isspace() for c in clave):
        print("Error: La clave debe contener solo letras. Por favor, ingrese una clave válida.\n" +
              "---------------------------------------")
        return False
    return True

def validar_posición(posición):
    if not isinstance(posición, int) or posición <= 0:
        print("Error: La posición debe ser un número entero positivo.\n" +
              "Por favor, ingrese una posición válida.\n" +
              "---------------------------------------")
        return False
    return True

# ///////////////////////////////////////// Menú /////////////////////////////////////////
opciones = {
    "1": cifrado_Cesar,
    "2": descifrado_Cesar,
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

    opción = input("Ingrese el número de la opción: ")

    if opción == "0":
        break

    if opción in opciones:
        opciones[opción]()
    else:
        print("Opción no válida. Inténtelo de nuevo.")
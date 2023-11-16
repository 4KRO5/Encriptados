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

# ///////////////////////////////////////// Cifrado Bifido /////////////////////////////////////////
def cifrar_Bifido(palabra):
    # Implementa tu lógica de cifrado Bifido aquí
    # Este es solo un marcador de posición
    return "Cifrado Bifido: " + palabra

# ///////////////////////////////////////// Cifrado Vigenere /////////////////////////////////////////
def cifrar_vigenere(palabra, clave, considerar_n=True):
    # if not all(c.isalpha() or c.isspace() for c in palabra) or not clave.isalpha():
    #     return "La palabra y la clave deben contener solo letras y/o espacios."

    palabra = palabra.upper()
    clave = clave.upper()

    resultado = ""
    i = 0

    for char in palabra:
        if char.isalpha():
            if not considerar_n and char == 'Ñ':
                resultado += char
            else:
                m = ord(char) - 65
                k = ord(clave[i % len(clave)]) - 65
                c = (m + k) % 26
                resultado += chr(c + 65)
                i += 1
        else:
            resultado += char

    return resultado

def descifrar_vigenere(palabra, clave, considerar_n=True):
    if not all(c.isalpha() or c.isspace() for c in palabra) or not clave.isalpha():
        return "La palabra y la clave deben contener solo letras y/o espacios."

    palabra = palabra.upper()
    clave = clave.upper()

    resultado = ""
    i = 0

    for char in palabra:
        if char.isalpha():
            if not considerar_n and char == 'Ñ':
                resultado += 'Ñ'
            else:
                c = (ord(char) - 65) % 26
                k = ord(clave[i % len(clave)]) - 65
                m = (c - k) % 26
                resultado += chr(m + 65)
                i += 1
        else:
            resultado += char

    return resultado

# ///////////////////////////////////////// Validaciones /////////////////////////////////////////
def validar_clave_excepción(palabra):
    if not all(palabra.isalpha() or palabra.isspace) or 'Ñ' in palabra.upper():
        print("Error: La palabra debe contener solo letras y no debe incluir la letra 'Ñ'.\n" +
              "Por favor, ingrese una palabra válida.\n" +
              "---------------------------------------")
        return False
    return True

def validar_clave(clave):
    if not clave.isalpha():
        print("Error: La clave debe contener solo letras. Por favor, ingrese una clave válida.\n" +
              "Por favor, ingrese una clave válida.\n" +
              "---------------------------------------")
        return False
    return True

def validar_posición(posición):
    if not posición.isdigit():
        print("Error: La posición debe ser un número entero.\n" + 
              "Por favor, ingrese una posición válida.\n" +
              "---------------------------------------")
        return False
    return True

# ///////////////////////////////////////// Input Cifrado Cesar /////////////////////////////////////////
def cifrado_Cesar():
    while True:
        palabra_original = input("Ingrese la palabra a cifrar: ")
        if validar_clave_excepción(palabra_original):
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
        if validar_clave_excepción(palabra_original):
            break

    while True:
        posición_descifrado = input("Ingrese la posición de descifrado: ")
        if validar_posición(posición_descifrado):
            break

    posición_descifrado = int(posición_descifrado)
    palabra_descifrada = descifrar_cesar(palabra_original, posición_descifrado)
    
    print("\n============= Resultado ===============\n" +
         f"Palabra Original: {palabra_original}\n" +
         f"Palabra Cifrada: {palabra_descifrada}")

# ///////////////////////////////////////// Input Cifrado Bifido /////////////////////////////////////////
def cifrado_Bifido():
    palabra_original = input("Ingrese la palabra a cifrar: ")
    palabra_cifrada = cifrar_Bifido(palabra_original)
    print("\n============= Resultado ===============\n" +
         f"Palabra Original: {palabra_original}\n" +
         f"Palabra Cifrada: {palabra_cifrada}")

# ///////////////////////////////////////// Input Cifrado Vigenere /////////////////////////////////////////
def cifrado_Vigenere():
    considerar_n = input("¿Desea considerar la letra 'Ñ' en el universo? (Sí: 1, No: 0): ")
    
    while True:
        palabra_original = input("Ingrese la palabra a cifrar: ")
        if validar_clave_excepción(palabra_original):
            break
        
    while True:
        clave_vigenere = input("Ingrese la clave Vigenere: ")
        if validar_clave(clave_vigenere):
            break
    
    if considerar_n == "1":
        palabra_cifrada_vigenere = cifrar_vigenere(palabra_original, clave_vigenere, considerar_n=True)
    else:
        palabra_cifrada_vigenere = cifrar_vigenere(palabra_original, clave_vigenere, considerar_n=False)

    print("\n============= Resultado ===============\n" +
         f"Palabra Original: {palabra_original}\n" +
         f"Palabra Descifrada: {palabra_cifrada_vigenere}")

def descifrado_Vigenere():
    palabra_original = input("Ingrese la palabra a descifrar: ")
    clave_vigenere = input("Ingrese la clave Vigenere: ")
    considerar_n = input("¿Desea considerar la letra 'Ñ' en el universo? (Sí: 1, No: 0): ")

    if considerar_n == "1":
        palabra_descifrada_vigenere = descifrar_vigenere(palabra_original, clave_vigenere, considerar_n=True)
    else:
        palabra_descifrada_vigenere = descifrar_vigenere(palabra_original, clave_vigenere, considerar_n=False)

    print("\n============= Resultado ===============\n" +
         f"Palabra Original: {palabra_original}\n" +
         f"Palabra Descifrada: {palabra_descifrada_vigenere}\n")

# ///////////////////////////////////////// Menú /////////////////////////////////////////
opciones = {
    "1": cifrado_Cesar,
    "2": descifrado_Cesar,
    "3": cifrado_Bifido,
    # "4": descifrado_Bifido,
    "5": cifrado_Vigenere,
    "6": descifrado_Vigenere,
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

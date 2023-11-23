from Validations import validate_input, validate_input_universe

# ///////////////////////////////////////// Vigenere Encrypted /////////////////////////////////////////
def vigenere_encrypted(word, key, universe, cryptography):
    result = []
    key = key.upper()

    for i, char in enumerate(word):
        if char.upper() in universe:
            char_index = universe.index(char.upper())
            key_index = universe.index(key[i % len(key)])
            if cryptography:
                encrypted_index = (char_index + key_index) % len(universe)
            else:
                encrypted_index = (char_index - key_index) % len(universe)

            encrypted_char = universe[encrypted_index]
            result.append(encrypted_char.lower() if char.islower() else encrypted_char)
        else:
            result.append(char)

    return ''.join(result)

# ///////////////////////////////////////// Vigenere Encrypted Input /////////////////////////////////////////
def vigenere_encrypted_input(universe, cryptography):
    while True:    
        if not universe:
            universe = input("› Ingrese el alfabeto del universo: ")
        if validate_input(universe, True):
            break
        else:
            universe = ""

    while True:
        input_word = input("› Ingrese la palabra a cifrar: ")
        if validate_input_universe(input_word, universe):
            break

    while True:
        key = input("› Ingrese la clave: ")
        if validate_input_universe(key, universe):
            break

    word_result = vigenere_encrypted(input_word, key, universe, cryptography)
    
    print("\n============= Resultado ===============\n" +
          f"Palabra Original: {input_word}\n" +
          f"Palabra Cifrada: {word_result.upper()}")

# ///////////////////////////////////////// Vigenere Encryption Menu /////////////////////////////////////////
def vigenere_encrypted_menu(cryptography):
    universe_AE = "ABCDE"
    universe_AZ = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    user_defined_universe = ""

    options = {
        "1": lambda: vigenere_encrypted_input(universe_AE, cryptography),
        "2": lambda: vigenere_encrypted_input(universe_AZ, cryptography),
        "3": lambda: vigenere_encrypted_input(user_defined_universe, cryptography)
    }

    while True:
        print("╔════════════════════════════════════════════════╗\n" +
              "║            Seleccione una operación            ║\n" +
              "╠═══════════════════════╦════════════════════════╣\n" +
              "║ 1.- Universo (A-E)    ║ 2.- Universo (A-Z)     ║\n" +
              "║ 3.- Definir Universo  ║                        ║\n" +
              "╠═══════════════════════╩════════════════════════╣\n" +
              "║ 0.- Salir                                      ║\n" +
              "╚════════════════════════════════════════════════╝")
        
        option = input("› Ingrese el número de la opción: ")

        if option == "0":
            break

        if option in options:
            options[option]()
        else:
            print("Opción no válida. Inténtelo de nuevo.")
from Validations import validate_input_universe

# ///////////////////////////////////////// Vigenere Encrypted Input /////////////////////////////////////////
def vigenere_encrypted(word, key, universe, cryptography):
    result = ""

    if cryptography:
        for i in range(len(word)):
            char = word[i].upper()
            if char in universe:
                plaintext_char_index = universe.index(char)
                key_char_index = universe.index(key[i % len(key)])
                encrypted_char_index = (plaintext_char_index + key_char_index) % len(universe)
                result += universe[encrypted_char_index]
            else:
                result += char
    else:
        for i in range(len(word)):
            char = word[i].upper()
            if char in universe:
                word = universe.index(char)
                key_char_index = universe.index(key[i % len(key)])
                decrypted_char_index = (word - key_char_index) % len(universe)
                result += universe[decrypted_char_index]
            else:
                result += char
    return result

# ///////////////////////////////////////// Vigenere Encrypted Input /////////////////////////////////////////
def vigenere_encrypted_input(universe, cryptography):
    if universe == "":
        universe = input("› Ingrese el alfabeto del universo: ")

    while True:
        input_word = input("› Ingrese la palabra a cifrar: ")
        if validate_input_universe(input_word, universe):  # Asegúrate de tener 'universe' definido
            break

    while True:
        key = input("› Ingrese la clave: ")
        if validate_input_universe(key, universe):  # Asegúrate de tener 'universe' definido
            break

    word_result = vigenere_encrypted(input_word, key, universe, cryptography)
    
    print("\n============= Resultado ===============\n" +
          f"Palabra Original: {input_word.capitalize()}\n" +
          f"Palabra Cifrada: {word_result.capitalize()}")

# ///////////////////////////////////////// Vigenere Encryption Menu /////////////////////////////////////////
def vigenere_encrypted_menu(cryptography):
    universe_AE = "ABCDE"
    universe_AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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
              "╚═══════════════════════╩════════════════════════╝")
        
        option = input("› Ingrese el número de la opción: ")

        if option == "0":
            break

        if option in options:
            options[option]()
        else:
            print("Opción no válida. Inténtelo de nuevo.")
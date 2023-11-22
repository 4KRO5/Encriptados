from Validations import validate_input_exception, validate_position

# ///////////////////////////////////////// Cesar Encrypted /////////////////////////////////////////
def cesar_encrypted(word, position, cryptography):
    position %= 26
    result = ""

    for char in word.upper():
        if char.isalpha() and char != 'Ñ':
            if cryptography:
                result += chr((ord(char) - 65 + position) % 26 + 65)
            else:
                result += chr((ord(char) - 65 - position) % 26 + 65)
        else:
            result += char
    return result

# ///////////////////////////////////////// Cesar Encrypted Input /////////////////////////////////////////
def cesar_encrypted_input(cryptography):
    while True:
        input_word = input(f"› Ingrese la palabra a {'cifrar' if cryptography else 'descifrar'}: ")
        if validate_input_exception(input_word):
            break

    while True:
        position = int(input(f"› Ingrese la posición de {'cifrado' if cryptography else 'descifrado'}: "))
        if validate_position(position):
            break

    word_result = cesar_encrypted(input_word, position, cryptography = cryptography)
    
    print("\n════════════════════ Resultado ═══════════════════\n" +
          f"Palabra {'Original' if cryptography else 'Cifrada'}: {input_word}\n" +
          f"Palabra {'Cifrada' if cryptography else 'Descifrada'}: {word_result}")
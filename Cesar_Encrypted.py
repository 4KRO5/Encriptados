from Validations import validate_input_exception, validate_position

# ///////////////////////////////////////// Cesar Encrypted /////////////////////////////////////////
def cesar_encrypted(word, position, cryptography):
    position = int(position) % 26  
    result = ""

    for char in word:
        if char.isalpha() and char != 'Ñ':
            base = ord('A') if char.isupper() else ord('a')
            shift = position if cryptography else - position
            result += chr((ord(char) - base + shift) % 26 + base)
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
        position = input(f"› Ingrese la posición de {'cifrado' if cryptography else 'descifrado'}: ")
        if validate_position(position):
            break

    word_result = cesar_encrypted(input_word, position, cryptography)

    print("\n════════════════════ Resultado ═══════════════════\n" +
          f"Palabra {'Original' if cryptography else 'Cifrada'}: {input_word}\n" +
          f"Palabra {'Cifrada' if cryptography else 'Descifrada'}: {word_result}")
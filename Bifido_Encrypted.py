from Validations import validate_input_exception, validate_position

# ///////////////////////////////////////// Cifrado Bífido /////////////////////////////////////////
def bifido_encrypted(word, cryptography):
    def indexing(encryption_coordinates):
        encrypted_word = ""
        for coord in encryption_coordinates:
            row, column = coord
            encrypted_letter = polybius_table[row][column]
            encrypted_word += encrypted_letter
        return encrypted_word
    
    polybius_table = [['A', 'B', 'C', 'D', 'E'],
                      ['F', 'G', 'H', '(I/J)', 'K'],
                      ['L', 'M', 'N', 'O', 'P'],
                      ['Q', 'R', 'S', 'T', 'U'],
                      ['V', 'W', 'X', 'Y', 'Z']]

    word = word.upper()
    encrypted_word = ""
    coordinates = []

    for letter in word:
        for i in range(5):
            for j in range(5):
                if letter in polybius_table[i][j]:
                    coordinates.append(i)
                    coordinates.append(j)

    middle = len(coordinates) // 2

    if cryptography:
        encryption_coordinates = [(coordinates[:middle][i], coordinates[middle:][i]) for i in range(middle)]
        encrypted_word = indexing(encryption_coordinates)
    else:
        coordinates_decryption = coordinates[::2] + coordinates[1::2]
        encrypted_word = indexing([(coordinates_decryption[i], coordinates_decryption[i + 1]) for i in range(0, len(coordinates_decryption), 2)])
    return encrypted_word

# ///////////////////////////////////////// Bifido Encrypted Input /////////////////////////////////////////
def bifido_encrypted_input(cryptography):
    while True:
        input_word = input(f"› Ingrese la palabra a {'cifrar' if cryptography else 'descifrar'}: ")
        if validate_input_exception(input_word):
            break

    word_result = bifido_encrypted(input_word, cryptography = cryptography)

    print("\n========================== Resultado =========================\n" +
          f"Palabra {'Original' if cryptography else 'Cifrada'}: {input_word}\n" +
          f"Palabra {'Cifrada' if cryptography else 'Descifrada'}: {word_result}")
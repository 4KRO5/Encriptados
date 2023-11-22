from Validations import validate_input_exception

# ///////////////////////////////////////// Cifrado Bífido /////////////////////////////////////////
def bifido_encrypted(word, cryptography):
    def indexing(encryption):
        return ''.join([polybius_table[row][column] for row, column in encryption])
    
    polybius_table = [['A', 'B', 'C', 'D', 'E'],
                      ['F', 'G', 'H', '(I/J)', 'K'],
                      ['L', 'M', 'N', 'O', 'P'],
                      ['Q', 'R', 'S', 'T', 'U'],
                      ['V', 'W', 'X', 'Y', 'Z']]

    word = word.upper()
    coordinates = []

    for letter in word:
        for i, row in enumerate(polybius_table):
            for j, cell in enumerate(row):
                if letter in cell:
                    coordinates.extend([i, j])

    middle = len(coordinates) // 2

    if cryptography:
        encryption = list(zip(coordinates[:middle], coordinates[middle:]))
    else:
        encryption = coordinates[::2] + coordinates[1::2]
        encryption = list(zip(encryption[::2], encryption[1::2]))

    return indexing(encryption)

# ///////////////////////////////////////// Bifido Encrypted Input /////////////////////////////////////////
def bifido_encrypted_input(cryptography):
    while True:
        input_word = input(f"› Ingrese la palabra a {'cifrar' if cryptography else 'descifrar'}: ")
        if validate_input_exception(input_word):
            break

    word_result = bifido_encrypted(input_word, cryptography = cryptography)

    print("\n========================== Resultado =========================\n" +
          f"Palabra {'Original' if cryptography else 'Cifrada'}: {input_word.capitalize()}\n" +
          f"Palabra {'Cifrada' if cryptography else 'Descifrada'}: {word_result.capitalize()}")
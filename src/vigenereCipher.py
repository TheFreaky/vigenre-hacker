LETTERS = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯЁ'


def decrypt_message(key, message):
    translated = []  # stores the encrypted/decrypted message string

    key_index = 0
    key = key.upper()

    for symbol in message:  # loop through each character in message
        num = LETTERS.find(symbol.upper())
        if num != -1:
            num -= LETTERS.find(key[key_index])  # subtract if decrypting

            num %= len(LETTERS)  # handle the potential wrap-around

            # add symbol to the end of translated.
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            key_index += 1  # move to the next letter in the key
            key_index = key_index % len(key)
        else:
            # The symbol was not in LETTERS, so add it to translated as is.
            translated.append(symbol)

    return ''.join(translated)

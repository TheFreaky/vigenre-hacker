UPPER_LETTERS = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯЁ'
LETTERS_AND_SPACE = UPPER_LETTERS + UPPER_LETTERS.lower() + ' \t\n'


def load_dictionary():
    dictionary_file = open('russian.txt')
    words = set()
    for word in dictionary_file.read().split('\n'):
        words.add(word)
    dictionary_file.close()
    return words


RUSSIAN_WORDS = load_dictionary()


def get_words_match_russian_probability(message):
    message = message.lower()
    message = remove_non_letters(message)
    possible_words = message.split()

    if not possible_words:
        return 0.0  # no words at all, so return 0.0

    matches = 0
    for word in possible_words:
        if word in RUSSIAN_WORDS:
            matches += 1
    return float(matches) / len(possible_words)


def remove_non_letters(message):
    letters_only = []
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            letters_only.append(symbol)
    return ''.join(letters_only)


def is_russian(message, word_percentage=20, letter_percentage=85):
    # By default, 20% of the words must exist in the dictionary file, and
    # 85% of all the characters in the message must be letters or spaces
    # (not punctuation or numbers).
    words_match = get_words_match_russian_probability(message) * 100 >= word_percentage
    num_letters = len(remove_non_letters(message))
    message_letters_percentage = float(num_letters) / len(message) * 100
    letters_match = message_letters_percentage >= letter_percentage
    return words_match and letters_match

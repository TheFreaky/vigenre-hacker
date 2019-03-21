RUSSIAN_LETTER_FREQ = {'О': 10.97, 'Е': 8.45, 'А': 8.01, 'И': 7.35, 'Н': 6.70, 'Т': 6.26, 'С': 5.47, 'Р': 4.73,
                       'В': 4.54, 'Л': 4.40, 'К': 3.49, 'М': 3.21, 'Д': 2.98, 'П': 2.81, 'У': 2.62, 'Я': 2.01,
                       'Ы': 1.90, 'Ь': 1.74, 'Г': 1.70, 'З': 1.65, 'Б': 1.59, 'Ч': 1.44, 'Й': 1.21, 'Х': 0.97,
                       'Ж': 0.94, 'Ш': 0.73, 'Ю': 0.64, 'Ц': 0.48, 'Щ': 0.36, 'Э': 0.32, 'Ф': 0.26, 'Ъ': 0.04,
                       'Ё': 0.04}
ORDERED_FREQ_LETTERS = 'ОЕАИНТСРВЛКМДПУЯЫЬГЗБЧЙХЖШЮЦЩЭФЪЁ'
LETTERS = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯЁ'


def get_letter_count(message):
    # Returns a dictionary with keys of single letters and values of the
    # count of how many times they appear in the message parameter.
    letter_count = {}

    for letter in LETTERS:
        letter_count[letter] = 0

    for letter in message.upper():
        if letter in LETTERS:
            letter_count[letter] += 1

    return letter_count


def get_item_at_index_zero(x):
    return x[0]


def get_frequency_order(message):
    # Returns a string of the alphabet letters arranged in order of most
    # frequently occurring in the message parameter.

    # first, get a dictionary of each letter and its frequency count
    letter_to_freq = get_letter_count(message)

    # second, make a dictionary of each frequency count to each letter(s)
    # with that frequency
    freq_to_letter = {}
    for letter in LETTERS:
        if letter_to_freq[letter] not in freq_to_letter:
            freq_to_letter[letter_to_freq[letter]] = [letter]
        else:
            freq_to_letter[letter_to_freq[letter]].append(letter)

    # third, put each list of letters in reverse "ETAOIN" order, and then
    # convert it to a string
    for freq in freq_to_letter:
        freq_to_letter[freq].sort(key=ORDERED_FREQ_LETTERS.find, reverse=True)
        freq_to_letter[freq] = ''.join(freq_to_letter[freq])

    # fourth, convert the freq_to_letter dictionary to a list of tuple
    # pairs (key, value), then sort them
    freq_pairs = list(freq_to_letter.items())
    freq_pairs.sort(key=get_item_at_index_zero, reverse=True)

    # fifth, now that the letters are ordered by frequency, extract all
    # the letters for the final string
    freq_order = []
    for freqPair in freq_pairs:
        freq_order.append(freqPair[1])

    return ''.join(freq_order)


def russian_freq_match_score(message):
    # Return the number of matches that the string in the message
    # parameter has when its letter frequency is compared to English
    # letter frequency. A "match" is how many of its six most frequent
    # and six least frequent letters is among the six most frequent and
    # six least frequent letters for English.
    freq_order = get_frequency_order(message)

    match_score = 0
    # Find how many matches for the six most common letters there are.
    for common_letter in ORDERED_FREQ_LETTERS[:6]:
        if common_letter in freq_order[:6]:
            match_score += 1
    # Find how many matches for the six least common letters there are.
    for uncommon_letter in ORDERED_FREQ_LETTERS[-6:]:
        if uncommon_letter in freq_order[-6:]:
            match_score += 1

    return match_score

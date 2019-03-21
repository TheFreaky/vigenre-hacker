import itertools
import re

import detectEnglish
import freqAnalysis
import vigenereCipher

LETTERS = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯЁ'
NUM_MOST_FREQ_LETTERS = 4
MAX_KEY_LENGTH = 10
NON_LETTERS_PATTERN = re.compile('[^А-ЯЁ]')


def main():
    cipher_text = """ЬВЙБО НКХЛР ТАЫЩИ ЮЧЧШР УРЩУЕ ЪИШЯФ РВИЯВ ПНЯИЭ УОШЦШ ЁЫЩЩБ ЦЮХФШ ЮЧАДК КЗЙАД ЬЩЪИЦ ЫЦШЩИ ЫЫЕШГ ЖПЫОЬ ЦХХЬЬ ЮОИБУ ШШГИЧ УЗУВЬ ПГСЩЦ ТПЙФЬ ВСПЫО ПЯКЁА ТЩРСЬ ШЬУРН ТУОХС ПФНШК ЩХХША КЁЩРХ ЭКЮЙП ДПФЮЬ ПБФЫЦ ШШГЩУ РЫХЮФ ЯЯЦЭН ГКЁОЁ ШТЩУЧ ЁАСКЁ ЧЖДЭН ЛЮПДФ ЦЦМЁУ ВШЛЮП ЫОУЮГ ДТЁЩЯ КИШЬУ ЪИЮЦЯ ЛЮСЖШ ЬУЦИМ ДЭОЯИ ЯВПНС ИФАЮЮ БУРША ЬПИБА ЪЖЫЧП ЁПКЯЪ ЭАСЛЮ СШТЁЮ ХОСЁЭ ОЯИЁШ ЖРЮСО ТЁЭСЫ ЛСОПУ ЙПЙФЭ ЛЩХТЭ ПЩЦПГ РЩАИД ВПШЦЦ ШШОУБ ШЮЮКТ ЯЛРЁЧ РРСПВ ПЬЁЩЮ ГАЫСЦ ХЁЧРР СЭЖЭЫ ЭЙЕЫЧ КЯИЖУ ЁЭЮЧЩ ТХУШЦ ШТЪУЖ ЙПФФТ РОУАО ЬЯМЫУ ЁУПИЭ ШОПЯШ ВГЩЛО ЫАСОП УЙПАЯ ОСЦКТ ТЩБЬФ УЯЬВЛ ХЁЬЩЪ ИТЮПЬ ВСПЫО ЩАМРЁ ЙКЭОА ДЬЩФЧ ПГПЧЯ ЬЯВПН ЬОЭЫН КЩЮПЧ ЭЦЧЦЮ ГАШЛО ПЮЧАС ИЮФНТ СЦКТЭ МЦЪЯШ ЕУВДП ЭПСХЧ ЬЕОНЯ РЬАХШ ЯЪБОО ЩШЦРЭ ЭЧЬОЭ ЫНКБИ ФАЩЮЭ ОЭДПЧ ЩИШТЫ ЛВОЁЫ ПЦСХШ ТЬРЁЧ АВФПБ ЫТШЬШ ЯИЧУА ЫСМШХ ПИЙСЬ ЫОРФЧ ПБЯЛУ ЙПЫОЬ УЧСАУ ЕРОАЮ ЧКЩЦЮ ШОШЦИ ЯВФПГ ЪЬААЫ ЦЦЮТЦ ЛЫЧЭА ЫКБЫР ДКЙРН ТУОЪП ЫЛТХУ ЬСИШО ШЦШЁЫ ЩЩБЦЮ ХФШЮЧ ПЁЧХВ ЧПЁФК УШЁУС РРШЁА ЬУЫЙБ ООНРП ШЮЧГЦ ИЯВЭЭ ЩЛПХЭ ЦЩИЯВ ЭСЩЛР РЗУЕИ ТТЬРЭ ИЫЫДК ЩЦРЙФ КЫЙЪТ СКБФВ ЙПЙЕИ ВГАЛЮ ЧТЮФШ ЮГДТВ РХОЁУ ЪЖЮГЬ ТЦЛЫЧ ЭАЫКЩ ФШТЬЛ РЧАЁЭ НСЦШЫ ОЬГНХ ФЬЩФЧ ПВФВЦ ЦШСОЬ ВЙБОН КХЛРТ ЖРБЫЛ ТЭПЩЦ ПЭПСХ ГЩТСЪ АЙТШО ЩЁЩХЧ ФЦПЫЛ ТЧКГУ РЪЙНС ЫЛТЁН ЯЖПЁП АЩЧЭУ ЪЖЮЬН ТЮЫЩЦ РЧЪРЧ ЦЮГАЖ РЦШЭА ЩРЦХТ ЫЩЧОБ ТРЕВД ПБЯУЮ ЬЦЧФШ РУПАЮ ЫЦНХЮ ФШЩЖП ЫОЮЫЙ ЧУЬУО ИАХЭР ЪИЭУД УЯЦРЮ КШЯТП БЯУЮЙ ФЮФСЮ ЧАДЧК ХЛРТЩ ЛЧНКЬ ОУЭОХ ДОЪАЙ ТАОШС ИЯАЪЖ ШЧТУЬ УЦИЁА УШЛХП СЦЕЫЧ ЬТЬЛР ЪТАРЩ ХЦКЬО НЛКЮВ ОЙШГЪ УОЩТБ ХЁЧЙР ЛЮГЮУ ВЙЭЫН КЯКВЙ ФШЩЗП ЫОЭУЧ ЁЙФЬВ ЛРТЁЭ СЫЛСО ПУЙПГ ФЧМИЮ ЧЧШРУ РЩУЕЪ ИЪДЭК ШЙЪАЬ ШЯИЭУ ГЩХСБ ГНКЮЙ ПДФЫА СБАЯУ ЩИЁАЁ ЬЩТАЭ ЭФРЭХ ЧФЫСЯ ШЫОУЭ ОХДОЪ АЙТАО ЬУЧСА УШЯИЯ ШЯРХЛ ШЦПЭМ ЪОТСЕ ТСЁУА ЖРХХГ АЩРШЁ ШРЕУЙ ЭЫНКЩ ИЦЫАР ЬДАДС ЛРНТУ ОХСПФ НШКЭЧ ЦШАКБ ЛЮФЭП ЮЧПХЙ РШПРД ККШЙП БЯРХО ЫНОЫЯ ЪАЫШЬ ЫЧЩТВ РХОЁУ ДУЩИУ ВПСХЙ ЭЫЬКА ЧАГЧФ БУЮЬО ЯЦНХВ ПАЩСП ЫЫРЦЫ ПБЯЛУ ЧПФФЬ ЁЩХБН ЭБЫТШ ЬШЯИТ АЦНАЙ ИУАЖБ ЗПХОЫ ЯЪАЫШ ЬЫЬНТ ВРХОЁ УДУОИ АДПЭМ ЗПЧСЛ РЛЮГФ ЧМИЪУ ХПЯХВ ТТЛАЙ ЭДЧЫГ ОБГНК БЛЮФЭ ПСИАА СРБЫШ ТЁНЯК ЮЧПКУ ОЁАЧЬ ЁЧТШУ ЛЮСОТ СХЬЖЖ УНКЁЩ РХЭКЩ ЪЯАСР ХЧТУА ЖРСЭЧ ЧНЩНВ УЪЖЮЧ ПЫЪУР ЪЮХЫР БЫЭАО ЬРНЁЕ ТУЭСП ЮММГЖ ПВФЦЩ МШРОУ ЬСПЁФ КЩЪЯА СРХЧТ УАЖРЦ ШЭПХЯ ТПГСЩ ТЧФЁЭ КУГСЫ ЯЛВДП ЫЫРВД ПЫОЫС ЪЯВЭЬ ВЩРЁН ЭМИЁШ ЪУФСЮ ЪЬЕЦИ ШТЧШЛ ОПЕРР ЧНХЁЧ ЙРСПЧ ФФБЫТ АСЛВД ПХОЬЯ ЧБХФЭ БЫТЫЧ КБИЭЫ ЫУРЪБ УАЖПИ ФХПКХ ОТСАЖ РЧФЫЬ КЫЙЦЧ ЭЧГИУ УЯЛЮЫ ШВБРВ ЪОТЁН ЯКЮЧП КЭГАЮ ЧКЩИА ЮЭНСИ ФХПКЮ ОПЧЭЪ ГЪЪУМ ЭБЗПБ ЯЩЁЙУ УЬПСИ ШЮЧКС МШДПА ЩЗПХЭ ТТЬЦЧ ПИЙСХ ТЁЩЖС РЮКШГ ЖПВПЬ ЯЛВРО ШСЯША ЬЛЬДЭ ЕМКЩФ ШТЯРЬ СУЫЭТ ЮЬНТЬ РЮЙТЫ ЁЭМИШ ТСЫСП ФЕОТС ШЁШЗЛ ЦЫАСО ЪАЧЯУ ТЛЮНР ТЁЩЖС РЮКШЯ МЮТЯЛ БЧТАТ ЩРЦРИ ЧЩЮЙЫ ОЬЩФЧ ПВФЦЩ МШАЦШ ЯМЮТЧ ЦЩИОЪ ЙХЯЛЮ ЦЭКЁЩ ХХЭЬЕ ЧФГАН СИБВЧ КЮСЪД ЭКЮОП ЯЭСЦЫ ПФЙЭМ ИЯВЧШ ГПФШЬ КЫИТН ЯЛЧОЭ ЫМКБЛ ЮЫГКЭ ЦХЁЧФ РСПЕР РЧНХЁ ЧФРСЫ ЫОЩВУ РЪБКЯ ЫПЁЧЁ РЁХДЙ ЫЦИЪУ ХПЛТП ЫЫРЦЫ ПБЯЛУ ЧПГСЩ ТЧФЁЭ КЩЪЪУ АЖРШЮ ЮББСЫ ЛТЮРА ОФУСЛ ВДПБЯ ЩЩРТА УУВДП ЫОЫСЪ ЯВЭЬВ ЩРЁНЭ МИШЁВ ЩАХРИ ЧИРФН ФЙЧРР РЭЭШЮ ГЬТЁЪ ЯЪЮФЭ ЧРШХВ ФБЦЦЛ ТЁНЦН ХЁЧФР ЪЮГАЛ УФОРЗ УЕИУА ЁЮХЙЁ ГАНЦЦ ЭЕМКВ ЙЩЁБК ЯШЁШУ РЬЗХД ЁЙРЭХ ЧФЫСФ ЛЁЙЧР РРЭЭШ ЯХПБН ЭМИУУ ЯЛЮЫШ ВБРВЪ ОТЁНЯ КЮЧПК ЭЙАГЭ НЯТПЫ ЬЯЯЩЬ УДУЩИ ЕШЬТГ ЩРТЦЛ ЁЩХЛП РВЪОМ """
    hacked_message = hack_vigenere(cipher_text)

    if hacked_message is not None:
        print(f'Hacked message: {hacked_message}')
    else:
        print('Failed to hack encryption.')


def find_repeat_sequences_spacings(message):
    # Goes through the message and finds any 3 to 5 letter sequences
    # that are repeated. Returns a dict with the keys of the sequence and
    # values of a list of spacings (num of letters between the repeats).

    # Use a regular expression to remove non-letters from the message.
    message = NON_LETTERS_PATTERN.sub('', message.upper())

    # Compile a list of seqLen-letter sequences found in the message.
    seq_spacings = {}  # keys are sequences, values are list of int spacings
    for seq_len in range(3, 6):
        for seq_start in range(len(message) - seq_len):
            # Determine what the sequence is, and store it in seq
            seq = message[seq_start:seq_start + seq_len]

            # Look for this sequence in the rest of the message
            for i in range(seq_start + seq_len, len(message) - seq_len):
                if message[i:i + seq_len] == seq:
                    # Found a repeated sequence.
                    if seq not in seq_spacings:
                        seq_spacings[seq] = []  # initialize blank list

                    # Append the spacing distance between the repeated
                    # sequence and the original sequence.
                    seq_spacings[seq].append(i - seq_start)
    return seq_spacings


def get_useful_factors(num):
    # Returns a list of useful factors of num. By "useful" we mean factors
    # less than MAX_KEY_LENGTH + 1. For example, getUsefulFactors(144)
    # returns [2, 72, 3, 48, 4, 36, 6, 24, 8, 18, 9, 16, 12]

    if num < 2:
        return []  # numbers less than 2 have no useful factors

    factors = []  # the list of factors found

    # When finding factors, you only need to check the integers up to
    # MAX_KEY_LENGTH.
    for i in range(2, MAX_KEY_LENGTH + 1):  # don't test 1
        if num % i == 0:
            factors.append(i)
            factors.append(int(num / i))
    if 1 in factors:
        factors.remove(1)
    return list(set(factors))


def get_item_at_index_one(x):
    return x[1]


def get_most_common_factors(seq_factors):
    # First, get a count of how many times a factor occurs in seqFactors.
    factor_counts = {}  # key is a factor, value is how often if occurs

    # seqFactors keys are sequences, values are lists of factors of the
    # spacings. seqFactors has a value like: {'GFD': [2, 3, 4, 6, 9, 12,
    # 18, 23, 36, 46, 69, 92, 138, 207], 'ALW': [2, 3, 4, 6, ...], ...}
    for seq in seq_factors:
        factor_list = seq_factors[seq]
        for factor in factor_list:
            if factor not in factor_counts:
                factor_counts[factor] = 0
            factor_counts[factor] += 1

    # Second, put the factor and its count into a tuple, and make a list
    # of these tuples so we can sort them.
    factors_by_count = []
    for factor in factor_counts:
        # exclude factors larger than MAX_KEY_LENGTH
        if factor <= MAX_KEY_LENGTH:
            # factors_by_count is a list of tuples: (factor, factorCount)
            # factors_by_count has a value like: [(3, 497), (2, 487), ...]
            factors_by_count.append((factor, factor_counts[factor]))

    # Sort the list by the factor count.
    factors_by_count.sort(key=get_item_at_index_one, reverse=True)

    return factors_by_count


def kasiski_examination(cipher_text):
    # Find out the sequences of 3 to 5 letters that occur multiple times
    # in the ciphertext. repeated_seq_spacings has a value like:
    # {'EXG': [192], 'NAF': [339, 972, 633], ... }
    repeated_seq_spacings = find_repeat_sequences_spacings(cipher_text)

    # See getMostCommonFactors() for a description of seq_factors.
    seq_factors = {}
    for seq in repeated_seq_spacings:
        seq_factors[seq] = []
        for spacing in repeated_seq_spacings[seq]:
            seq_factors[seq].extend(get_useful_factors(spacing))

    # See getMostCommonFactors() for a description of factors_by_count.
    factors_by_count = get_most_common_factors(seq_factors)

    # Now we extract the factor counts from factors_by_count and
    # put them in all_likely_key_lengths so that they are easier to
    # use later.
    all_likely_key_lengths = []
    for twoIntTuple in factors_by_count:
        all_likely_key_lengths.append(twoIntTuple[0])

    return all_likely_key_lengths


def get_nth_subkeys_letters(n, key_length, message):
    # Use a regular expression to remove non-letters from the message.
    message = NON_LETTERS_PATTERN.sub('', message)

    i = n - 1
    letters = []
    while i < len(message):
        letters.append(message[i])
        i += key_length
    return ''.join(letters)


def attempt_hack_with_key_length(cipher_text, most_likely_key_length):
    # Determine the most likely letters for each letter in the key.
    cipher_text_up = cipher_text.upper()
    # all_freq_scores is a list of mostLikelyKeyLength number of lists.
    # These inner lists are the freq_scores lists.
    all_freq_scores = []
    for nth in range(1, most_likely_key_length + 1):
        nth_letters = get_nth_subkeys_letters(nth, most_likely_key_length, cipher_text_up)

        # freq_scores is a list of tuples like:
        # [(<letter>, <Eng. Freq. match score>), ... ]
        # List is sorted by match score. Higher score means better match.
        # See the englishFreqMatchScore() comments in freqAnalysis.py.
        freq_scores = []
        for possible_key in LETTERS:
            decrypted_text = vigenereCipher.decrypt_message(possible_key, nth_letters)
            key_and_freq_match_tuple = (possible_key, freqAnalysis.russian_freq_match_score(decrypted_text))
            freq_scores.append(key_and_freq_match_tuple)
        # Sort by match score
        freq_scores.sort(key=get_item_at_index_one, reverse=True)

        all_freq_scores.append(freq_scores[:NUM_MOST_FREQ_LETTERS])

    for i in range(len(all_freq_scores)):
        # use i + 1 so the first letter is not called the "0th" letter
        print('Possible letters for letter %s of the key: ' % (i + 1), end='')
        for freq_score in all_freq_scores[i]:
            print('%s ' % freq_score[0], end='')
        print()  # print a newline

    # Try every combination of the most likely letters for each position
    # in the key.
    for indexes in itertools.product(range(NUM_MOST_FREQ_LETTERS), repeat=most_likely_key_length):
        # Create a possible key from the letters in all_freq_scores
        possible_key = ''
        for i in range(most_likely_key_length):
            possible_key += all_freq_scores[i][indexes[i]][0]

        # if not SILENT_MODE:
        #     print('Attempting with key: %s' % (possible_key))

        decrypted_text = vigenereCipher.decrypt_message(possible_key, cipher_text_up)

        if detectEnglish.is_russian(decrypted_text):
            # Set the hacked ciphertext to the original casing.
            orig_case = []
            for i in range(len(cipher_text)):
                if cipher_text[i].isupper():
                    orig_case.append(decrypted_text[i].upper())
                else:
                    orig_case.append(decrypted_text[i].lower())
            decrypted_text = ''.join(orig_case)

            # Check with user to see if the key has been found.
            print(f'Possible encryption hack with key {possible_key}:')
            print(decrypted_text[:200])  # only show first 200 characters
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decrypted_text

    # No Russian-looking decryption found, so return None.
    return None


def hack_vigenere(ciphertext):
    # First, we need to do Kasiski Examination to figure out what the
    # length of the ciphertext's encryption key is.
    hacked_message = None
    all_likely_key_lengths = kasiski_examination(ciphertext)
    key_length_str = ''
    for key_length in all_likely_key_lengths:
        key_length_str += f'{key_length} '
    print(f'Kasiski Examination results say the most likely key lengths are: {key_length_str}\n')

    for key_length in all_likely_key_lengths:
        print('Attempting hack with key length %s (%s possible keys)...' % (
            key_length, NUM_MOST_FREQ_LETTERS ** key_length))
        hacked_message = attempt_hack_with_key_length(ciphertext, key_length)
        if hacked_message is not None:
            break

    # If none of the key lengths we found using Kasiski Examination
    # worked, start brute-forcing through key lengths.
    if hacked_message is None:
        print('Unable to hack message with likely key length(s). Brute forcing key length...')

        for key_length in range(1, MAX_KEY_LENGTH + 1):
            # don't re-check key lengths already tried from Kasiski
            if key_length not in all_likely_key_lengths:
                print('Attempting hack with key length %s (%s possible keys)...' % (
                    key_length, NUM_MOST_FREQ_LETTERS ** key_length))
                hacked_message = attempt_hack_with_key_length(ciphertext, key_length)
                if hacked_message is not None:
                    break
    return hacked_message


if __name__ == '__main__':
    main()

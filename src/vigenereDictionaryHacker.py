import detectEnglish, vigenereCipher


def main():
    ciphertext = """ЬВЙБО НКХЛР ТАЫЩИ ЮЧЧШР УРЩУЕ ЪИШЯФ РВИЯВ ПНЯИЭ УОШЦШ ЁЫЩЩБ ЦЮХФШ ЮЧАДК КЗЙАД ЬЩЪИЦ ЫЦШЩИ ЫЫЕШГ ЖПЫОЬ ЦХХЬЬ ЮОИБУ ШШГИЧ УЗУВЬ ПГСЩЦ ТПЙФЬ ВСПЫО ПЯКЁА ТЩРСЬ ШЬУРН ТУОХС ПФНШК ЩХХША КЁЩРХ ЭКЮЙП ДПФЮЬ ПБФЫЦ ШШГЩУ РЫХЮФ ЯЯЦЭН ГКЁОЁ ШТЩУЧ ЁАСКЁ ЧЖДЭН ЛЮПДФ ЦЦМЁУ ВШЛЮП ЫОУЮГ ДТЁЩЯ КИШЬУ ЪИЮЦЯ ЛЮСЖШ ЬУЦИМ ДЭОЯИ ЯВПНС ИФАЮЮ БУРША ЬПИБА ЪЖЫЧП ЁПКЯЪ ЭАСЛЮ СШТЁЮ ХОСЁЭ ОЯИЁШ ЖРЮСО ТЁЭСЫ ЛСОПУ ЙПЙФЭ ЛЩХТЭ ПЩЦПГ РЩАИД ВПШЦЦ ШШОУБ ШЮЮКТ ЯЛРЁЧ РРСПВ ПЬЁЩЮ ГАЫСЦ ХЁЧРР СЭЖЭЫ ЭЙЕЫЧ КЯИЖУ ЁЭЮЧЩ ТХУШЦ ШТЪУЖ ЙПФФТ РОУАО ЬЯМЫУ ЁУПИЭ ШОПЯШ ВГЩЛО ЫАСОП УЙПАЯ ОСЦКТ ТЩБЬФ УЯЬВЛ ХЁЬЩЪ ИТЮПЬ ВСПЫО ЩАМРЁ ЙКЭОА ДЬЩФЧ ПГПЧЯ ЬЯВПН ЬОЭЫН КЩЮПЧ ЭЦЧЦЮ ГАШЛО ПЮЧАС ИЮФНТ СЦКТЭ МЦЪЯШ ЕУВДП ЭПСХЧ ЬЕОНЯ РЬАХШ ЯЪБОО ЩШЦРЭ ЭЧЬОЭ ЫНКБИ ФАЩЮЭ ОЭДПЧ ЩИШТЫ ЛВОЁЫ ПЦСХШ ТЬРЁЧ АВФПБ ЫТШЬШ ЯИЧУА ЫСМШХ ПИЙСЬ ЫОРФЧ ПБЯЛУ ЙПЫОЬ УЧСАУ ЕРОАЮ ЧКЩЦЮ ШОШЦИ ЯВФПГ ЪЬААЫ ЦЦЮТЦ ЛЫЧЭА ЫКБЫР ДКЙРН ТУОЪП ЫЛТХУ ЬСИШО ШЦШЁЫ ЩЩБЦЮ ХФШЮЧ ПЁЧХВ ЧПЁФК УШЁУС РРШЁА ЬУЫЙБ ООНРП ШЮЧГЦ ИЯВЭЭ ЩЛПХЭ ЦЩИЯВ ЭСЩЛР РЗУЕИ ТТЬРЭ ИЫЫДК ЩЦРЙФ КЫЙЪТ СКБФВ ЙПЙЕИ ВГАЛЮ ЧТЮФШ ЮГДТВ РХОЁУ ЪЖЮГЬ ТЦЛЫЧ ЭАЫКЩ ФШТЬЛ РЧАЁЭ НСЦШЫ ОЬГНХ ФЬЩФЧ ПВФВЦ ЦШСОЬ ВЙБОН КХЛРТ ЖРБЫЛ ТЭПЩЦ ПЭПСХ ГЩТСЪ АЙТШО ЩЁЩХЧ ФЦПЫЛ ТЧКГУ РЪЙНС ЫЛТЁН ЯЖПЁП АЩЧЭУ ЪЖЮЬН ТЮЫЩЦ РЧЪРЧ ЦЮГАЖ РЦШЭА ЩРЦХТ ЫЩЧОБ ТРЕВД ПБЯУЮ ЬЦЧФШ РУПАЮ ЫЦНХЮ ФШЩЖП ЫОЮЫЙ ЧУЬУО ИАХЭР ЪИЭУД УЯЦРЮ КШЯТП БЯУЮЙ ФЮФСЮ ЧАДЧК ХЛРТЩ ЛЧНКЬ ОУЭОХ ДОЪАЙ ТАОШС ИЯАЪЖ ШЧТУЬ УЦИЁА УШЛХП СЦЕЫЧ ЬТЬЛР ЪТАРЩ ХЦКЬО НЛКЮВ ОЙШГЪ УОЩТБ ХЁЧЙР ЛЮГЮУ ВЙЭЫН КЯКВЙ ФШЩЗП ЫОЭУЧ ЁЙФЬВ ЛРТЁЭ СЫЛСО ПУЙПГ ФЧМИЮ ЧЧШРУ РЩУЕЪ ИЪДЭК ШЙЪАЬ ШЯИЭУ ГЩХСБ ГНКЮЙ ПДФЫА СБАЯУ ЩИЁАЁ ЬЩТАЭ ЭФРЭХ ЧФЫСЯ ШЫОУЭ ОХДОЪ АЙТАО ЬУЧСА УШЯИЯ ШЯРХЛ ШЦПЭМ ЪОТСЕ ТСЁУА ЖРХХГ АЩРШЁ ШРЕУЙ ЭЫНКЩ ИЦЫАР ЬДАДС ЛРНТУ ОХСПФ НШКЭЧ ЦШАКБ ЛЮФЭП ЮЧПХЙ РШПРД ККШЙП БЯРХО ЫНОЫЯ ЪАЫШЬ ЫЧЩТВ РХОЁУ ДУЩИУ ВПСХЙ ЭЫЬКА ЧАГЧФ БУЮЬО ЯЦНХВ ПАЩСП ЫЫРЦЫ ПБЯЛУ ЧПФФЬ ЁЩХБН ЭБЫТШ ЬШЯИТ АЦНАЙ ИУАЖБ ЗПХОЫ ЯЪАЫШ ЬЫЬНТ ВРХОЁ УДУОИ АДПЭМ ЗПЧСЛ РЛЮГФ ЧМИЪУ ХПЯХВ ТТЛАЙ ЭДЧЫГ ОБГНК БЛЮФЭ ПСИАА СРБЫШ ТЁНЯК ЮЧПКУ ОЁАЧЬ ЁЧТШУ ЛЮСОТ СХЬЖЖ УНКЁЩ РХЭКЩ ЪЯАСР ХЧТУА ЖРСЭЧ ЧНЩНВ УЪЖЮЧ ПЫЪУР ЪЮХЫР БЫЭАО ЬРНЁЕ ТУЭСП ЮММГЖ ПВФЦЩ МШРОУ ЬСПЁФ КЩЪЯА СРХЧТ УАЖРЦ ШЭПХЯ ТПГСЩ ТЧФЁЭ КУГСЫ ЯЛВДП ЫЫРВД ПЫОЫС ЪЯВЭЬ ВЩРЁН ЭМИЁШ ЪУФСЮ ЪЬЕЦИ ШТЧШЛ ОПЕРР ЧНХЁЧ ЙРСПЧ ФФБЫТ АСЛВД ПХОЬЯ ЧБХФЭ БЫТЫЧ КБИЭЫ ЫУРЪБ УАЖПИ ФХПКХ ОТСАЖ РЧФЫЬ КЫЙЦЧ ЭЧГИУ УЯЛЮЫ ШВБРВ ЪОТЁН ЯКЮЧП КЭГАЮ ЧКЩИА ЮЭНСИ ФХПКЮ ОПЧЭЪ ГЪЪУМ ЭБЗПБ ЯЩЁЙУ УЬПСИ ШЮЧКС МШДПА ЩЗПХЭ ТТЬЦЧ ПИЙСХ ТЁЩЖС РЮКШГ ЖПВПЬ ЯЛВРО ШСЯША ЬЛЬДЭ ЕМКЩФ ШТЯРЬ СУЫЭТ ЮЬНТЬ РЮЙТЫ ЁЭМИШ ТСЫСП ФЕОТС ШЁШЗЛ ЦЫАСО ЪАЧЯУ ТЛЮНР ТЁЩЖС РЮКШЯ МЮТЯЛ БЧТАТ ЩРЦРИ ЧЩЮЙЫ ОЬЩФЧ ПВФЦЩ МШАЦШ ЯМЮТЧ ЦЩИОЪ ЙХЯЛЮ ЦЭКЁЩ ХХЭЬЕ ЧФГАН СИБВЧ КЮСЪД ЭКЮОП ЯЭСЦЫ ПФЙЭМ ИЯВЧШ ГПФШЬ КЫИТН ЯЛЧОЭ ЫМКБЛ ЮЫГКЭ ЦХЁЧФ РСПЕР РЧНХЁ ЧФРСЫ ЫОЩВУ РЪБКЯ ЫПЁЧЁ РЁХДЙ ЫЦИЪУ ХПЛТП ЫЫРЦЫ ПБЯЛУ ЧПГСЩ ТЧФЁЭ КЩЪЪУ АЖРШЮ ЮББСЫ ЛТЮРА ОФУСЛ ВДПБЯ ЩЩРТА УУВДП ЫОЫСЪ ЯВЭЬВ ЩРЁНЭ МИШЁВ ЩАХРИ ЧИРФН ФЙЧРР РЭЭШЮ ГЬТЁЪ ЯЪЮФЭ ЧРШХВ ФБЦЦЛ ТЁНЦН ХЁЧФР ЪЮГАЛ УФОРЗ УЕИУА ЁЮХЙЁ ГАНЦЦ ЭЕМКВ ЙЩЁБК ЯШЁШУ РЬЗХД ЁЙРЭХ ЧФЫСФ ЛЁЙЧР РРЭЭШ ЯХПБН ЭМИУУ ЯЛЮЫШ ВБРВЪ ОТЁНЯ КЮЧПК ЭЙАГЭ НЯТПЫ ЬЯЯЩЬ УДУЩИ ЕШЬТГ ЩРТЦЛ ЁЩХЛП РВЪОМ """
    hacked_message = hackVigenere(ciphertext)

    if hacked_message is not None:
        print(f'Hacked message: {hacked_message}')
    else:
        print('Failed to hack encryption.')


def hackVigenere(ciphertext):
    fo = open('russian.txt')
    words = fo.readlines()
    fo.close()

    index = 0
    print(f'All: {len(words)}')
    for word in words:
        index += 1
        if index % 10000 == 0:
            print(f'Process {index}. {(float(index) / float(len(words))) * 100}%')

        word = word.strip() # remove the newline at the end
        decryptedText = vigenereCipher.decrypt_message(word, ciphertext)
        if detectEnglish.is_russian(decryptedText, word_percentage=20):
            # Check with user to see if the decrypted key has been found.
            print()
            print('Possible encryption break:')
            print('Key ' + str(word) + ': ' + decryptedText[:100])
            print()
            print('Enter D for done, or just press Enter to continue breaking:')
            response = input('> ')

            if response.upper().startswith('D'):
                return decryptedText


if __name__ == '__main__':
    main()
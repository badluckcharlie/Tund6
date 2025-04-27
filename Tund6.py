# # Tühja sõnastiku loomine
# andmed = {}
# # Võtmete ja väärtustega
# andmed = {'nimi': 'Mari', 'vanus': 25, 'keel': 'eesti'}
# # dict() funktsiooniga
# andmed = dict(nimi='Mari', vanus=25, keel='eesti')
# print(andmed['nimi']) # Mari
# print(andmed['vanus'])
# # Või kasutades get() — kui võtit pole, ei tule viga
# print(andmed)
# print(andmed.get('aadress', 'Ei ole määratud')) # Ei ole määratud
# print(andmed.get('nimi'))
# print(andmed.keys())
# print(andmed.values())
# for k,v in andmed.items():
#     print(k,v)
# andmed['email']="Lexa@supermail.com"
# print(andmed)
# andmed['prillid']=True
# print(andmed)
# del andmed['email']
# print(andmed)
# andmed.pop('prillid')
# andmed.update({'nimi':'Lex', 'keel':'Inglise'})
# print(andmed)

#read = ['Mis on Python?:programmeerimiskeel', 'Eesti pealinn?:Tallinn']
#or
# import random
# read = ['Mis on Python?-programmeerimiskeel', 'Eesti pealinn?-Tallinn', 'Rootsi pealinn?-Stockholm']
# kus_vas = {}
# for rida in read:
#     kysimus, vastus = rida.split('-')
#     kus_vas[kysimus.strip()] = vastus.strip()
# print(kus_vas)
# print(kus_vas['Mis on Python?'])
# print(kus_vas['Eesti pealinn?'])
# kysimused = list(kus_vas.keys())
# while True:
#     n=random.randint(0, len(read)-1)
#     valitud_kysimus = kysimused[n]
#     print(valitud_kysimus)
#     vastus= input("Sisesta vatus: ")
#     if kus_vas[valitud_kysimus] == vastus.lower():
#         print("Õige vastus")
#     else:
#         print("Vale vastus")
# {'Mis on Python?': 'programmeerimiskeel',
from gtts import gTTS

from translator_functions import *

Dictionary = load_dictionary("Dictionary.txt")
# Dictionary = [
#     ["hello", "welcome", "thank you", "goodbye", "good", "sorry", "price"],
#     ["bonjour", "bienvenue", "merci", "au revoir", "bien", "désolée", "prix"],
#     ["Nǐ hǎo", "Huānyíng", "Xièxiè", "Zàijiàn", "Hǎo de", "Duìbùqǐ", "Jiàgé"]
# ]

Welcomeeng = "Welcome to the ENGLISH/FRENCH/CHINESE translator"
Welcomefra = "Bienvenue dans le traducteur ANGLAIS/FRANÇAIS/CHINOIS"
Welcomechi = "Huānyíng shǐyòng yīngyǔ/fǎyǔ/zhōngwén fānyì"

test_user_score = [[], []]

print(f"{Welcomeeng} / {Welcomefra} / {Welcomechi}")
print("_" * 20)
user = input(str("Please type your name: "))

while True:
    print("_" * 20)
    print("Options:")
    print("1. Translate word")
    print("2. Add word")
    print("3. Remove word")
    print("4. Edit word")
    print("5. Show all words")
    print("6. Show all words in English")
    print("7. Show all words in French")
    print("8. Show all words in Chinese")
    print("9. Test French-English")
    print("10. Show test score (current user)")
    print("11. Text to speech")
    print("12. Test Chinese-English")
    print("13. Exit")
    print("14. SAVE SCORES TO FILE")
    print("15. SHOW SCORE HISTORY")
    print("16. SAVE DICTIONARY TO FILE")
    print("_" * 20)

    try:
        choice = int(input("Enter your choice [select 1-13]: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        word = input("Enter the word to translate: ")
        print(translate_word(word, Dictionary))

    elif choice == 2:
        word = input("Enter the word to add: ")
        french_word = input("Enter the French translation: ")
        chinese_word = input("Enter the Chinese translation: ")
        print(add_word(word, french_word, chinese_word, Dictionary))

    elif choice == 3:
        word = input("Enter the word to remove: ")
        print(remove_word(word, Dictionary))

    elif choice == 4:
        word = input("Enter the word to edit: ")
        new_word = input("Enter the new word: ")
        new_french_word = input("Enter the new French translation: ")
        new_chinese_word = input("Enter the new Chinese translation: ")
        print(edit_word(word, new_word, new_french_word, new_chinese_word, Dictionary))

    elif choice == 5:
        for entry in show_all_words(Dictionary):
            print(entry)

    elif choice == 6:
        for word in show_words_by_language(Dictionary, 0):
            print(word)

    elif choice == 7:
        for word in show_words_by_language(Dictionary, 1):
            print(word)

    elif choice == 8:
        for word in show_words_by_language(Dictionary, 2):
            print(word)

    elif choice == 9:
        test_french(Dictionary, user, test_user_score)

    elif choice == 10:
        for line in show_scores(user, test_user_score, Dictionary):
            print(line)

    elif choice == 11:
        language= input("select language en/fr/chi: ")
        if language=="chi":
            language="zh-CN"
        word = input("Enter the word to convert to speech: ")
        print(text_to_speech(word, Dictionary, language))

    elif choice == 12:
        test_chinese(Dictionary, user, test_user_score)

    elif choice == 13:
        print("Exiting the program.")
        break

    elif choice == 14:
        save_scores("Score_Save.txt", test_user_score, Dictionary)
    elif choice == 15:
        history = show_score_history("Score_Save.txt")
        for line in history:
            print(line)

    elif choice == 16:
        save_dictionary ("Dictionary.txt", Dictionary)
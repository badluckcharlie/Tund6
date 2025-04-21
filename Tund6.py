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

Dictionary = [["hello","welcome","thank you","goodbye","good","sorry","price"],["bonjour","bienvenue","merci","au revoir","bien","désolée","prix"],["Nǐ hǎo","Huānyíng","Xièxiè","Zàijiàn","Hǎo de","Duìbùqǐ","Jiàgé"]]
Welcomeeng="Welcome to the ENGLISH/FRENCH/CHINESE translator"
Welcomefra="Bienvenue dans le traducteur ANGLAIS/FRANÇAIS/CHINOIS"
Welcomechi="Huānyíng shǐyòng yīngyǔ/fǎyǔ/zhōngwén fānyì"
test_user_score=[[],[]]
print(f"{Welcomeeng} / {Welcomefra} / {Welcomechi}")
print("_" * 20)
user=input(str("Please type your name: "))
while True:
    print("_" * 20)
    print("Options: ")
    print("1. Translate word")
    print("2. Add word")
    print("3. Remove word")
    print("4. Edit word")
    print("5. Show all words")
    print("6. Show all words in English")
    print("7. Show all words in French")
    print("8. Show all words in Chinese")
    print("9. Test French-English")
    print("10. Show test scores")
    print("11. Text to speech")
    print("12. Test Chinese-English")
    print("13. Exit")

    try:
        choice = int(input("Enter your choice [select 1-13]: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if choice == 1:
        word = input("Enter the word to translate: ")
        if word in Dictionary[0]:
            index = Dictionary[0].index(word)
            print(f"'{word}' in French is '{Dictionary[1][index]}' and in Chinese is '{Dictionary[2][index]}'.")
        else:
            print(f"The'{word}' is not in the dictionary.")
    elif choice == 2:
        word = input("Enter the word to add: ")
        french_word = input("Enter the French translation: ")
        chinese_word = input("Enter the Chinese translation: ")
        Dictionary[0].append(word)
        Dictionary[1].append(french_word)
        Dictionary[2].append(chinese_word)
        print(f"The word '{word}' has been added to the dictionary.")
    elif choice == 3:
        word = input("Enter the word to remove: ")
        if word in Dictionary[0]:
            index = Dictionary[0].index(word)
            Dictionary[0].pop(index)
            Dictionary[1].pop(index)
            Dictionary[2].pop(index)
            print(f"The word '{word}' has been removed from the dictionary.")
        else:
            print(f"The word '{word}' is not in the dictionary.")
    elif choice == 4:
        word = input("Enter the word to edit: ")
        if word in Dictionary[0]:
            index = Dictionary[0].index(word)
            new_word = input("Enter the new word: ")
            new_french_word = input("Enter the new French translation: ")
            new_chinese_word = input("Enter the new Chinese translation: ")
            Dictionary[0][index] = new_word
            Dictionary[1][index] = new_french_word
            Dictionary[2][index] = new_chinese_word
            print(f"The word '{word}' has been edited.")
        else:
            print(f"The word '{word}' is not in the dictionary.")
    elif choice == 5:
        print("All words in the dictionary:")
        for i in range(len(Dictionary[0])):
            print(f"{Dictionary[0][i]} - {Dictionary[1][i]} - {Dictionary[2][i]}")
    elif choice == 6:
        print("All words in English:")
        for word in Dictionary[0]:
            print(word)
    elif choice == 7:
        print("All words in French:")
        for word in Dictionary[1]:
            print(word)
    elif choice == 8:
        print("All words in Chinese:")
        for word in Dictionary[2]:
            print(word)
    elif choice == 9:
        print("Test:")
        score = 0
        for i in range(len(Dictionary[0])):
            print(f"Translate '{Dictionary[1][i]}' to English:")
            answer = input("Your answer: ")
            if answer.lower() == Dictionary[0][i].lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is '{Dictionary[0][i]}'.")
        print(f"Your score is {score}/{len(Dictionary[0])}.")
        test_user_score[0].append(user)
        test_user_score[1].append(score)
    elif choice == 10:
        print("Test scores:")
        try:
            with open("test_scores.txt", "r") as file:
                scores = file.readlines()
                for score in scores:
                    print(score.strip())
        except FileNotFoundError:
            print("No test scores found.")
    elif choice == 11:
        print("Text to speech:")
        word = input("Enter the word to convert to speech: ")
        if word in Dictionary[0]:
            print(f"Converting '{word}' to speech...")
            
        else:
            print(f"The word '{word}' is not in the dictionary.")
    elif choice == 13:
        print("Exiting the program.")
        break
    elif choice == 12:
        print("Test:")
        score = 0
        for i in range(len(Dictionary[0])):
            print(f"Translate '{Dictionary[2][i]}' to English:")
            answer = input("Your answer: ")
            if answer.lower() == Dictionary[0][i].lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is '{Dictionary[0][i]}'.")
        print(f"Your score is {score}/{len(Dictionary[0])}.")
        test_user_score[0].append(user)
        test_user_score[1].append(score)


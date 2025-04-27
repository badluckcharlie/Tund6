from encodings import utf_8_sig


def translate_word(word, dictionary):
    if word in dictionary[0] or dictionary[1] or dictionary[2]:
        if word in dictionary[0]:
            index = dictionary[0].index(word)
        elif word in dictionary[1]:
            index = dictionary[1].index(word)
        else:
            index = dictionary[2].index(word)
        return (f"'{word}' is found.\n"
            f"ENG: '{dictionary[0][index]}'\n"
            f"FRA: '{dictionary[1][index]}'\n"
            f"CHI: '{dictionary[2][index]}'.")
    else:
        return f"The word '{word}' is not in the dictionary."


def add_word(word, french_word, chinese_word, dictionary):
    dictionary[0].append(word)
    dictionary[1].append(french_word)
    dictionary[2].append(chinese_word)
    return f"The word '{word}' has been added to the dictionary."


def remove_word(word, dictionary):
    if word in dictionary[0]:
        index = dictionary[0].index(word)
        for lang in dictionary:
            lang.pop(index)
        return f"The word '{word}' has been removed from the dictionary."
    else:
        return f"The word '{word}' is not in the dictionary."


def edit_word(word, new_word, new_french_word, new_chinese_word, dictionary):
    if word in dictionary[0]:
        index = dictionary[0].index(word)
        dictionary[0][index] = new_word
        dictionary[1][index] = new_french_word
        dictionary[2][index] = new_chinese_word
        return f"The word '{word}' has been edited."
    else:
        return f"The word '{word}' is not in the dictionary."


def show_all_words(dictionary):
    return [f"{dictionary[0][i]} - {dictionary[1][i]} - {dictionary[2][i]}" for i in range(len(dictionary[0]))]


def show_words_by_language(dictionary, index):
    return dictionary[index]


def test_french(dictionary, user, test_user_score):
    score = 0
    for i in range(len(dictionary[0])):
        answer = input(f"Translate '{dictionary[1][i]}' to English:\nYour answer: ")
        if answer.lower() == dictionary[0][i].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{dictionary[0][i]}'.")
    print(f"Your score is {score}/{len(dictionary[0])}.")
    test_user_score[0].append(user)
    test_user_score[1].append(score)
    save_scores


def test_chinese(dictionary, user, test_user_score, score):
    score = 0
    for i in range(len(dictionary[0])):
        answer = input(f"Translate '{dictionary[2][i]}' to English:\nYour answer: ")
        if answer.lower() == dictionary[0][i].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{dictionary[0][i]}'.")
    print(f"Your score is {score}/{len(dictionary[0])}.")
    test_user_score[0].append(user)
    test_user_score[1].append(score)
    save_scores


def show_scores(user, test_user_score, dictionary):
    try:
        return [f"{test_user_score[0][i]}: {test_user_score[1][i]}/{len(dictionary[0])}" 
                for i in range(len(test_user_score[0]))]
    except FileNotFoundError:
        return ["No test scores found."]
    
    

def save_scores(file, test_user_score, dictionary):
    with open(file, "w", encoding="utf-8-sig") as f:
        for i in range(len(test_user_score[0])):
            f.write(f"{test_user_score[0][i]}: {test_user_score[1][i]}/{len(dictionary[0])}\n")
    print("Scores saved to file.")

def show_score_history(file):
    try:
        with open(file, "r", encoding="utf-8-sig") as f:
            scores = f.readlines()
            return [line.strip() for line in scores]
    except:
        return ["No score history found."]

def load_dictionary(file):
    dictionary = [[], [], []]
    try:
        with open(file, "r", encoding="utf-8-sig") as f:
            for line in f:
                eng, fra, chi = line.strip().split("|")
                dictionary[0].append(eng)
                dictionary[1].append(fra)
                dictionary[2].append(chi)
    except FileNotFoundError:
        print(f"Dictionary file '{file}' not found. Starting with empty dictionary.")
    return dictionary

def save_dictionary(file, dictionary):
    with open(file, "w", encoding="utf-8-sig") as f:
        for i in range(len(dictionary[0])):
            f.write(f"{dictionary[0][i]}|{dictionary[1][i]}|{dictionary[2][i]}\n")
    print("Dictionary saved to file.")


# from gtts import gTTS
# from playsound import playsound
# def text_to_speech(word, dictionary, language):
#     if word in dictionary[0] or dictionary[1] or dictionary[2]:
#         obj = gTTS(text=word, lang=language, slow=False)
#         failinimi = "heli.mp3"
#         obj.save(failinimi)
#         playsound(failinimi)
#     else:
#         print (f"The word '{word}' is not in the dictionary.")


    

# def loe_failist(fail:str)->list:
#     f=open(fail, "r", encoding="utf-8-sig")
#     jarjend=[]
#     for rida in f:
#         jarjend.append(rida.strip())
#     f.close()
#     return jarjend
# def kirjuta_failisse(fail:str, jarjend:list):
#     f=open(fail, "w", encoding="utf-8-sig")
#     for i in jarjend:
#         f.write(i+"\n")
#     f.close()
# loetelu=loe_failist("Score_Save.txt")
# print(loetelu)
# for i in range(8,11,1):
#     loetelu.append(input(f"{i}: "))
# kirjuta_failisse("Score_Save.txt", loetelu)
# loetelu=loe_failist("Score_Save.txt")

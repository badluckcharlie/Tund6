def translate_word(word, dictionary):
    if word in dictionary[0]:
        index = dictionary[0].index(word)
        return f"'{word}' in French is '{dictionary[1][index]}' and in Chinese is '{dictionary[2][index]}'."
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


def test_chinese(dictionary, user, test_user_score):
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


def show_scores():
    try:
        with open("test_scores.txt", "r") as file:
            scores = file.readlines()
            return [score.strip() for score in scores]
    except FileNotFoundError:
        return ["No test scores found."]

from gtts import gTTS
from playsound import playsound
def text_to_speech(word, dictionary, language):
    if word in dictionary[0] or dictionary[1] or dictionary[2]:
        obj = gTTS(text=word, lang=language, slow=False)
        failinimi = "heli.mp3"
        obj.save(failinimi)
        playsound(failinimi)
    else:
        return f"The word '{word}' is not in the dictionary."
    


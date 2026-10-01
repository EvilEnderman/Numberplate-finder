from english_words import get_english_words_set

english_words_set = get_english_words_set(['web2'], lower=True)
import random
import string

#Python Dictionary
cool_letters1 = {"R": "2", "A": "4", "I": "1", "E": "3", "S": "5", "G": "6", "T": "7", "B": "8", "P": "9"}
cool_letters2 = {
                 "OI": "01", "OR": "02", "OE": "03", "OA": "04", "OS": "05", "OG": "06", "OT": "07", "OB": "08",
                 "OP": "09", "IO": "10", "II": "11", "IR": "12", "IE": "13", "IA": "14", "IS": "15", "IG": "16",
                 "IT": "17", "IB": "18", "IP": "19", "RO": "20", "SI": "51", "SR": "52", "SE": "53", "SA": "54",
                 "SS": "55", "SG": "56", "ST": "57", "SB": "58", "SP": "59", "GO": "60", "GI": "61", "GR": "62",
                 "GE": "63", "GA": "64", "GS": "65", "GG": "66", "GT": "67", "GB": "68", "GP": "69", "TO": "70"
                 }


def generate_five_letter_plate():
    plates = []
    for word in english_words_set:
        if len(word) == 5:
            word_big = word.upper()
            if word_big[1] in cool_letters1.keys():
                word_big = list(word_big)
                word_big[1] = cool_letters1[word_big[1]]
                plates.append("".join(word_big))
    return plates


def generate_four_letter_plate():
    plates7 = []
    for word in english_words_set:
        if len(word) == 4:
            word_big = word.upper()
            appended = word_big[2:]
            if appended in cool_letters2:
                plates7.append(word_big[:2] + cool_letters2[appended])
    return plates7


if __name__ == "__main__":
    #ignore 5 letter plates as we only want the 4 letter starting data
    #with open("5LetterPlates.txt", "w") as f:
        #f.writelines("\n".join(generate_five_letter_plate()))

    with open("4LetterPlates.txt", "w") as f:
        f.writelines("\n".join(generate_four_letter_plate()))

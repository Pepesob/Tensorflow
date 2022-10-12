import pandas as pd
from random import randint

def del_known(word, known):
    word_local = word[:]
    i = 0
    output = ""
    while i < len(word_local):
        if i+len(known) <= len(word_local) and word[i:i+len(known)] == known:
            i += len(known)
        else:
            output += word_local[i]
            i += 1
    return output



def if_word_has_only_konwn(word, tab_known):
    word_local = word[:]
    for known in tab_known:
        word_local = del_known(word_local, known)
    return not bool(word_local)


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

data = pd.read_excel(io="jpn_words.xls",header=None)
row_length = len(data.index)

# a,e,i,o,u,ka,ki,ku,ke,ko if_word_has_only_known("kekkaku", "a,e,i,o,u,ka,ki,ku,ke,ko".split(sep=","))

known_char = input("Podaj znane ci głoski po przecinku: ")
known_char.split(sep=",")

while True:

    command = input("Kliknij 'ENTER' po nowy wyraz: ")
    if command.lower() == "q":
        quit()

    word = data.iloc[randint(0,row_length), 2]
    while not if_word_has_only_konwn(word,known_char):
        word = data.iloc[randint(0, row_length), 2]

    print(word,"\n")



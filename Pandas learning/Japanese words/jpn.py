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

# problem jest taki że czasem jak jest jakaś jedna sama zjebana spółgłoska niewiadomo skąd to potrafi połączyć się z
# samogłoską po usunięciu i rozjebać algorytm; rozwiązanie jest takie że dziele wyraz na tablice w ten sposób że
# wsadzam sylabę od samogłoski (wyłącznie) do samogłoski (włącznie)
def if_word_has_only_konwn(word:str, tab_known:list)->bool:
    word_local = word[:]
    for known in tab_known:
        word_local = del_known(word_local, known)
    return not bool(word_local)


def main():
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    data = pd.read_excel(io="jpn_words.xls", header=None)
    data.drop_duplicates(subset=[2], inplace=True)
    row_length = len(data.index)

    # a,e,i,o,u,ka,ki,ku,ke,ko if_word_has_only_known("kekkaku", "a,e,i,o,u,ka,ki,ku,ke,ko".split(sep=","))

    known_char = input("Podaj znane ci głoski po przecinku: ")
    known_char = known_char.split(sep=",")
    if known_char == ['']:
        quit()

    known_char.sort(key=lambda x: len(x), reverse=True)

    while True:
        command = input("Kliknij 'ENTER' po nowy wyraz: ")
        if command.lower() == "q":
            quit()

        r = randint(0, row_length - 1)
        word = str(data.iloc[r, 2])
        while not if_word_has_only_konwn(word, known_char):
            r = randint(0, row_length - 1)
            word = str(data.iloc[r, 2])
        print(word, end="    ")
        input()
        print(data.iloc[r,1],"\n")


def test():
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)

    data = pd.read_excel(io="jpn_words.xls", header=None)
    data.drop_duplicates(subset=[2], inplace=True)
    row_length = len(data.index)

    # a,e,i,o,u,ka,ki,ku,ke,ko,sa,shi,su,se,so,ta,chi,tsu,te,to,na,ni,nu,ne,no,ga,gi,gu,ge,go,za,ji,zu,ze,zo,da,ji,zu,de,do,ha,hi,fu,he,ho,ba,bi,bu,be,bo,pa,pi,pu,pe,po if_word_has_only_known("kekkaku", "a,e,i,o,u,ka,ki,ku,ke,ko,sa,shi,su,se,so".split(sep=","))

    known_char = input("Podaj znane ci głoski po przecinku: ")
    known_char = known_char.split(sep=",")
    if known_char == ['']:
        quit()

    known_char.sort(key=lambda x: len(x), reverse=True)

    for i in range(row_length):
        word = str(data.iloc[i, 2])
        if if_word_has_only_konwn(word, known_char):
            print(i, ", ", word, ", yes", sep="")
        else:
            print(i, ", ", word, ", no", sep="")


if __name__ == "__main__":
    main()
import random
import argparse
import os.path
import urllib.request

parser = argparse.ArgumentParser()
parser.add_argument('dictionary', action='store_true', default='https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt',  help='Put a link to some dictionary')
parser.add_argument('lengh', default=5, nargs='?', help='Choose the quantity of letters in the words', type=int)
args = parser.parse_args()

def bullscows(guess, secret):
    c=0
    b=0
    letters=[]
    for i in secret:
        for j in guess:
            if j==i and i not in letters:
                c+=1
                letters.append(i)
    for k1 in range(0, len(secret)):
        if guess[k1]==secret[k1]:
            b+=1
    return b, c

def ask(valid: list[str] = None):
    prompt=input("Введите слово: ")
    if valid:
        while prompt not in dict:
            print("Такое слово не подходит")
            prompt=input("Введите слово: ")
    return prompt

def inform(b, c):
    print("Быки: {", b, "}, Коровы: {", c, "}")

def gameplay():
    o=0
    b=0
    Sword=random.choice(dict)
    while b!=len(Sword):
        Gword=ask(dict)
        b, c = bullscows(Gword, Sword)
        inform(b, c)
        o+=1
    return o

dict = []
if os.path.exists(args.dictionary):
    with open(args.dictionary, 'r') as f:
        for line in f.readlines():
            word = line.strip()
            if len(word) == args.length:
                dict.append(word)
else:
    with urllib.request.urlopen(args.dictionary) as f:
        for line in f.readlines():
            word = line.decode('utf-8').strip()
            if len(word) == args.length:
                dict.append(word)
if len(dict) == 0:
        print('В выбранном словаре отсутствуют слова заданной длины')
else:
    print(gameplay())

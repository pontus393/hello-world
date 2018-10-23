# https://cloud.google.com/translate/docs/quickstart-client-libraries#client-libraries-install-python
# Använda Google's API för att hitta översättningar. Detta kostar pengar
# Använd istället googletrans men den buggar atm

from difflib import SequenceMatcher
import csv

# Creates a dictionary from .csv file with Danish and Swedish words
with open('danishswedish.csv', mode='r') as infile:
    reader = csv.reader(infile, delimiter=';')
    with open('danishswedish_dictionary.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[1]:rows[0] for rows in reader}

# Creates a ratio of spelling
def similar(a,b):
    return SequenceMatcher(None, a, b).ratio()

# Assess whether user knows the word.
def does_it_pass(ratio, danish, swedish):
    if ratio == 1:
        return "Perfect"
    elif ratio > 0.8:
        return "Almost, the correct spelling is {}".format(danish)
    else:
        return "Fail. The word '{}' in Danish is '{}'".format(swedish, danish)

def quiz():
    score = 0
    loops = 0
    for k, v in mydict.items():
        try:
            print("What's '{}' in Danish?".format(k))
            answer = input("-> ")
            print(does_it_pass(similar(v, answer), v, k))
            score += similar(v, answer)
            loops += 1
        except KeyboardInterrupt:
            print("You've canceled the program")
            break
    print("You're average score is {}".format(int((score/loops)*100)) + " %")

quiz()

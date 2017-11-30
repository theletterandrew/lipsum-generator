import random

words = ['and', 'tho', 'chisel', 'prediction', 'funnel', 'project']

def randomSentence(wordsList, numWords):
    sentence = ""
    for word in range(numWords):
        randomWord = random.choice(wordsList)
        if word == 0:
            randomWord = randomWord.title()
        sentence += randomWord + " "
        if word == numWords - 1:
            sentence += randomWord + "."
        else:
            sentence += randomWord + " "
    return sentence

testSentence = randomSentence(words, 12)

print(testSentence)

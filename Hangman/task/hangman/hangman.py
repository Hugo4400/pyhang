# Write your code here
import random
import string
from random_word import RandomWords


def find(letter: str):

    indexes = [x for x, v in enumerate(word) if v == letter]
    if not indexes:
        print("That letter doesn't appear in the word")
        return preview
    else:
        preview_replace = list(preview)
        for i in indexes:
            preview_replace[i] = letter
        return ''.join(preview_replace)


def verify(letter: str):

    if len(letter) != 1:
        print('You should input a single letter')
        return False

    if not letter.islower() or not letter.translate(string.punctuation).isalnum():
        print('Please enter a lowercase English letter')
        return False

    if letter in guesses:
        print("You've already guessed this letter")
        return False

    return True


print("H A N G M A N")

getout = False
while not getout:

    playstop = input('Type "play" to play the game, "exit" to quit:')

    if playstop == 'play':

        # RandomWords() breaks too often.
        # r = RandomWords()
        # word = r.get_random_word()

        words = ['pizza', 'beer', 'climbing', 'music', 'argentina', 'moracchini']
        word = words[random.randint(0, 3)]

        preview = '-' * (len(word))
        found = False
        guesses = set()
        nbguess = 0

        while not found and nbguess != 8:
            print('')
            guess = input("""{}
        Input a letter: """.format(preview))

            if not verify(guess):
                continue

            prepreview = preview
            preview = find(guess)

            if prepreview == preview:
                nbguess += 1

            guesses.add(guess)
            if preview == word:
                print("""{}
                
        You guessed the word!""".format(word))
                found = True


        if found:
            print("You survived!")
        else:
            print("You lost!")
        print("Thanks for playing!")

    elif playstop == "exit":
        getout = True

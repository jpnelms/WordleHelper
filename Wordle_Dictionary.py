# Wordle - Dictionary
#For when you cant figure out a Word

# Loading words
from pkg_resources import WorkingSet


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

size = input("How many letters? ")

if __name__ == '__main__':
    english_words = load_words()
    def by_size(english_words, size):
        return [word for word in english_words if len(word)== size]
    wordsL5 = by_size(english_words,size)

wordset = wordsL5
solved = 0  # Set to !0 to exit script

def guessfilter(wordset,guess,r):
    # Returns words based on guessed letters
    # l1,l2,... letter 1, letter 2, ... of guess
    # r1,r2,... result of letter guess
        # r1 = 0: Not contained
        # r1 = 1: Contained
        # r1 = 2: Correct
    for l in range(size):
        wordset_new = []
        if r[l] == 2:
            wordset = [word for word in wordset if word[l] == guess[l]]
        if r[l] == 1:
            for word in wordset:
                containscore = 0
                for letter in word:
                    if letter == guess[l]:
                        containscore = containscore + 1
                    else:
                        pass
                if containscore > 0:
                    wordset_new.append(word)
                    containscore = 0
            wordset = wordset_new
        if r[l] == 0:
            for word in wordset:
                containscore = 0
                for letter in word:
                    if letter == guess[l]:
                        containscore = containscore + 1
                    else:
                        pass
                if containscore <= 0:
                    wordset_new.append(word)
                    containscore = 0
            wordset = wordset_new
        #if r[l] == 0:
        #    wordset = [word for word in wordset if word[:] == guess[l]]
    return wordset

rounds = 1

while solved == 0:
    # Inside the outermost loop.
    guess = input("Enter guess:")
    while (len(guess) != size):
        print("Error - Incorrect Size")
        print("Redo - input:")
        guess = input("Enter guess:")
    while (len(guess) != size):
        print("Error - Incorrect Size")
        print("Redo - input:")
    r_str = input("Enter Guess Results (0-N,1-S,2-C):")
    r = []
    for ii in range(size):
        r.append(int(r_str[ii]))

    wordset = guessfilter(wordset,guess,r)    
    rounds = rounds + 1
    print("There are " + str(len(wordset)) + " words left:")
    if len(wordset) < 60:
        print(wordset)
    if wordset <= 1:
        solved = 1
    if rounds > 5:
        solved = 1


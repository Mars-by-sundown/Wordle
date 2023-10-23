#Nicholas Ragano
#10-23-2023
#used https://github.com/dwyl/english-words/words_dictionary.json for list of words
#allows user to narrow down list of possible words, does not account for frequency of use

import json, string

def load_words():
    fl = open('words_dictionary.json')
    valid_words_dict = json.load(fl) 
    valid_words = []
    for k in valid_words_dict.keys():
        if(len(k) == 5):
            valid_words.append(k)
    fl.close()
    return valid_words

def trimDict(wordList, guessedword, guessOutcome):
    twos = []
    for idx in range(len(guessedword)):
        if(guessOutcome[idx] == '2'):
            twos.append(guessedword[idx])
    print("twos", twos)
    for idx in range(len(guessedword)):
        #go through each letter, get its status
        #if 0, delete all words with that letter
        
        if(guessOutcome[idx] == '0'):
            if(guessedword[idx] not in twos):
                wordList = [word for word in wordList if (guessedword[idx] not in word)]

        #if 1 delete all words with that letter in that position
        if(guessOutcome[idx] == '1'):
            wordList = [word for word in wordList if ((guessedword[idx] in word) and (guessedword[idx] != word[idx]))]

        if(guessOutcome[idx] == '2'):
            wordList = [word for word in wordList if guessedword[idx] == word[idx]]

    return wordList
        #if 2 do nothing

if __name__ == '__main__':
    #load english words
    english_words = load_words()
    guessList = []
    letterStatus = dict.fromkeys(string.ascii_lowercase, -1)
    print(letterStatus)
    guessesLeft = 6

    while(guessesLeft > 0):
        print(f"Previous guesses: {guessList}")
        print(f"Guesses remaining: {guessesLeft}")
        guess = input('Enter your next guess\n').lower()
        guessList.append(guess)
        guessOutcome = str(input('Enter 5 digit result code, 0 = not in word, 1 = yellow, 2 = green, ex. 02210:'))
        if(guess == '22222'):
            guess == 0
        english_words = trimDict(english_words, guess, guessOutcome)

        print(english_words)
        guessesLeft -= 1
        
        

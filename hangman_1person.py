player = raw_input("Welcome player.  What is your name? ")
print "Hello {0}!  Welcome to hangman.".format(player)

with open('G:/Programming for Analytics/HW #1/words.txt','r') as words:
    words = words.read().split("\n")

import random

def word_info(words, word_list = [], current_revealed = []):
    word = random.choice(words)
    length = 0
    word_list[:] = []
    current_revealed[:] = []
    for i in word:
        length += 1
        word_list.append(i)
        current_revealed.append("*")
    print "The word has {0} letters: {1}.".format(length, ''.join(current_revealed))
    return word, length, word_list, current_revealed

def guessing(word, word_length, word_letter_list,current_revealed,letters_guessed = []):
    letters_guessed[:]=[]    
    wrong_guess_qty = 0    
    guess_qty = 0
    while wrong_guess_qty < 6:
        guess_qty += 1
        guess_letter = raw_input("{0}, please enter your letter for guess # {1}: ".format(player,guess_qty))
        guess_letter = guess_letter.lower()
        letters_guessed.append(guess_letter)        
        checking_letter_in_word = 0
        correct_letter = False
        for letter_in_word in word_letter_list:
            if guess_letter == letter_in_word:
                current_revealed[checking_letter_in_word] = letter_in_word
                correct_letter = True
            checking_letter_in_word += 1
        if(correct_letter == False):
            wrong_guess_qty += 1
            guesses_left = 6 - wrong_guess_qty
            print "That letter is not in the word.  That is wrong guess # {0}, you have {1} guesses left.".format(wrong_guess_qty, guesses_left)
        current_missing = 0
        for x in current_revealed:
            if x == "*":
                current_missing += 1
        if current_missing != 0:
            print "So far you have successfully guessed {0}.  You have guessed the following letters: {1}".format(''.join(current_revealed),letters_guessed)
        else:
            print "You successfully guessed the word {0} in {1} guesses!  Congrats!".format(word,guess_qty)
            points2guesser = True
            break
    else:
        print "Sorry, you lost that round.  The word was {0}.  Better luck next time.".format(word)
        points2guesser = False
    return points2guesser

current_rnd = 0
wins = 0

def games(current_rnd,wins):
    current_rnd += 1
    print "Welcome to round {0}.  So far you have won {1} games.".format(current_rnd, wins)
    word, word_length, word_letter_list, current_revealed = word_info(words)
    points2guesser = guessing(word, word_length, word_letter_list,current_revealed)
    if points2guesser == True:
        wins += 1
        "That is the end of round {0}.  So far you have {1} wins.".format(current_rnd,wins)
    another_game = raw_input("Do you want to play another round (y/n)? ")
    another_game = another_game.lower()
    if(another_game == 'yes'):
        another_game = 'y'
    if another_game == 'y':
        games(current_rnd,wins)
    else:
        print "Thanks for playing!"

games(current_rnd,wins)

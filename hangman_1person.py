player = raw_input("Welcome player.  What is your name? ") #Initiate game, by asking who is playing
print "Hello {0}!  Welcome to hangman.".format(player)

with open('G:/Programming for Analytics/HW #1/words.txt','r') as words: #import word file that will be pulled from
    words = words.read().split("\n")

import random

def word_info(words, word_list = [], current_revealed = []): #function to pick a word from the word document to use in the game, and sets up the word for use
    word = random.choice(words) 
    length = 0
    word_list[:] = []
    current_revealed[:] = []
    for i in word: #creates a list of the letters in the word, and creates a list to show what letters have been guessed correctly, with a placeholder (*) for letters that haven't been guessed
        length += 1
        word_list.append(i)
        current_revealed.append("*")
    print "The word has {0} letters: {1}.".format(length, ''.join(current_revealed))
    return word, length, word_list, current_revealed

def guessing(word, word_length, word_letter_list,current_revealed,letters_guessed = []): #guessing function
    letters_guessed[:]=[]    #no guesses have occured yet
    wrong_guess_qty = 0    #initially no wrong guesses for round
    guess_qty = 0 #initially no guesses for round
    while wrong_guess_qty < 6: #total of 6 guesses allowed, once they reach 6 guesses the game is over and they lost
        guess_qty += 1
        guess_letter = raw_input("{0}, please enter your letter for guess # {1}: ".format(player,guess_qty)) #requests letter guess
        guess_letter = guess_letter.lower() #capitalization does not matter, thus make all guesses lower
        letters_guessed.append(guess_letter)    #adds guessed letter to the list of guessed letters    
        checking_letter_in_word = 0 
        correct_letter = False 
        for letter_in_word in word_letter_list: 
            if guess_letter == letter_in_word:
                current_revealed[checking_letter_in_word] = letter_in_word #replace placeholder in revealed list with actual letter
                correct_letter = True
            checking_letter_in_word += 1 #increases position to check further in the word for the guessed letter
        if(correct_letter == False): #increases qty of wrong guesses, lets player know howmany guesses are in the word
            wrong_guess_qty += 1
            guesses_left = 6 - wrong_guess_qty
            print "That letter is not in the word.  That is wrong guess # {0}, you have {1} guesses left.".format(wrong_guess_qty, guesses_left)
        current_missing = 0
        for x in current_revealed: #checks how many letters in word still need to be guessed
            if x == "*":
                current_missing += 1
        if current_missing != 0: #if all letters have been revealed/guessed then inform player they won, and what the word was, otherwise lets player know what letters they successfully guessed and what all of their guesses are
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

def games(current_rnd,wins): #starts a game, letting the player know how many rounds they have played and how many they won.  Once a game is complete, it asks if they want to play again
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

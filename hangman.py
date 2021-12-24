import random

def play_again():
    response = input('Would you like to play again?? y/n ').lower()
    if response == 'y':
        game_run()
    else:
        print('Thanks!!!!')

def getWord():
    with open ('dictionary.txt') as f:
        words = f.read().split(",")
    return random.choice(words).upper()

def scaff(lives):
	if (lives == 6):
		print ("_________")
		print ("|	 |")
		print ("|")
		print ("|")
		print ("|")
		print ("|")
		print ("|________")
	elif (lives == 5):
		print ("_________")
		print ("|	 |")
		print ("|	 O")
		print ("|")
		print ("|")
		print ("|")
		print ("|________")
	elif (lives == 4):
		print ("_________")
		print ("|	 |")
		print ("|	 O")
		print ("|	 |")
		print ("|	 |")
		print ("|")
		print ("|________")
	elif (lives == 3):
		print ("_________")
		print ("|	 |")
		print ("|	 O")
		print ("|	\|")
		print ("|	 |")
		print ("|")
		print ("|________")
	elif (lives == 2):
		print ("_________")
		print ("|	 |")
		print ("|	 O")
		print ("|	\|/")
		print ("|	 |")
		print ("|")
		print ("|________")
	elif (lives == 1):
		print ("_________")
		print ("|	 |")
		print ("|	 O")
		print ("|	\|/")
		print ("|	 |")
		print ("|	/ ")
		print ("|________")
	elif (lives == 0):
		print ("_________")
		print ("|	 |")
		print ("|	 O")
		print ("|	\|/")
		print ("|	 |")
		print ("|	/ \ ")
		print ("|________")

def game_run():
    alphabet = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    word = getWord()
    letters_guessed= []
    lives = 7
    guessed = False
    print()
    print('The word contains', len(word), 'letters')
    print(len(word) * ' _')

    while guessed == False and lives > 0:
        print('\nYou have total ' + str(lives) + ' lives') 
        guess = input('Guess a letter in the word : ').upper()
        if len(guess) == 1 :
            if guess not in alphabet:
                print('You are yet to enter a letter. Check your entry, make sure you enter an alphabet not a number')
            elif guess in letters_guessed:
                print("You have already guessed that letter before. Try again!")
            elif guess not in word:
                print('Sorry, that letter is not part of the word')
                letters_guessed.append(guess)
                lives -=1
                scaff(lives)
            elif guess in word:
                print('Great! That letter exists in the word!')
                letters_guessed.append(guess)
            else:
                print('Check your entry! You might have entered the wrong entry...')
        else:
            print('The length of your guess is not the same as the length of the correct word.')
            lives -=1
            scaff(lives)

        status = ''
        if guessed == False:
            for letter in word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += ' _'
            print (status)

        if status == "".join(word):
            print('\nGreat Job! You guessed the word correctly!')
            guessed = True
        elif lives == 0:
            print("The word is ", word)
            print('\nOpps! You ran out of lives\nYou hanged a nice man!!!!\n')
    play_again()
game_run()
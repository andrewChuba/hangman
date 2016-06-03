from random import *

word = 'practice' #the word that we have chosen randomnly 
lettersguessed = [] #the letters that have been guessed so far
answer = [] #the current word with the letters the user has guessed
mistakes = 0 #number of guesses allowed

print ("Hello! Welcome to Hangman")
print ("Type 'used' if you would like to see the letters already used")
hiddenword = ''
content = []
with open("wordsEn.txt") as f:
    content = f.readlines()

rando = randint(0,len(content))
word = content[rando]
for x in range (0, len(word)-2):
	hiddenword = hiddenword + '_ '
	answer.append('_')
print("Your word is " + hiddenword)

def printImg(pid):
    path = './images/%s.txt'%pid
    image=""
    with open(path) as f:
        image = f.read()
    print(image)

def printAnswer(answer):
	answerToPrint = ''
	for x in range (0, len(answer)):
		answerToPrint = answerToPrint + answer[x] + ' '
	print(answerToPrint)

def validGuess(guess, lettersguessed):
	if ((not guess.isalpha()) or (not lettersguessed.count(guess) == 0) or (not len(guess)) == 1):
		return False
	return True

def checkletter(word, answer, mistakes):
	returnValue = 0
	guess = raw_input("Please, type in the letter you would like to guess: ")

	if guess == 'used':
		print "Guessed: ",
		for letter in lettersguessed:
			print letter,
		print ""
		return 0
	else:
		#Get a valid guess 
		while not validGuess(guess, lettersguessed):
			print("You made in invalid guess, you may have guessed the letter before")
			guess = raw_input("Try again: ")

	#see if the letter is in the word
	i = 0
	found = False
	while i < len(word):
		if word[i] == guess:
			answer[i] = guess;
			found = True
		i = i + 1

	#print out new pattern
	if found:
		print("Your guess was correct!")
	else:
		print("Your guess was incorrect!")
		returnValue = 1
	lettersguessed.append(guess)
	printAnswer(answer)	
	return returnValue	
		
while (answer.count('_') > 0 and mistakes < 6):	
	printImg(mistakes)
	mistakes = mistakes + checkletter(word, answer, mistakes)
if answer.count('_') > 0:
	print ("You lost!!!!!!!!")
	print ("Correct word is: %s"%word)
else:
	print ("You won!!!!!!!!!")


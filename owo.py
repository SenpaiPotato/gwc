import random

# A list of words that 
potential_words = ["nootnoot", "hedgehog"]

word = random.choice(potential_words)

# Use to test your code:
# print(word)  

# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word = ["_", "_", "_", "_", "_", "_", "_", "_"] # TIP: the number of letters should match the word
word = list(word)

# Some useful variables
guesses = []
maxfails = 20
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")

	# check if the guess is valid: Is it one letter? Have they already guessed it?
	if guess in word:
		for i in range(0, 8):
			if guess == word[i]:
				current_word[i] = guess

		print(current_word)
		print("correct")
	if current_word == word:
		print("all correct")
		quit()
	# check if the guess is correct: Is it in the word? If so, reveal the letters!
	if guess not in current_word:
		fails = fails+1
		print("You have " + str(maxfails - fails) + " tries left!")
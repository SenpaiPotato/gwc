import random
# --- Define your functions below! ---
def introduction():
    acceptable_answers = ["hey", "hello", "hi", "holla", "what's up"]
    answer = input("Hello? ")
    if answer in acceptable_answers:
        print("I am nani nice to meet you ")
    else:
        print("That's cool!")
        
def rock_paper_scissors():
    answer = input("Rock, Paper, or Scissors? ")
    choices = ["rock", "scissors", "paper"]
    word = random.choice(choices)
    done = False
    while done is not True:    
        if answer == word:
            print("I choose" + word)
            answer = input("Try Again ")
        elif answer == "rock" and word == "scissors":
            print("I choose " + word)
            print("you win ")
            done = True
        elif answer == "paper" and word == "scissors":
            print("I choose " + word)
            print("you lose")
            done = True 
        elif answer == "rock" and word == "paper":
            print("I choose " + word)
            print("you lose")
            done = True
        elif answer == "scissors" and word == "paper":
            print("I choose " + word)
            print("you win")
            done = True
        elif answer == "scissors" and word == "rock":
            print("I choose " + word)
            print("you lose")
            done = True
        elif answer == "paper" and word == "rock":
            print("I choose " + word)
            print("you win")
            done = True
        else:
            answer = input("Try again, rock, paper, or scissors? ")
            done = False

def goodbye():
    print("goodbye")
    print(" (\_/)")
    print(" |. .|")
    print("=\_T_/=")
    print(" /   \ .-.")
    print(" | _ |/")     
    print("/| | ||")
    print("\)_|_(/")
   


   
# --- Put your main program below! ---
def main():
  while True:
    introduction()
    response = input("would you like to play rock, paper, scissors? ")
    if response == "yes":
        rock_paper_scissors()
    if response == "no":
        exit()
        
    goodbye()
    exit()

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
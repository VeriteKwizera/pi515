# Unit 1 Guessing Game
# 1. Import the random module
# 2a. Create a boolean variable to indicate rounds of the game and a while loop using that boolean
# 2b. Create a variable that stores the result of input provided by the user, ask them to - "Type a number for an upper bound: "
# 3a. Check if a valid number was entered using an if statement
# 3b. If it is a valid number, print "Let's play!" and set the boolean variable to False
# 3c. "Scrub" the value of the entered number, by setting it to an int 
# 3d. Write the else condition and give the user an error message

# TEST IT OUT AND SEE WHAT HAPPENS WITH DIFFERENT INPUTS

# 4. Generate a random number from the range 1 to the number the user entered, make sure it is outside your while loop - known as a global variable
# 5. Create two more variables - one for the guess and one for the count of guesses 
# 6a. Create a new while loop below these variables that runs while the guess vairable is not equal to the random number
# 6b. Update the guess variable with input from the user, prompt them by saying "Type a number between 1 and" add the number they orginally entered
# 7. Verify the guess is a number (like before) and if it is, update the guess variable to be the value of itself as an int
# 8. Check it! Make an if else statement to see if guess equals the random number, if it does tell the user they won! If it does not, update the guess count number by 1
# 9. Let the user know how many guesses it took.  Print a message using the guess count number - make sure it makes sense no matter what the number is
# 10. Make the game playable more than once, add a while loop around all of your code
# import random

# name = input("Type Name, ")
# boolean = True
# while boolean:
#   minNum = input ("Type a number for a lower bound: ")
#   maxNum = input (str(name) + ", Type a number for an upper bound: ")
#   if maxNum.isdigit() & minNum.isdigit():
#     print("Let's play!")
#     upperBound = int(maxNum) 
#     lowerBound = int(minNum)
#     boolean = False
    
#   else: 
#     print("Not a digit")
#   secret = random.randrange(lowerBound,upperBound)
#   guess = None
#   count = 0
# while guess != secret:
#   guess = input("Type a number between" + str(lowerBound) + " and " + str(upperBound) + ":")
#   if guess. isdigit():
#     guess = int(guess)
#     count +=1
#   if guess == secret:
#     print(f"{username} got it!")
#   else: 
#     print("Try again.")
# if count == 1:
#    print("It took you",count, "guess!")
# else: 
#   print("It took you", count, "guesses!")


# candyList = ["gummy bears", "sour patch", "m&m", "skittles"]
    
# i = 1
# for candy in candyList:
#   if i == 3:
#     print (candy)
#     continue
#   i += 1
import random 
computer_count = 0
user_input_count = 0
count = 1
username = input("Enter username: ")
next_game = True
while next_game is True:
  
  user_input = ""
  list = ["rock", "paper", "scissors"]
  computer = random.choice(list) 
  # print(computer)
  while user_input not in list:
    user_input = input ("Type, rock, paper or scissors: ").lower()
  
  if computer == user_input:
    print("Draw")
  elif user_input == "rock":
    if computer == "paper":
      print(f"{username} lost")
      computer_count +=1
    else:
      print(f"{username} won!")
      user_input_count +=1
  
  elif user_input == "paper":
    if computer == "scissors":
        print(f"{username} lost")
        computer_count += 1
    else:
        print(f"{username} won!")
        user_input_count +=1
  
  else:
    if computer == "rock":
        print(f"{username} lost")
        computer_count +=1
    else:
        print(f"{username} won!")
        user_input_count +=1
  # next_game_list = ["yes", "no"]  
  # answer = input("Do you want to play again").lower()
  # if answer == "yes": 
  #   next_game = True
  # else: 
  #   next_game = False
  print("computer count = " + str(computer_count)) 
  print("user count" + str(user_input_count))
  if computer_count <2 and user_input_count < 2:
    next_game = True
  else:
    next_game = False


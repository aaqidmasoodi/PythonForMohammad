# Create a guessing game
'''
    keep asking for input and if they don't enter the target value
    just keep promting them 
'''

target = 7

user_guess = int(input("What's your guess? ")) # loop variable

while user_guess != target: # condition
    print("That's not the correct number!")
    # user_guess = int(input("What's your guess again? ")) # updation of the loop variable
 
print("Nice! you got it.")

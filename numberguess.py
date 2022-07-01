# Lucas Chang
# This program is a number guessing game. 
def main(): # Main function
    running = 'y' # While this condition is met the commands in the block (the game) executes
    while running == 'y' or running == 'Y' or running == 'yes' or running == 'Yes':
        print('Welcome to the Number Guessing Game!') # intro to the player to start the game
        input('Press ENTER to Begin.')
        random_num = random() # calling on the random function
        game(random_num) # calling the game function, the purpose of this function is defined below
        odd_or_even(random_num) # calling function to determine if the value is even or odd.
        running = input('Would you like to play the game again? ')
    else: # If the user enters something other than y or Y or yes or Yes the condition isn't met and the program quits
        print('You have quit the game')
def random():# The random function generates a nuber between 1 and 10 and returns the value back to main
    import random
    number = random.randint(1,10)
    return number
def game(random_num): # This function tells the user to input value until they get the correct value, that is
    tries = 0 # the value equal to the randomly generated number. Upon guessing correctly, num value is returned to main
    guess = int(input("I'm thinking of a number between 1 and 10. Take a guess: "))
    tries += 1
    while guess != random_num: # The loop will repeat until the user enters the correct guess
        if guess < random_num:
            print('That guess is incorrect! Too low! Try again')
            guess = int(input('Take another guess: '))
        elif guess > random_num:
            print('That guess is incorrect! Too high! Try again')
            guess = int(input('Take another guess: '))    
    else: 
        print(f'You have guessed the correct number in {tries} tries!')
def odd_or_even(number): # Function to determine whether the number was even or odd
    if number % 2 == 0: # using remainder division in order to determine even or odd
        print(f'Your guess {number} is even')
    else:
        print(f'Your number {number} is odd')
main()  # calling the main function
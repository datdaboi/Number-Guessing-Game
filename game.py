import random

print("==========================")
print("      Welcome to the      ")
print("   Number Guessing Game   ")
print("==========================")

while True:
    print("\nPlease select difficulty!\n1. Easy (10 guesses)"
          "\n2. Medium (5 guesses)\n3. Hard (3 guesses)")
    
    difficulties = ['easy', 'medium', 'hard']
    
    diff = input("\nInput difficulty level: ")
    
    if diff in ['quit', 'q', 'x', 'exit']:
        break
    
    try:
        diff = int(diff)
    except ValueError:
        print("Please insert a valid number! (1, 2 or 3)")
        continue
    
    if diff == 1:
        guesses = 10
    elif diff == 2:
        guesses = 5
    elif diff == 3:
        guesses = 3
    else:
        print("Please insert a valid number! (1, 2 or 3)")
        continue
    
    print(f"\nYou have chosen the {difficulties[diff-1]} difficulty!"
          f"\nYou have {guesses} chances.")
    
    if diff == 3:
        print("You get no hints when you guess wrong.")
    else:
        print("You get hints when you guess wrong.")
        
    num = random.randint(1, 100)
    
    print("\nI'm thinking of a number between 1 and 100.\n"
          "Can you guess what number it is?\n")
    
    while guesses > 0:
        guess = input("Guess what the number I'm thinking of is: ")
        
        if guess in ['quit', 'q', 'x', 'exit']:
            break
        
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number!")
            continue
        
        if guess < 1 or guess > 100:
            print("Out of bounds.\nI'm thinking of a number between 1 and 100.")
            continue
        
        if guess == num:
            print(f"Correct! I was thinking of {num}")
            break
        else:
            print("\nOops! Not quite!")
            guesses -= 1
            print(f"You have {guesses} attempts left.")
            
            if diff == 1 or diff == 2:  # don't give hints in hard mode
                if guess > num:
                    print("Your guess was too high.")
                else:
                    print("Your guess was too low.")
    
    if guesses == 0:
        print("Game over!", f"\nI was thinking of {num}.\n")
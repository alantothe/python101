import random
from capitals import states

random.shuffle(states)

def game():
    correct = 0
    incorrect = 0

    for state in states:
        answer = input(f"What is the capital of {state['name']}? ")
        
        if answer == str(state['capital']):
            correct += 1
            print("Correct!")
            print(f"You have {correct} correct and {incorrect} incorrect answers.")
        else:
            incorrect += 1
            print("Incorrect!")
            print(f"Correct: {correct} Incorrect:  {incorrect}")

    print(f"Game over! You got {correct} correct and {incorrect} incorrect answers.")

while True: 
    print("Greetings! How well do you know the geography of the United States?")
    print("Guess the capitals of each state and test your knowledge!")
    game()
    
    replay = input("Would you like to play again? (yes/no): ")
    if replay.lower() != 'yes':
        break

    

   
    
    
    


import random
from PyDictionary import PyDictionary

dictionary = PyDictionary()
print("Let's begin Hangman Game...", end='\n\n')

# Choosing a random word from 'word.txt'
def get_word():
    global word
    random_no = random.randint(1,850)
    with open('words.txt','r') as f:
        lines = f.readlines()
        word = lines[random_no]
        word = word.replace('\n','')

def create_guess_word():
    global guess
    guess = list('_'* len(word)) 
    # Filling ~1/3 of the word
    for _ in range(len(word)//3): 
        r_no = random.randint(0,len(word)-1)
        guess[r_no] = word[r_no]

def print_hint():
    print('Hint: ')
    try:
        hint_dict = dictionary.meaning(word) 
        hint = [j[0].replace(word,'*') for j in hint_dict.values()]
        print(*hint, sep='\n')
    except Exception as e:
        print('Sorry! Hint is not available.')

def win():
    global points
    print('\nYou guessed it right ',word, sep='=> ')
    points += attempts

points = 0

while True:
    print(f'You have {points} points.', end='\n\n')
    attempts = 5  
    get_word()     
    print_hint()   
    create_guess_word()

    while attempts>0:
        # If the word is complete
        if '_' not in guess:
            win()
            break

        print(f"\nAttempts = {attempts}/5")
        print(" ".join(guess))  # For better readabilty

        letter = input("Guess a letter: ")
        
        if letter==word:
            win()
            break

        # Flag: Has user made a right guess.. By default NO
        flag= False
        for i in range(len(word)):
            if word[i]==letter:
                guess[i] = letter
                flag = True  

        # Reduce the no of attempts by 1, if user made a wrong guess.
        if not flag: attempts-=1
        if attempts == 0:
            print('Better Luck next time:)',word)
            break
    print('-'*30, end='\n\n')

        


    








import random
from Day7_hangman_game_words import words_list
from Days_hangman_game_image import logo,stages
lives = 6
print(logo)
chosen_word = random.choice(words_list)
print(chosen_word) # This print statement is to check the code output and for my understanding.
placeholder = '_'
word_position = len(chosen_word)
for letter in chosen_word:
    placeholder += '_'
print(f'Word To Guess : {placeholder}')
game_over = False
correct_letter =[]
while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input('Guss The Word: ').lower()
    if guess in correct_letter: 
        print(f'You already guess the letter {guess}')
    display =''
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display +='_'
    print(f'Word to guess: {display}')
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    if lives == 0:
        game_over = True
        print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
    if '_' not in display:
        game_over = True
        print('You Win')
        print("****************************YOU WIN****************************")
    print(stages[lives])
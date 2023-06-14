import random
import hangman_words as words
import hangman_art as art


blanks = []
lives_remaining=7

print (art.logo)
chosen_word = random.choice(words.word_list)
word_length = len(chosen_word)
print(chosen_word)
for _ in range(word_length):
    blanks+="_"
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in blanks:
        print("ERROR: You already entered this letter.")   
    for position in range (word_length):
        letter=chosen_word[position]
        if guess == letter:
            blanks[position] = letter

    if guess not in chosen_word: 
        lives_remaining-=1
        print(art.stages[lives_remaining] + "\n")
        print(f"INCORRECT! The letter {guess} is not in the word! You have {lives_remaining} lives remaining!\n Try again.\n")
    print(blanks)

    if "_" not in blanks:
        end_of_game = True
        print("YOU WON??? WHY???? NOW HE HAS TO GO HOME TO HIS FAMILY AND FUFILL ALL HIS RESPONSIBILTIES ;-;")

    elif lives_remaining==0:
        end_of_game=True
        print("GAME OVER!!!! YOU KILLED HIM, WHY????? NOW HIS KIDS WON'T EVER SEE HIM AGAIN ;_;")
        
    
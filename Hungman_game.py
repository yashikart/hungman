import random
from replit import clear
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word=["avenue","gossip","transcript","zipper"]
chosen_word=random.choice(word)
print("Choosen word:",chosen_word)
display=[]
for _ in range(len(chosen_word)):
  display+="_"
print(display)
lives=6
end_game=False
while not end_game:
  Guess=input("Guess Word: ").lower()
  clear()
  for position in range(len(chosen_word)):
    letter=chosen_word[position]
    if Guess==letter:
      display[position]=letter
      
       
  print(f"{display}")
 
    
  if Guess not in chosen_word:
     print(stages[lives]) 
     lives-=1
     print(f"{Guess} is not in the word")
  else:
    print(f"{letter} is matched ")
  if lives==0:
    end_game=True
    print(f"You Lose..correct word is {chosen_word}")
      
  if "_" not in display:
    end_game=True
    print("You win")

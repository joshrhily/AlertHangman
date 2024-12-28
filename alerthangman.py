import random as rd
import os
import sys

#Access Word Bank (Names of cameras & vocabulary from www.alertwest.live)
basePath = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
filePath = os.path.join(basePath, "alertwords.txt")

with open(filePath, 'r') as file:
  words = [line.strip() for line in file]

# Game Data
wordCount = len(words) - 1
lives = 6
lifeCap = 12
winStreak = 0
game = True

def clearScreen():
  os.system('cls' if os.name == 'nt' else 'clear')

while game == True:
  randomWord = rd.randint(0, wordCount)
  gameWord = words[randomWord].upper()
  
  # String representation of redacted word
  blank = ''
  for i in gameWord:
    if i == " ":
      blank += " "
    elif i == "-":
      blank += "-"
    else:
      blank += "_"
  
    # Word bank to store entered letters
    guessed = []

  while lives > 0:
    clearScreen()
    print(f"Lives: {lives} (Cap: {lifeCap})")
    print(f'Win Streak: {winStreak}')
    print(f'Guessed Letters: {guessed}')
    guess = str(input(f"Your word is: {blank}\nEnter a character or guess the word: ")).upper()
    if guess == gameWord:
      clearScreen()
      blank = gameWord
      print(f'You guessed correctly! The word was {gameWord}!')
      winStreak += 1
      break
    else:
      # Updates redacted word with guessed letters if found in gameWord;
      if guess in gameWord and len(guess) == 1:
        idx = [i for i, char in enumerate(gameWord) if char == guess]
        for i in idx:
          blank = blank[:i] + guess + blank[i+1:]
      # Ensures one character is guessed if guessed word is not gameWord
      elif len(guess) != 1:
        input("Enter a single character or guess the word. Press <enter> to continue.")
      else:
        # Updates guessed bank to display to player
        if guess not in guessed:
          lives -= 1
          guessed.append(guess)
          if lives == 0:
            clearScreen()
            print(f"Game Over! The word was: {gameWord}")
            winStreak = 0
        else:
          input(f'Already guessed: {guess}')

    # Handles win condition if won by guessing last letter
    if blank == gameWord:
      clearScreen()
      winStreak += 1
      print(f'You got the word! The word was {gameWord}!')
      break
 
  # Prompts to play again
  guess = str(input("Would you like to continue? (Y/N)")).upper()
  if guess == 'N':
    game = False
  else:
    if lives < 6:
      lives = 6
    if (winStreak >= 5 and winStreak % 5 == 0):
      # Logic to ensure lives do not go over 12
      diff = lifeCap - lives
      if (lives + diff) > lifeCap or diff == 0:
        input("5 wins in a row!")
        lives = lifeCap
      else:
        input(f"5 wins in a row! +{diff} lives!")
        lives += diff

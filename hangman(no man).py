#seven mistakes
from getpass import getpass
import os

os.system('clear')

# to make it in a function


def clear():
  os.system('clear')


word = input("Input your word: ")

clear()
blank = list("_" * len(word))

mistakes = 0

print(''.join(map(str, blank)))
print("Mistakes: " + str(mistakes))

while mistakes < 7:
  guess = input("Guess: ")
  clear()
  if word.find(guess) != -1:
    counter = -1
    for char in word:
      counter += 1
      if char == guess:
        blank.insert(counter, guess)
        blank.pop(counter + 1)
      else:
        None
    #blank.insert(re.findall(guess), guess)
    #blank.pop(word.find(guess) + 1)
  else:
    mistakes += 1
  check = 0
  for char in blank:
    if char != "_":
      check += 1
      if check == len(word):
        print("The word was: " + word)
        print('Guesser Wins!')
        exit()
    else:
      None

  print(''.join(map(str, blank)))
  print("Mistakes: " + str(mistakes))
  if mistakes == 7:
    print("The word was: " + word)
    print("Executioner Wins!")
    exit()

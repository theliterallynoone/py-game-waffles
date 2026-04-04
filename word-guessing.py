import random
import sys

if not sys.stdin.isatty():
  print(
    'This game needs an interactive terminal.\n'
    'In Cursor/VS Code: open Terminal (Ctrl+`), then run:\n'
    '  python word-guesssing.py\n'
    'Do not use the Run button if typing does not work.'
  )
  sys.exit(1)

word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']
word = random.choice(word_bank)
guessedword = ['_'] * len(word)
attempts = 6
while attempts > 0:
  print('\nCurrent word: ' + ' '.join(guessedword), flush=True)

  guess = input('Guess a letter: ').strip().lower()

  if len(guess) != 1 or not guess.isalpha():
    print('Please enter a single letter.', flush=True)
    continue

  if guess in word:
    for i in range(len(word)):
      if word[i] == guess:
        guessedword[i] = guess
    print('Great guess!', flush=True)
  else:
    attempts -= 1
    print('Wrong guess! Attempts left: ' + str(attempts), flush=True)

  if '_' not in guessedword:
    print('\nCongratulations!! You guessed the word: ' + word, flush=True)
    break

if attempts == 0 and '_' in guessedword:
  print('\nYou\'ve run out of attempts! The word was: ' + word, flush=True)

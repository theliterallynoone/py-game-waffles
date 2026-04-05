import random
import streamlit as st

st.set_page_config(page_title='Word Guessing Game', page_icon='🎮')

if 'word' not in st.session_state:
  st.session_state.word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']
  st.session_state.word = random.choice(st.session_state.word_bank)
  st.session_state.guessedword = ['_'] * len(st.session_state.word)
  st.session_state.attempts = 6
  st.session_state.message = ''
  st.session_state.game_over = False

st.markdown(
  """
  <style>
  body {
    background-color: #f0f0f0;
    font-family: 'Arial', sans-serif;
    color: #333;
    text-align: center;
    padding: 20px;
  }
  .stTextInput input {
    font-size: 18px;
    padding: 10px;
    width: 200px;
    margin-top: 20px;
  }
  </style>
  """,
  unsafe_allow_html=True
)

st.header('Welcome to the Word Guessing Game!')
st.write('Try to guess the word by entering one letter at a time. You have 6 attempts!')
st.write('Current word: ' + ' '.join(st.session_state.guessedword))
st.write('Attempts left: ' + str(st.session_state.attempts))

with st.form('guess_form'):
  guess = st.text_input('Guess a letter:', max_chars=1)
  submit_guess = st.form_submit_button('Submit')

  if submit_guess and not st.session_state.game_over:
    guess = guess.strip().lower()

    if len(guess) != 1 or not guess.isalpha():
      st.session_state.message = 'Please enter a single letter.'
    elif guess in st.session_state.guessedword:
      st.session_state.message = f'You already guessed "{guess}".'
    elif guess in st.session_state.word:
      for i, letter in enumerate(st.session_state.word):
        if letter == guess:
          st.session_state.guessedword[i] = guess
      st.session_state.message = 'Great guess!'
    else:
      st.session_state.attempts -= 1
      st.session_state.message = 'Wrong guess! Attempts left: ' + str(st.session_state.attempts)

    if '_' not in st.session_state.guessedword:
      st.session_state.message = 'Congratulations!! You guessed the word: ' + st.session_state.word
      st.session_state.game_over = True
    elif st.session_state.attempts <= 0:
      st.session_state.message = 'You\'ve run out of attempts! The word was: ' + st.session_state.word
      st.session_state.game_over = True

if st.session_state.message:
  st.write(st.session_state.message)

if st.session_state.game_over:
  st.write('Game Over! Refresh the page to play again.')
  st.write('The word was: ' + st.session_state.word)

st.write('Made with ❤️ by Darcy')

with st.form("feedback_form"):
  feedback = st.text_area("Your feedback:")
  submitted = st.form_submit_button("Submit")
  if submitted:
    st.write("Thank you for your feedback!")

st.write('streamlit-2026')
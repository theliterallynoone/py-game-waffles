import random
import streamlit as st

st.set_page_config(
    page_title='Word Guessing Game',
    page_icon='🎮',
    layout='centered',
    initial_sidebar_state='collapsed'
)

# Custom CSS for minimalistic UI
st.markdown(
    """
    <style>
    * {
        margin: 0;
        padding: 0;
    }
    
    .main {
        max-width: 600px;
        margin: 0 auto;
    }
    
    .title-container {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .word-display {
        font-size: 3rem;
        letter-spacing: 1rem;
        font-weight: bold;
        text-align: center;
        font-family: 'Courier New', monospace;
        margin: 2rem 0;
        color: #1f77b4;
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
        padding: 1rem;
        background-color: #f8f9fa;
        border-radius: 8px;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #666;
        margin-bottom: 0.5rem;
    }
    
    .stat-value {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1f77b4;
    }
    
    .guessed-letters {
        text-align: center;
        margin: 1.5rem 0;
        min-height: 2rem;
    }
    
    .guessed-label {
        font-size: 0.9rem;
        color: #666;
        margin-bottom: 0.5rem;
    }
    
    .letter-badge {
        display: inline-block;
        margin: 0.3rem;
        padding: 0.4rem 0.8rem;
        background-color: #e0e0e0;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: bold;
    }
    
    .success-message {
        padding: 1rem;
        background-color: #d4edda;
        color: #155724;
        border-radius: 8px;
        text-align: center;
        margin: 1rem 0;
        font-weight: bold;
    }
    
    .error-message {
        padding: 1rem;
        background-color: #f8d7da;
        color: #721c24;
        border-radius: 8px;
        text-align: center;
        margin: 1rem 0;
        font-weight: bold;
    }
    
    .info-message {
        padding: 1rem;
        background-color: #d1ecf1;
        color: #0c5460;
        border-radius: 8px;
        text-align: center;
        margin: 1rem 0;
    }
    
    .game-over-container {
        padding: 2rem;
        background-color: #f8f9fa;
        border-radius: 8px;
        text-align: center;
        margin: 1.5rem 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Expanded word bank by difficulty
EASY_WORDS = ['cat', 'dog', 'bird', 'fish', 'tree', 'book', 'sun', 'moon', 'star', 
              'rain', 'snow', 'wind', 'fire', 'water', 'stone', 'house', 'door', 'hand']

MEDIUM_WORDS = ['python', 'computer', 'programming', 'streamlit', 'database', 'algorithm',
                'function', 'variable', 'problem', 'solution', 'project', 'developer',
                'keyboard', 'monitor', 'software', 'network', 'internet', 'website']

HARD_WORDS = ['encyclopedia', 'extraordinary', 'synchronization', 'architecture', 'philosophical',
              'infrastructure', 'sophisticated', 'complicated', 'enthusiastic', 'experimental',
              'environmental', 'professional', 'achievement', 'development', 'technology']

def get_word_bank(difficulty):
    if difficulty == 'Easy':
        return EASY_WORDS
    elif difficulty == 'Medium':
        return MEDIUM_WORDS
    else:
        return HARD_WORDS

def reset_game(difficulty):
    word_bank = get_word_bank(difficulty)
    st.session_state.word = random.choice(word_bank)
    st.session_state.guessedword = ['_'] * len(st.session_state.word)
    st.session_state.attempts = 6
    st.session_state.message = ''
    st.session_state.game_over = False
    st.session_state.guessed_letters = set()
    st.session_state.difficulty = difficulty

# Initialize session state
if 'word' not in st.session_state:
    st.session_state.difficulty = 'Medium'
    reset_game('Medium')
    st.session_state.guessed_letters = set()
    st.session_state.games_won = 0
    st.session_state.games_lost = 0

# Header
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("<div class='title-container'><h1>🎮 Word Guess</h1></div>", unsafe_allow_html=True)

# Difficulty selector
difficulty_col1, difficulty_col2, difficulty_col3 = st.columns([1, 1, 1])
with difficulty_col1:
    if st.button('🟢 Easy', use_container_width=True, key='easy_btn'):
        if st.session_state.difficulty != 'Easy':
            reset_game('Easy')
        st.rerun()
        
with difficulty_col2:
    if st.button('🟡 Medium', use_container_width=True, key='medium_btn'):
        if st.session_state.difficulty != 'Medium':
            reset_game('Medium')
        st.rerun()
        
with difficulty_col3:
    if st.button('🔴 Hard', use_container_width=True, key='hard_btn'):
        if st.session_state.difficulty != 'Hard':
            reset_game('Hard')
        st.rerun()

st.divider()

# Game stats
stat_col1, stat_col2 = st.columns(2)
with stat_col1:
    st.markdown(f"""
    <div class='stats-container'>
        <div class='stat-item'>
            <div class='stat-label'>Attempts Left</div>
            <div class='stat-value'>{st.session_state.attempts}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
with stat_col2:
    st.markdown(f"""
    <div class='stats-container'>
        <div class='stat-item'>
            <div class='stat-label'>Word Length</div>
            <div class='stat-value'>{len(st.session_state.word)}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Progress bar
progress = (6 - st.session_state.attempts) / 6
progress_color = "#d32f2f" if st.session_state.attempts <= 2 else "#ff9800" if st.session_state.attempts <= 4 else "#4caf50"
st.markdown(f"""
<div style="background-color: #e0e0e0; border-radius: 10px; height: 8px; overflow: hidden; margin: 1rem 0;">
    <div style="background-color: {progress_color}; height: 100%; width: {progress * 100}%;"></div>
</div>
""", unsafe_allow_html=True)

# Word display
st.markdown(f"<div class='word-display'>{' '.join(st.session_state.guessedword)}</div>", unsafe_allow_html=True)

# Guessed letters display
if st.session_state.guessed_letters:
    guessed_str = ' '.join(sorted(st.session_state.guessed_letters))
    st.markdown(f"""
    <div class='guessed-letters'>
        <div class='guessed-label'>Guessed Letters</div>
        {' '.join([f'<span class="letter-badge">{letter.upper()}</span>' for letter in sorted(st.session_state.guessed_letters)])}
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Game logic
with st.form('guess_form', clear_on_submit=True):
    guess = st.text_input('Enter a letter:', max_chars=1, placeholder='A-Z')
    submit_guess = st.form_submit_button('Guess', use_container_width=True)

    if submit_guess and not st.session_state.game_over:
        guess = guess.strip().lower()

        if not guess:
            st.session_state.message = 'Please enter a letter'
            st.session_state.message_type = 'info'
        elif len(guess) != 1 or not guess.isalpha():
            st.session_state.message = 'Please enter a single letter (A-Z)'
            st.session_state.message_type = 'error'
        elif guess in st.session_state.guessed_letters:
            st.session_state.message = f'You already guessed "{guess.upper()}"'
            st.session_state.message_type = 'info'
        elif guess in st.session_state.word:
            for i, letter in enumerate(st.session_state.word):
                if letter == guess:
                    st.session_state.guessedword[i] = guess
            st.session_state.guessed_letters.add(guess)
            st.session_state.message = '✓ Correct guess!'
            st.session_state.message_type = 'success'
        else:
            st.session_state.attempts -= 1
            st.session_state.guessed_letters.add(guess)
            st.session_state.message = f'✗ Wrong! "{guess.upper()}" is not in the word'
            st.session_state.message_type = 'error'

        # Check win/loss
        if '_' not in st.session_state.guessedword:
            st.session_state.message = f'🎉 You Won! The word was: {st.session_state.word.upper()}'
            st.session_state.message_type = 'success'
            st.session_state.game_over = True
            st.session_state.games_won += 1
        elif st.session_state.attempts <= 0:
            st.session_state.message = f'😢 Game Over! The word was: {st.session_state.word.upper()}'
            st.session_state.message_type = 'error'
            st.session_state.game_over = True
            st.session_state.games_lost += 1

        st.rerun()

# Display message
if hasattr(st.session_state, 'message') and st.session_state.message:
    message_type = getattr(st.session_state, 'message_type', 'info')
    if message_type == 'success':
        st.markdown(f"<div class='success-message'>{st.session_state.message}</div>", unsafe_allow_html=True)
    elif message_type == 'error':
        st.markdown(f"<div class='error-message'>{st.session_state.message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='info-message'>{st.session_state.message}</div>", unsafe_allow_html=True)

# Game over screen
if st.session_state.game_over:
    st.divider()
    st.markdown("<div class='game-over-container'>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button('🔄 Play Again', use_container_width=True):
            reset_game(st.session_state.difficulty)
            st.rerun()
    with col2:
        if st.button('🏠 New Difficulty', use_container_width=True):
            st.session_state.show_difficulty = True
            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer with stats
st.divider()
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"<div style='text-align: center;'><p style='color: #666; font-size: 0.9rem;'>Wins: <strong style='color: #4caf50;'>{st.session_state.games_won}</strong></p></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div style='text-align: center;'><p style='color: #666; font-size: 0.9rem;'>Losses: <strong style='color: #d32f2f;'>{st.session_state.games_lost}</strong></p></div>", unsafe_allow_html=True)

st.markdown("<div style='text-align: center; margin-top: 2rem; color: #999; font-size: 0.85rem;'>Made with ❤️ • Word Guessing Game 2026</div>", unsafe_allow_html=True)

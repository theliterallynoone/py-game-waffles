import streamlit as st
from word_guessing import run_word_guessing

st.set_page_config(
    page_title='Game Hub',
    page_icon='🎲',
    layout='wide',
    initial_sidebar_state='expanded'
)

st.markdown(
    """
    <style>
    body {
        background: #f7f9fc;
    }
    .home-title {
        margin-bottom: 0.5rem;
    }
    .game-card {
        border: 1px solid #e1e5eb;
        border-radius: 16px;
        padding: 1.5rem;
        background: white;
        box-shadow: 0 12px 24px rgba(15, 23, 42, 0.06);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .game-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 18px 32px rgba(15, 23, 42, 0.12);
    }
    .game-card h3 {
        margin-top: 0;
    }
    .sidebar .block-container {
        padding-top: 1rem;
    }
    """,
    unsafe_allow_html=True,
)

st.sidebar.title('Game Menu')
selected_game = st.sidebar.radio(
    'Choose a game',
    ['Home', 'Word Guessing', 'Snake (Coming Soon)'],
)

st.sidebar.markdown('---')

if selected_game == 'Home':
    st.markdown('<div class="home-title"><h1>🎮 Welcome to the Game Hub</h1></div>', unsafe_allow_html=True)
    st.write('Choose a game from the sidebar to start playing.')

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            """
            <div class='game-card'>
                <h3>Word Guessing</h3>
                <p>Guess the hidden word, one letter at a time. Choose from easy, medium, or hard word banks.</p>
                <p><strong>Ready to play?</strong></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class='game-card'>
                <h3>Other Games</h3>
                <p>Explore more game ideas like Snake. More games will be added soon!</p>
                <p>For now, select a game on the left to launch it.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif selected_game == 'Word Guessing':
    run_word_guessing(set_page=False)
else:
    st.markdown(f"<h1>{selected_game}</h1>", unsafe_allow_html=True)
    st.info('This game spot is reserved for future builds.')
    if 'Snake' in selected_game:
        st.write('A C++ version of Snake is available in the workspace as `snake.cpp`.')
    st.write('Check back later for more interactive game experiences.')

st.markdown("<div style='text-align: center; margin-top: 2rem; color: #999; font-size: 0.85rem;'>Made with ❤️ • Game Hub • 2026</div>", unsafe_allow_html=True)
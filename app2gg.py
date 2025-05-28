{\rtf1\ansi\ansicpg1252\cocoartf2707
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww14980\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import random\
import time\
\
# Game configuration\
GRID_SIZE = 10\
SPEED = 0.3  # seconds between moves\
\
# Initialize game state\
if "snake" not in st.session_state:\
    st.session_state.snake = [(5, 5)]\
    st.session_state.food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))\
    st.session_state.direction = "RIGHT"\
    st.session_state.score = 0\
    st.session_state.game_over = False\
\
# Game control buttons\
st.title("\uc0\u55357 \u56333  Snake Game in Streamlit")\
col1, col2, col3 = st.columns([1, 1, 1])\
with col2:\
    if st.button("\uc0\u11014 \u65039  UP"):\
        if st.session_state.direction != "DOWN":\
            st.session_state.direction = "UP"\
with col1:\
    if st.button("\uc0\u11013 \u65039  LEFT"):\
        if st.session_state.direction != "RIGHT":\
            st.session_state.direction = "LEFT"\
with col3:\
    if st.button("\uc0\u10145 \u65039  RIGHT"):\
        if st.session_state.direction != "LEFT":\
            st.session_state.direction = "RIGHT"\
with col2:\
    if st.button("\uc0\u11015 \u65039  DOWN"):\
        if st.session_state.direction != "UP":\
            st.session_state.direction = "DOWN"\
\
# Restart button\
if st.button("\uc0\u55357 \u56577  Restart Game"):\
    st.session_state.snake = [(5, 5)]\
    st.session_state.food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))\
    st.session_state.direction = "RIGHT"\
    st.session_state.score = 0\
    st.session_state.game_over = False\
    st.experimental_rerun()\
\
# Movement logic\
def move_snake():\
    if st.session_state.game_over:\
        return\
\
    head = st.session_state.snake[0]\
    direction = st.session_state.direction\
    if direction == "UP":\
        new_head = (head[0] - 1, head[1])\
    elif direction == "DOWN":\
        new_head = (head[0] + 1, head[1])\
    elif direction == "LEFT":\
        new_head = (head[0], head[1] - 1)\
    elif direction == "RIGHT":\
        new_head = (head[0], head[1] + 1)\
\
    # Check for wall or self collision\
    if (new_head in st.session_state.snake) or not (0 <= new_head[0] < GRID_SIZE) or not (0 <= new_head[1] < GRID_SIZE):\
        st.session_state.game_over = True\
        return\
\
    st.session_state.snake.insert(0, new_head)\
\
    # Check for food\
    if new_head == st.session_state.food:\
        st.session_state.score += 1\
        while True:\
            new_food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))\
            if new_food not in st.session_state.snake:\
                st.session_state.food = new_food\
                break\
    else:\
        st.session_state.snake.pop()\
\
# Draw grid\
def draw_board():\
    board = [["\uc0\u11035 " for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]\
    for x, y in st.session_state.snake:\
        board[x][y] = "\uc0\u55357 \u57321 "\
    fx, fy = st.session_state.food\
    board[fx][fy] = "\uc0\u55356 \u57166 "\
\
    board_display = "\\n".join("".join(row) for row in board)\
    st.markdown(f"<pre style='font-size:20px'>\{board_display\}</pre>", unsafe_allow_html=True)\
\
# Move and render\
move_snake()\
draw_board()\
\
# Display score\
st.write(f"**Score:** \{st.session_state.score\}")\
if st.session_state.game_over:\
    st.error("\uc0\u55357 \u56448  Game Over!")\
else:\
    time.sleep(SPEED)\
    st.experimental_rerun()\
}
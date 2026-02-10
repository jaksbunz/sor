import streamlit as st
from moviepy.audio.io.AudioFileClip import AudioFileClip
import time

if 'accepted' not in st.session_state:
    st.session_state['accepted'] = False
if 'start_time' not in st.session_state:
    st.session_state['start_time'] = None
if 'duration' not in st.session_state:
    st.session_state['duration'] = 0
if 'go_next' not in st.session_state:
    st.session_state['go_next'] = False

st.markdown(
    "<h1 style='text-align: center; font-size:50px;'>Click the press button po, baby</h1>",
    unsafe_allow_html=True
)

st.write("")
st.write("")
st.write("")

col1, col2, col3 = st.columns([2.3, 2, 1])
with col2:
    yes = st.button("PRESS", key="big_button")

if yes and not st.session_state['accepted']:
    st.session_state['accepted'] = True
    audio_path = "C:/Users/admin/Downloads/6d632feb-32da-4d4b-a926-ca4644221e57.mp4"

    st.audio(audio_path, format="audio/mp3", start_time=0)

    audio = AudioFileClip(audio_path)
    st.session_state['duration'] = audio.duration
    audio.close()

    st.session_state['start_time'] = time.time()
    st.success("I'm really sorry po talaga, baby")
    st.success("I love you so much po")

import streamlit as st
import streamlit.components.v1 as components

# from gtts import gTTS
# from pydub import AudioSegment
# from pydub.playback import play

# def text_to_speech(text):
#     tts = gTTS(text=text, lang='en')
#     audio_file = 'output.mp3'
#     tts.save(audio_file)
#     sound = AudioSegment.from_mp3(audio_file)
#     play(sound)
    
def speak(text):
    # JavaScript code for text-to-speech using the Web Speech API
    js = f"""
    <script>
    var msg = new SpeechSynthesisUtterance();
    msg.text = "{text}";
    msg.lang = 'en-US';
    window.speechSynthesis.speak(msg);
    </script>
    """
    # Use Streamlit's components.html to execute the JavaScript code
    components.html(js, height=0, width=0)

# def speak(text):
#     # JavaScript to choose a female voice, assuming one is available among the English voices
#     js = f"""
#     <script>
#     function speakText() {{
#         var msg = new SpeechSynthesisUtterance();
#         msg.text = "{text}";
#         msg.lang = 'en-US';

#         // Get the list of available voices
#         var voices = window.speechSynthesis.getVoices();

#         // Attempt to find a female voice among the English voices
#         // This is a heuristic approach and might not always accurately select a female voice
#         var femaleVoice = voices.find(voice => voice.lang.startsWith('en-') && voice.name.toLowerCase().includes('female'));

#         // If a female voice is found, use it
#         if (femaleVoice) {{
#             msg.voice = femaleVoice;
#         }}

#         window.speechSynthesis.speak(msg);
#     }}

#     // Due to the asynchronous nature of voice loading, attempt to speak after ensuring voices are loaded
#     if (speechSynthesis.onvoiceschanged !== undefined) {{
#         speechSynthesis.onvoiceschanged = speakText;
#     }} else {{
#         setTimeout(speakText, 500);
#     }}
#     </script>
#     """
#     # Execute the JavaScript code
#     st.markdown(js, unsafe_allow_html=True)
        
        
# Apply custom CSS styles
# Apply custom CSS styles
st.markdown(
    """
    <style>
    /* Define large words */
    .large-text {
        font-size: 36px;
    }

    /* Apply "My Little Pony" theme */
    body {
        background-color: #FFD5E5 !important; /* Pink background */
    }

    h1 {
        color: #7F00FF; /* Violet header */
    }

    h2 {
        color: #FF69B4; /* Pink header */
    }

    p {
        color: #800080; /* Purple text */
    }

    </style>
    """,
    unsafe_allow_html=True
)
# def main():
col1, col2 = st.columns(2)

col1.title("Yong Yee's Secret Lab!")
picture = col2.camera_input("My Security Camera")

# if picture:
#     st.image(picture)
# Define the correct 4-digit code
correct_code = col2.text_input('Yong Yee Secret Lab',type="password")
# correct_code = "1234"

# Create input widget for the user to enter the code
entered_code = col2.text_input("Enter the 4-digit code:")

# Check if the entered code matches the correct code
if col2.button("Submit"):
    if entered_code == correct_code:
        # If the codes match, play success sound and display balloons
        st.success("Correct! Please enter!")
        speak("Correct! Please enter!")
        # play_sound("success_sound.mp3")  # Replace with your success sound file path
        st.balloons()
    else:
        # If the codes do not match, display error message and play error sound
        st.error("Wrong. Hahahahahaha!")
        speak("Wrong. Hahahahahaha!")
        # play_sound("error_sound.mp3")  # Replace with your error sound file path


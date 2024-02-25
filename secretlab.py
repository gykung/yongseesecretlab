import streamlit as st
# from playsound import playsound

# def play_sound(file_path):
#     playsound(file_path)

def main():
    st.title("Yong Yee's Secret Lab!")
    picture = st.camera_input("Take a picture")

    if picture:
        st.image(picture)
    # Define the correct 4-digit code
    correct_code = st.text_input('Yong Yee Secret Lab',type="password")
    # correct_code = "1234"

    # Create input widget for the user to enter the code
    entered_code = st.text_input("Enter the 4-digit code:")

    # Check if the entered code matches the correct code
    if st.button("Submit"):
        if entered_code == correct_code:
            # If the codes match, play success sound and display balloons
            st.success("Correct! Please enter!")
            # play_sound("success_sound.mp3")  # Replace with your success sound file path
            st.balloons()
        else:
            # If the codes do not match, display error message and play error sound
            st.error("Wrong. Hahahahahaha!")
            # play_sound("error_sound.mp3")  # Replace with your error sound file path

if __name__ == "__main__":
    main()
    
    
    #python -m streamlit run "c:\users\kgua\onedrive - singapore refining company\data\play\secretlab.py"

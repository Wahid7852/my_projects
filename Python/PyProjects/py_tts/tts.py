import pyttsx3
import speech_recognition as sr

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    engine.say(text)
    engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Please start speaking...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print(f"Request error: {e}")
    
    return ""

if __name__ == "__main__":
    user_choice = None
    
    while user_choice != "0":
        if user_choice == "1":
            text = input("Enter the text you want to convert to speech: ")
            text_to_speech(text)
        elif user_choice == "2":
            recognized_text = speech_to_text()
            if recognized_text:
                print("Recognized Text:", recognized_text)
        
        print("\nOptions:")
        print("1. Text-to-Speech (TTS)")
        print("2. Speech-to-Text (STT)")
        print("0. Exit")
        user_choice = input("Choose an option: ")
        
        if user_choice not in ["0", "1", "2"]:
            print("Invalid choice. Please select 1 for TTS, 2 for STT, or 0 to exit.")
    
    print("Exiting the program.")
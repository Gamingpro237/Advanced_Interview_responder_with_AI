import os
import json
import time
import keyboard
import threading
import tkinter as tk
from vosk import Model, KaldiRecognizer
import pyaudio
import openai
import PyPDF2


# Set your OpenAI API Key
openai.api_key = "your_openai_api_key_here"

# Vosk model setup (update the path to your downloaded model)
vosk_model_path = "path_to_vosk_model_directory"

# Initialize Vosk Speech Recognition model
if not os.path.exists(vosk_model_path):
    print(f"Please download the model from https://alphacephei.com/vosk/models and unpack as '{vosk_model_path}'")
    exit(1)

model = Model(vosk_model_path)
recognizer = KaldiRecognizer(model, 16000)

# Initialize PyAudio
p = pyaudio.PyAudio()

# Start a PyAudio stream
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()
# Function to stop and clear the recording
def stop_and_clear_recording():
    global stream
    if stream.is_active():
        stream.stop_stream()  # Stop the audio stream
        stream.close()        # Close the audio stream


# Teleprompter: Floating window
class Telepromter:
    def __init__(self):
     self.root = tk.Tk()
     self.root.title("Advanced_Interview_Responder_with_AI")
     self.root.geometry("1100x600")
     self.root.attributes("-topmost", True)
     self.root.attributes("-alpha", 0.6)  # Slight transparency
     self.root.resizable(True, True)
     
     self.text_widget = tk.Text(self.root, wrap='word', font=("Arial", 20), bg="black", fg="white", padx=10, pady=10)
     self.text_widget.configure(state="disabled")
     self.text_widget.pack(expand=True, fill='both')
     self.root.update()
     
    def update_text(self, response_text):
     self.text_widget.configure(state="normal")
     self.text_widget.delete(1.0,tk.END)   #clear previous text
     self.text_widget.insert(tk.END, response_text)    #insert new text
     self.text_widget.configure(state="disabled")
     self.root.update()
     
#gkljkh
'''
def create_overlay(response_text):
    root = tk.Tk()
    root.title("Advanced_Interview_Responder_with_AI")
    root.geometry("1366x768")
    root.attributes("-topmost", True)
    root.attributes("-alpha", 0.7)  # Slight transparency
    root.resizable(False, False)

    text_widget = tk.Text(root, wrap='word', font=("Arial", 20), bg="black", fg="white", padx=10, pady=10)
    text_widget.insert(tk.END, response_text)
    text_widget.configure(state="disabled")
    text_widget.pack(expand=True, fill='both')
'''


# Resume Parsing
def extract_resume_data(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        resume_text = ""
        for page in reader.pages:
            resume_text += page.extract_text()
    return resume_text

# Get response from GPT based on the question and resume data
def get_response_from_gpt(prompt, resume_context):
    full_prompt = f"Respond as if you were me. The question is :\n{prompt}\n\n My Resume information: {resume_context}"
    response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
             {"role":"user","content":full_prompt}],
            
           max_tokens=60,
              n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

# Speech Recognition with Vosk
def transcribe_audio():
    print("Listening for questions...")
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            text = json.loads(result).get("text", "")
            if text:
                print(f"Transcribed text: {text}")
                return text
            
pause_event= threading.Event()
def toggle_pause_reaume():
    if pause_event.is_set():
        print("Resuming bot.......")
        pause_event.clear() # resume
    else:
        print("Pausing bot........")
        pause_event.set() # pause
def listen_for_keyboard():
    keyboard.on_press(lambda _:toggle_pause_reaume(), lambda _:stop_and_clear_recording())
    keyboard.wait() #keep the listener active
    
# Main interview process
def start_interview():
    resume_path = "path_to_resume.pdf"  # Update with your resume path
    resume_data = extract_resume_data(resume_path)
    teleprompter= Telepromter()
    while True:
        # Step 1: Transcribe audio (question)
        question = transcribe_audio()

        if question:
            # Step 2: Get response from GPT
            response = get_response_from_gpt(question, resume_data)
            print(f"Generated response: {response}")
            
            # Step 3: Display response in the teleprompter (0n the same window)
            teleprompter.update_text(response)

        time.sleep(1)

if __name__ == "__main__":
    # Start the keyboard listener in a separate thread
    keyboard_thread = threading.Thread(target=listen_for_keyboard)
    keyboard_thread.daemon = True  # Run as a background thread
    keyboard_thread.start()

    # Start the interview process
    start_interview()

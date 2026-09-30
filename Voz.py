from tkinter import *
import speech_recognition as sr
vent= Tk()
vent.geometry("500x500")
def r_audio():
    speech_recognition= sr.Recognizer()
    with sr.Microphone() as source:
        audio= speech_recognition.listen(source)
        voice_data=""
        try:
            voice_data= speech_recognition.recognize_google(audio, language= 'es-mx')
        except sr.UnknownValueError:
            print("Por favor, repite. No entendi tu solicitud")
    print(voice_data)

r_audio()

vent.mainloop()
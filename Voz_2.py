import speech_recognition as sr

for i, nombre in enumerate(sr.Microphone.list_microphone_names()):
    print(i, nombre)
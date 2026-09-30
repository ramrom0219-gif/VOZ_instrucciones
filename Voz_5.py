import tkinter as tk
import speech_recognition as sr

vent = tk.Tk()
vent.geometry("500x500")
vent.title("Reconocimiento de voz")


def r_audio():

    reconocimiento = sr.Recognizer()

    try:
        with sr.Microphone(device_index=15) as source:

            print("Escuchando...")
            reconocimiento.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = reconocimiento.listen(source)

        texto = reconocimiento.recognize_google(
            audio,
            language="es-MX"
        )

        print("Reconocí:", texto)

    except sr.UnknownValueError:
        print("No entendí el audio.")

    except sr.RequestError as error:
        print("Problema con el servicio:", error)

    except Exception as error:
        print("Problema con el micrófono:", error)


boton = tk.Button(
    vent,
    text="HABLAR",
    command=r_audio
)

boton.pack(pady=100)

vent.mainloop()
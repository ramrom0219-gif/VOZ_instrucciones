from tkinter import *
from tkinter import ttk
import speech_recognition as sr


# -----------------------------
# VENTANA
# -----------------------------
vent = Tk()
vent.geometry("600x400")
vent.title("Reconocimiento de voz")


# -----------------------------
# DETECTAR MICRÓFONOS
# -----------------------------
microfonos = sr.Microphone.list_microphone_names()

print("MICRÓFONOS DETECTADOS:")
print("----------------------")

for i, nombre in enumerate(microfonos):
    print(i, nombre)


# -----------------------------
# COMBOBOX
# -----------------------------
Label(
    vent,
    text="Selecciona un micrófono:",
    font=("Arial", 14)
).pack(pady=20)


combo_microfonos = ttk.Combobox(
    vent,
    width=60,
    state="readonly"
)

combo_microfonos.pack()


# Mostrar los micrófonos en el ComboBox
lista_microfonos = []

for i, nombre in enumerate(microfonos):
    lista_microfonos.append(f"{i} - {nombre}")

combo_microfonos["values"] = lista_microfonos


# Seleccionar el primero automáticamente
if len(lista_microfonos) > 0:
    combo_microfonos.current(0)


# -----------------------------
# FUNCIÓN PARA SABER CUÁL SE USA
# -----------------------------
def mostrar_microfono():
    seleccion = combo_microfonos.get()

    if seleccion == "":
        etiqueta_estado.config(
            text="No has seleccionado un micrófono"
        )
        return

    print("Micrófono seleccionado:")
    print(seleccion)

    etiqueta_estado.config(
        text="Micrófono seleccionado:\n" + seleccion
    )


# -----------------------------
# BOTÓN
# -----------------------------
boton_seleccionar = Button(
    vent,
    text="Seleccionar micrófono",
    command=mostrar_microfono
)

boton_seleccionar.pack(pady=20)


# -----------------------------
# RECONOCIMIENTO DE VOZ
# -----------------------------
def r_audio():

    seleccion = combo_microfonos.get()

    if seleccion == "":
        etiqueta_estado.config(
            text="Selecciona primero un micrófono"
        )
        return

    # Obtener el número del micrófono
    indice = int(seleccion.split(" - ")[0])

    print("Usando micrófono:", indice)
    print(microfonos[indice])

    reconocimiento = sr.Recognizer()

    try:

        with sr.Microphone(device_index=indice) as source:

            etiqueta_estado.config(
                text="Escuchando...\nHabla ahora"
            )

            vent.update()

            audio = reconocimiento.listen(source)

        try:

            voice_data = reconocimiento.recognize_google(
                audio,
                language="es-MX"
            )

            print("Texto reconocido:")
            print(voice_data)

            etiqueta_estado.config(
                text="Dijiste:\n" + voice_data
            )

        except sr.UnknownValueError:

            print("No se entendió el audio")

            etiqueta_estado.config(
                text="No entendí lo que dijiste.\nIntenta nuevamente."
            )

        except sr.RequestError as error:

            print("Error con Google:", error)

            etiqueta_estado.config(
                text="No fue posible conectarse al servicio."
            )

    except Exception as error:

        print("Error al utilizar el micrófono:")
        print(error)

        etiqueta_estado.config(
            text="Error al utilizar el micrófono.\n"
                 "Revisa que esté conectado y disponible."
        )


# -----------------------------
# BOTÓN HABLAR
# -----------------------------
boton_hablar = Button(
    vent,
    text="🎤 HABLAR",
    font=("Arial", 14),
    command=r_audio
)

boton_hablar.pack(pady=20)


# -----------------------------
# ETIQUETA DE ESTADO
# -----------------------------
etiqueta_estado = Label(
    vent,
    text="Selecciona un micrófono",
    font=("Arial", 12),
    wraplength=550
)

etiqueta_estado.pack(pady=20)


# -----------------------------
# INICIAR VENTANA
# -----------------------------
vent.mainloop()
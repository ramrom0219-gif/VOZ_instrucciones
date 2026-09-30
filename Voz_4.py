
from tkinter import *
from tkinter import ttk
import speech_recognition as sr


# ==========================================
# VENTANA
# ==========================================

vent = Tk()
vent.geometry("700x500")
vent.title("Detector de micrófonos")


# ==========================================
# OBTENER MICRÓFONOS
# ==========================================

try:
    microfonos = sr.Microphone.list_microphone_names()
except Exception as error:
    microfonos = []
    print("Error al detectar micrófonos:")
    print(error)


print("===================================")
print("MICRÓFONOS DETECTADOS")
print("===================================")

for i, nombre in enumerate(microfonos):
    print(i, "-", nombre)


# ==========================================
# TÍTULO
# ==========================================

titulo = Label(
    vent,
    text="Detector de micrófonos",
    font=("Arial", 20)
)

titulo.pack(pady=20)


# ==========================================
# LISTA DE MICRÓFONOS
# ==========================================

Label(
    vent,
    text="Micrófonos encontrados:",
    font=("Arial", 13)
).pack()


combo_microfonos = ttk.Combobox(
    vent,
    width=70,
    state="readonly"
)

combo_microfonos.pack(pady=10)


# Agregar micrófonos al ComboBox

lista_microfonos = []

for i, nombre in enumerate(microfonos):
    lista_microfonos.append(
        str(i) + " - " + nombre
    )

combo_microfonos["values"] = lista_microfonos


# Seleccionar automáticamente el primero

if len(lista_microfonos) > 0:
    combo_microfonos.current(0)


# ==========================================
# ETIQUETA DE ESTADO
# ==========================================

estado = Label(
    vent,
    text="Selecciona un micrófono y presiona PROBAR",
    font=("Arial", 12),
    wraplength=650
)

estado.pack(pady=20)
# ==========================================
# FUNCIÓN PARA PROBAR MICRÓFONO
# ==========================================

def probar_microfono():

    if combo_microfonos.get() == "":
        estado.config(
            text="Primero selecciona un micrófono."
        )
        return

    # Obtener índice
    seleccion = combo_microfonos.get()

    indice = int(
        seleccion.split(" - ")[0]
    )

    nombre = microfonos[indice]

    print()
    print("===================================")
    print("PROBANDO MICRÓFONO")
    print("Índice:", indice)
    print("Nombre:", nombre)
    print("===================================")

    estado.config(
        text="Probando:\n" + nombre +
        "\n\nHabla durante unos segundos..."
    )

    vent.update()

    reconocimiento = sr.Recognizer()

    try:

        with sr.Microphone(
            device_index=indice
        ) as source:

            print("Ajustando ruido ambiental...")

            reconocimiento.adjust_for_ambient_noise(
                source,
                duration=1
            )

            print("Habla ahora...")

            estado.config(
                text="🎤 HABLA AHORA\n\n"
                + nombre
            )

            vent.update()

            audio = reconocimiento.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

        print("Procesando audio...")

        estado.config(
            text="Procesando lo que dijiste..."
        )

        vent.update()

        texto = reconocimiento.recognize_google(
            audio,
            language="es-MX"
        )

        print("===================================")
        print("MICRÓFONO FUNCIONANDO")
        print("Micrófono:", nombre)
        print("Texto:", texto)
        print("===================================")

        estado.config(
            text="✅ MICRÓFONO FUNCIONANDO\n\n"
            "Micrófono:\n"
            + nombre
            + "\n\nReconocí:\n"
            + texto
        )

    except sr.WaitTimeoutError:

        print("No se detectó voz.")

        estado.config(
            text="⚠️ No detecté voz.\n\n"
            "El micrófono puede estar funcionando, "
            "pero no se detectó que hablaras."
        )

    except sr.UnknownValueError:

        print("Se recibió audio, pero no se entendió.")

        estado.config(
            text="⚠️ El micrófono recibió audio,\n"
            "pero no pude entender lo que dijiste."
        )

    except sr.RequestError as error:

        print("Error con Google Speech Recognition:")
        print(error)

        estado.config(
            text="⚠️ El micrófono puede funcionar,\n"
            "pero hubo un problema con el servicio "
            "de reconocimiento de voz."
        )

    except Exception as error:

        print("ERROR:")
        print(error)

        estado.config(
            text="❌ Error al probar el micrófono:\n\n"
            + str(error)
        )

# ==========================================
# BOTÓN PROBAR
# ==========================================

boton_probar = Button(
    vent,
    text="🎤 PROBAR MICRÓFONO",
    font=("Arial", 14),
    command=probar_microfono
)

boton_probar.pack(pady=10)


# ==========================================
# BOTÓN MOSTRAR MICRÓFONO SELECCIONADO
# ==========================================

def mostrar_seleccion():

    seleccion = combo_microfonos.get()

    if seleccion == "":
        estado.config(
            text="No hay ningún micrófono seleccionado."
        )
        return

    indice = int(
        seleccion.split(" - ")[0]
    )

    print()
    print("Micrófono seleccionado:")
    print("Índice:", indice)
    print("Nombre:", microfonos[indice])

    estado.config(
        text="Micrófono seleccionado:\n\n"
        + microfonos[indice]
    )


boton_seleccionar = Button(
    vent,
    text="Mostrar seleccionado",
    command=mostrar_seleccion
)

boton_seleccionar.pack(pady=5)


# ==========================================
# INICIAR
# ==========================================
vent.mainloop()
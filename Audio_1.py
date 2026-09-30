import pyaudio

audio = pyaudio.PyAudio()

print("======================================")
print("DISPOSITIVOS DE AUDIO")
print("======================================")

for i in range(audio.get_device_count()):

    info = audio.get_device_info_by_index(i)

    print(
        i,
        "-",
        info["name"],
        "-",
        "Entradas:",
        info["maxInputChannels"]
    )

audio.terminate()
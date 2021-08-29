import sounddevice
from scipy.io.wavfile import write

# define tempo de gravação
fs = 44100
second = int(input("Quantos segundos deseja gravar ?"))

print("\nGravando......\n")

# Captura a gravação
record_voice = sounddevice.rec(int(second*fs), samplerate=fs, channels=2)
sounddevice.wait()

# salva arquivo da gravação
write("gravacao.wav", fs, record_voice)

print("Gravação Finalizada")

# For å laste inn pakkene: pip install sounddevice scipy 

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io.wavfile import read
from scipy.io.wavfile import write

fs = 44100  # Samplingsfrekvens
seconds = 2  # Lengden på opptaket

print("Snakk nå!")
opptak = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  
print("Opptak ferdig!")

write("opptak.wav", fs, opptak)  # Lagrer filen


fs, data = read("opptak.wav") # Leser lydfilen
data = data.flatten()  #Gjør om til 1D array


N = len(data)
fft_data = np.fft.fft(data) #Diskret fouriertrensformering av dataen
freq = np.fft.fftfreq(N, d = 1/fs) #Diskret fouriertransformering av frekvensene

# Bare ha med de positive frekvensene
positive_freqs = freq[:N // 2]
amplitudes = np.abs(fft_data)[:N // 2]


plt.figure(figsize=(10, 5))
plt.plot(positive_freqs, amplitudes)
plt.title("Frekvensspekter av lyd")
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude")
plt.xlim(0, 4000)  # Velger taleområde å fokusere på
plt.grid(True)
plt.show()

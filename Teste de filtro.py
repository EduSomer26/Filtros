import numpy as np 
import matplotlib.pyplot as plt 
import scipy as sp
from scipy.io.wavfile import read, write
from scipy.signal import sosfilt, iirfilter

#samplerate é o número de vezes por segundo que o som é registrado, dado em Hertz (taxa de amostragem)
#data.shape[0] são a quantidade de amostras disponíveis e data.shape[1] o número de canais.
#data[0]

samplerate, data = read('The Animals - The House of the Rising Sun (TRADUÇÃO) 1964.wav') 
length = data.shape[0] / samplerate
time = np.linspace(0,length,data.shape[0])
Período = time[2] - time[1]
Fs = 1/Período

fig, ax1 = plt.subplots(3,2)
ax1[0][0].plot(time,data[:,0])
ax1[1][0].magnitude_spectrum(data[:,0], Fs=Fs,sides='twosided')
ax1[2][0].phase_spectrum(data[:,0], Fs=Fs,sides='twosided')

#Filtro passa alta
sos = iirfilter(4,50, fs=Fs, btype='highpass',output='sos',ftype='butter')
data[:,0] = sosfilt(sos,data[:,0])

#Filtro passa baixa
sos = iirfilter(4,52, fs=Fs, btype='lowpass',output='sos',ftype='butter')
data[:,0] = sosfilt(sos,data[:,0])

ax1[0][1].plot(time,data[:,0])
ax1[1][1].magnitude_spectrum(data[:,0], Fs=Fs,sides='twosided')
ax1[2][1].phase_spectrum(data[:,0], Fs=Fs,sides='twosided')

write("example2.wav", samplerate, data)
plt.show()
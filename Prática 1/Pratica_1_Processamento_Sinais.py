import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqz, lfilter

# 1) Geração do sinal

N = 100  # Número de amostras
n = np.arange(N)  # Vetor de amostras
frequencias = [0.1 * np.pi, 0.5 * np.pi, 0.75 * np.pi]  # Frequências angulares
amplitudes = [1, 1.5, 0.5]  # Amplitudes

sinal = np.sum(np.sin(np.outer(n, frequencias)) * amplitudes, axis=1)

plt.figure()
plt.plot(n, sinal)
plt.title('Sinal Original')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.show()

# 2) Transformada de Fourier do sinal

S = np.fft.fftshift(np.abs(np.fft.fft(sinal)))  # Módulo da FFT

frequencias_fft = np.linspace(-np.pi, np.pi, N)  # Eixo de frequências

plt.figure()
plt.plot(frequencias_fft, S)
plt.title('Transformada de Fourier do Sinal')
plt.xlabel('Frequência (rad/s)')
plt.ylabel('|S(f)|')
plt.show()

# 3) Filtro Butterworth

wc = 0.3 * np.pi  # Frequência de corte
ordem = 4  # Ordem do filtro
b, a = butter(ordem, wc / np.pi)  # Coeficientes do filtro passa-baixa
impulso = np.concatenate([[1], np.zeros(N - 1)])  # Resposta ao impulso

resposta_impulso = lfilter(b, a, impulso)

plt.figure()
plt.stem(resposta_impulso)
plt.title('Resposta ao Impulso do Filtro Butterworth')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.show()

# 4) Resposta em magnitude do filtro

w, h = freqz(b, a, N, whole=True)  # Resposta em frequência

plt.figure()
plt.plot(w - np.pi, np.abs(np.fft.fftshift(h)))  # Frequências entre -pi e pi
plt.title('Resposta em Magnitude do Filtro')
plt.xlabel('Frequência (rad/s)')
plt.ylabel('|H(f)|')
plt.show()

# 5) Filtragem do sinal

sinal_filtrado = lfilter(b, a, sinal)

plt.figure()
plt.plot(n, sinal_filtrado)
plt.title('Sinal Filtrado')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.show()

# 6) Transformada de Fourier do sinal filtrado

S_filtrado = np.fft.fftshift(np.abs(np.fft.fft(sinal_filtrado)))  # Módulo da FFT

plt.figure()
plt.plot(frequencias_fft, S_filtrado)
plt.title('Transformada de Fourier do Sinal Filtrado')
plt.xlabel('Frequência (rad/s)')
plt.ylabel('|S_{filtrado}(f)|')
plt.show()

# 7) Adição de ruído e repetição

variancia_ruido = 0.1
ruido = np.sqrt(variancia_ruido) * np.random.randn(N)  # Ruído branco gaussiano
sinal_ruidoso = sinal + ruido

# Gráfico do sinal com ruído
plt.figure()
plt.plot(n, sinal_ruidoso)
plt.title('Sinal com Ruído')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.show()

# Transformada de Fourier do sinal com ruído
S_ruidoso = np.fft.fftshift(np.abs(np.fft.fft(sinal_ruidoso)))

plt.figure()
plt.plot(frequencias_fft, S_ruidoso)
plt.title('Transformada de Fourier do Sinal com Ruído')
plt.xlabel('Frequência (rad/s)')
plt.ylabel('|S_{ruidoso}(f)|')
plt.show()

# Filtrar o sinal com ruído
sinal_filtrado_ruidoso = lfilter(b, a, sinal_ruidoso)

plt.figure()
plt.plot(n, sinal_filtrado_ruidoso)
plt.title('Sinal Filtrado com Ruído')
plt.xlabel('Amostras')
plt.ylabel('Amplitude')
plt.show()

# Transformada de Fourier do sinal filtrado com ruído
S_filtrado_ruidoso = np.fft.fftshift(np.abs(np.fft.fft(sinal_filtrado_ruidoso)))

plt.figure()
plt.plot(frequencias_fft, S_filtrado_ruidoso)
plt.title('Transformada de Fourier do Sinal Filtrado com Ruído')
plt.xlabel('Frequência (rad/s)')
plt.ylabel('|S_{filtrado\_ruidoso}(f)|')
plt.show()
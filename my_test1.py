import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt
from pydub import AudioSegment

wf = wave.open('assets/Cowboy Bebop - Full.wav', 'rb')  # mode: read binary

p = pyaudio.PyAudio()   # Creates a PyAudio object just like Scanner() in Scanner class in Java

# Read audio data
chunk = 4096
data = wf.readframes(chunk)

# Close PyAudio
p.terminate()   # Close the PyAudio object just like scanner.close() in Java

# Convert binary data to NumPy array
signal = np.frombuffer(data, dtype=np.int16)

# Plot waveform
plt.figure(figsize=(10, 4))
plt.plot(signal)
# zoom in and out the waveform
plt.xlim(chunk, 2 * chunk)

plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.title('Waveform')


plt.show()

import pyaudio
import wave
import numpy as np
import matplotlib.pyplot as plt

# Open the wave file
wf = wave.open('assets/Cowboy Bebop - Full.wav', 'rb')

# play the song
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(),
                rate=wf.getframerate(), output=True)


# Get the sample rate
sample_rate = wf.getframerate()

# Read the entire audio data
data = wf.readframes(-1)

# Close the wave file
wf.close()

# Convert the binary data to a NumPy array
signal = np.frombuffer(data, dtype=np.int16)

# Separate the channels
left_channel = signal[::2]
right_channel = signal[1::2]

# Choose one of the channels for analysis
signal = left_channel

# Downsample the signal
downsample_factor = 10
downsampled_signal = signal[::downsample_factor]

# Define the size of the smoothing window
window_size = 50

# Create a one-dimensional convolutional kernel
kernel = np.ones(window_size) / window_size

# Convolve the signal with the kernel to smooth it
smoothed_signal = np.convolve(downsampled_signal, kernel, mode='same')

# Create a time array
time = np.arange(len(smoothed_signal)) / (sample_rate / downsample_factor)

# Plot the smoothed signal
plt.figure(figsize=(10, 4))
plt.plot(time, smoothed_signal)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Smoothed Waveform')
plt.show()
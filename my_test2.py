from pydub import AudioSegment

# Convert mp3 to wav file
# audio = AudioSegment.from_mp3('audio_file.mp3')
# audio.export('audio_file.wav', format='wav')

audio = AudioSegment.from_file('assets/Cowboy Bebop - Full.wav')

# Extract sample rate and total duration
sample_rate = audio.frame_rate
total_duration = len(audio) / 1000  # Duration in seconds

print("Sample rate:", sample_rate)
print("Total duration:", total_duration, "seconds")

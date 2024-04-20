import numpy as np
from pydub import AudioSegment
import librosa
import soundfile as sf
from pydub import effects
from scipy.io import wavfile
import noisereduce as nr


def load_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    return audio


# def speed_up(audio, speed_factor):
#     return audio.speedup(playback_speed=speed_factor)

# def slow_down(audio, speed_factor):
#     # Load the audio file
#     y = librosa.load("Rageen Ya Hawa.wav")
#     # Slow down the audio
#     y_slow = librosa.effects.time_stretch(y, speed_factor)
#     # Save the slowed down audio
#     return y_slow

def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
        "frame_rate": int(sound.frame_rate * speed)
    })

    # convert the sound with altered frame rate to a standard frame rate
    # so that regular playback programs will work right. They often only
    # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)


def add_reverb(audio):
    duration = len(audio)  # Get the length of the audio in milliseconds
    return audio.low_pass_filter(500).fade(start=0, duration=duration)


def change_pitch(audio, semitones):
    samples = audio.get_array_of_samples()
    new_samples = librosa.effects.pitch_shift(np.array(samples), audio.frame_rate, semitones)
    new_audio = audio._spawn(new_samples)
    return new_audio


# def noise_suppression(audio, amount):
#     samples = audio.get_array_of_samples()
#     new_samples = librosa.effects.remix(np.array(samples), intervals=librosa.effects.split_top_db(np.array(samples), top_db=amount))
#     new_audio = audio._spawn(new_samples)
#     return new_audio

def noise_suppression(audio):
    rate, data = audio
    # perform noise reduction
    reduced_noise = nr.reduce_noise(y=data, sr=rate)
    return rate, reduced_noise


def remix(audio, segments):
    new_audio = AudioSegment.empty()
    for segment in segments:
        new_audio += audio[segment[0]:segment[1]]
    return new_audio


def main():
    audio = load_audio("Babble.wav")
    audio1 = wavfile.read("Babble.wav")
    fast_audio = speed_change(audio, 2)
    fast_audio.export("fast.mp3", format="mp3")

    slowed = speed_change(audio, 0.5)
    slowed.export("slow.mp3", format="mp3")

    rate, suppressed_audio = noise_suppression(audio1)
    wavfile.write("suppressed.wav", rate, suppressed_audio)

    # reverb_audio = add_reverb(audio)
    # reverb_audio.export("reverb.mp3", format="mp3")

    # high_pitch_audio = change_pitch(audio, 5)
    # high_pitch_audio.export("high_pitch.mp3", format="mp3")

    # low_pitch_audio = change_pitch(audio, -5)
    # low_pitch_audio.export("low_pitch.mp3", format="mp3")

    # remixed_audio = remix(audio, [(1000, 2000), (3000, 4000), (5000, 6000)])
    # remixed_audio.export("remix.mp3", format="mp3")


if __name__ == "__main__":
    main()

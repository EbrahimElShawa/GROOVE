import os
import random
import multiprocessing

import numpy as np
import sounddevice as sd
import soundfile as sf
from pydub import AudioSegment


def process(current_song, preprocessed_songs, finished):
    song = AudioSegment.from_file(current_song)
    for speed_factor in [1.25, 1.5, 2]:
        song = song.speedup(playback_speed=speed_factor)
        new_file_name = f"AudioX{speed_factor}.wav"
        sped_up_song_path = os.path.join('temps', new_file_name)
        song.export(sped_up_song_path, format="wav")
        preprocessed_songs.append(sped_up_song_path)
    finished.set()


class AudioPlayer:
    def __init__(self, update_name_callback, context_callback):
        self.working_directory, self.songs = None, []
        self.original_song, self.current_song, self.stream = None, None, None
        self.current_song_index, self.volume = 0, 0.4
        self.is_playing, self.shuffled = False, False
        self.current_pos, self.length = 0, 0
        self.data, self.frame_rate, self.samples = None, None, None
        self.current_preprocessing_process = None
        self.process_finished_event = multiprocessing.Event()

        self.update_name = update_name_callback
        self.give_context = context_callback
        manager = multiprocessing.Manager()
        self.preprocessed_songs = manager.list()

    def get_audio_files(self, directory_path):
        all_files = os.listdir(directory_path)
        self.working_directory = directory_path
        audio_files = [file for file in all_files if file.endswith('.mp3') or file.endswith('.wav')]
        self.songs = audio_files
        # print(audio_files)  # Debugging

    def play_song(self):
        if self.is_playing:
            self.stop_song()

        self.is_playing = True
        self.data, self.frame_rate = sf.read(self.current_song)     # soundfile implicitly converts from .mp3 to .wav
        self.samples = np.array(self.data)
        self.length = len(self.data) / self.frame_rate
        self.stream = sd.OutputStream(callback=self.callback, channels=2, samplerate=self.frame_rate)
        self.stream.start()

    def callback(self, out_data, frames, time, status):
        start = int(self.current_pos * self.frame_rate)
        stop = start + frames
        if self.is_playing:
            if stop >= len(self.data) - frames:
                self.next_song()

            out_data[:] = self.data[start:stop] * self.volume
            self.current_pos += frames / self.frame_rate

    def pause_song(self):
        if self.stream is not None:
            self.stream.stop()
            self.is_playing = False

    def resume_song(self):
        if self.stream is not None:
            self.stream.start()
            self.is_playing = True

    def stop_song(self):
        if self.stream is not None and self.is_playing:
            self.stream.close()
            self.current_pos = 0
            self.is_playing = False
            self.stream = None

            if self.current_preprocessing_process is not None:
                self.current_preprocessing_process.terminate()
                self.current_preprocessing_process = None

    def fast_forward(self):
        self.current_pos = min(self.current_pos + 10, self.length - 1)

    def rewind(self,):
        self.current_pos = max(self.current_pos - 10, 0)

    def change_speed(self, speed_factor):
        current_pos = self.current_pos
        if speed_factor == 1.0:
            self.current_song = os.path.join(self.working_directory, self.songs[self.current_song_index])
            speed_factor = 0.25  # For division at line 88
        elif speed_factor == 1.25:
            self.current_song = self.preprocessed_songs[0]
        elif speed_factor == 1.5:
            self.current_song = self.preprocessed_songs[1]
        else:                    # speed_factor == 2
            self.current_song = self.preprocessed_songs[2]

        self.play_song()
        self.current_pos = current_pos / speed_factor

    def preprocess_audio(self):
        self.current_preprocessing_process = multiprocessing.Process(
            target=process, args=(self.current_song, self.preprocessed_songs, self.process_finished_event))
        self.current_preprocessing_process.start()

    def next_song(self):
        if self.shuffled:
            new_index = self.current_song_index
            while new_index == self.current_song_index:
                new_index = random.randint(0, len(self.songs) - 1)
            self.current_song_index = new_index
        else:
            self.current_song_index = (self.current_song_index + 1) % len(self.songs)
        self.current_song = os.path.join(self.working_directory, self.songs[self.current_song_index])

        self.play_song()
        self.preprocess_audio()
        self.update_name(self.songs[self.current_song_index])

    def previous_song(self):
        if self.shuffled:
            new_index = self.current_song_index
            while new_index == self.current_song_index:
                new_index = random.randint(0, len(self.songs) - 1)
            self.current_song_index = new_index
        else:
            self.current_song_index = (self.current_song_index - 1) % len(self.songs)
        self.current_song = os.path.join(self.working_directory, self.songs[self.current_song_index])

        self.play_song()
        self.preprocess_audio()
        self.update_name(self.songs[self.current_song_index])

    def read_waveform(self):
        samples = self.samples
        if samples.ndim > 1 and samples.shape[1] == 2:
            samples = samples[:, 0]  # Take one channel if stereo
        samples = samples / np.max(np.abs(samples))  # Normalize

        max_points = 5000
        if len(samples) > max_points:
            factor = len(samples) // max_points
            samples = samples[::factor]
        return samples

    def get_song_duration(self):
        return self.length

    def get_song_position(self):
        if self.stream is not None:
            return self.current_pos
        else:
            return -1

    def set_song_position(self, position):
        self.current_pos = position * self.length

    def set_processed_finished(self):
        self.current_preprocessing_process = None
        self.give_context('Processes have finished')

import os
import threading

import sounddevice as sd
import soundfile as sf
from pydub import AudioSegment


class AudioPlayer:
    def __init__(self):
        self.original_song, self.current_song = None, None
        self.songs, self.preprocessed_songs = [], []
        self.is_playing = False
        self.current_pos, self.length = 0, 0
        self.frame_rate = None
        self.data, self.stream = None, None
        self.volume = 0.4

    def get_audio_files(self, directory_path):
        all_files = os.listdir(directory_path)
        audio_files = [file for file in all_files if file.endswith('.mp3') or file.endswith('.wav')]
        self.songs = audio_files
        # print(audio_files)  # Debugging

    def play_song(self):
        if self.is_playing:
            self.stop_song()
        self.is_playing = True
        self.data, self.frame_rate = sf.read(self.current_song)     # soundfile implicitly converts from .mp3 to .wav
        self.length = len(self.data) / self.frame_rate
        self.stream = sd.OutputStream(callback=self.callback, channels=2, samplerate=self.frame_rate)
        self.stream.start()

    def callback(self, out_data, frames, time, status):
        start = int(self.current_pos * self.frame_rate)
        stop = start + frames
        if self.is_playing:
            if stop >= len(self.data) - frames:
                self.stop_song()

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

    def fast_forward(self):
        self.current_pos = min(self.current_pos + 10, self.length - 1)

    def rewind(self,):
        self.current_pos = max(self.current_pos - 10, 0)

    def change_speed(self, speed_factor):
        current_pos = self.current_pos
        if speed_factor == 1.0:
            self.current_song = self.original_song
            speed_factor = 0.25  # For division at line 88
        elif speed_factor == 1.25:
            self.current_song = self.preprocessed_songs[0]
        elif speed_factor == 1.5:
            self.current_song = self.preprocessed_songs[1]
        elif speed_factor == 2.0:
            self.current_song = self.preprocessed_songs[2]
        else:
            self.current_song = self.preprocessed_songs[3]

        self.play_song()
        self.current_pos = current_pos / speed_factor

        # self.data = np.array([librosa.resample(c, orig_sr=self.frame_rate, target_sr=int(self.frame_rate * 0.5))
        #                       for c in self.data.T]).T

        # self.frame_rate = int(self.frame_rate * 0.5)
        # self.length = len(self.data) / self.frame_rate
        # pitch_shift_factor = -12 / len(self.data)  # Shift the pitch down by one octave
        # self.data = librosa.effects.pitch_shift(self.data.T, sr=self.frame_rate, n_steps=pitch_shift_factor).T

    def preprocess_audio(self):
        def thread():
            self.current_song = self.original_song
            song = AudioSegment.from_file(self.current_song)

            for speed_factor in [1.25, 1.5, 2, 0.8]:
                song = song.speedup(playback_speed=speed_factor)
                new_file_name = f"AudioX{speed_factor}.wav"
                sped_up_song_path = os.path.join('temps', new_file_name)
                song.export(sped_up_song_path, format="wav")
                self.preprocessed_songs.append(sped_up_song_path)
                print(f'Done processing: {speed_factor}')

        preprocessing_thread = threading.Thread(target=thread)
        preprocessing_thread.start()

    def get_song_duration(self):
        return self.length

    def get_song_position(self):
        if self.stream is not None:
            return self.current_pos
        else:
            return -1

    def set_song_position(self, param):
        pass

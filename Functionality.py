import os
import sounddevice as sd
import soundfile as sf


class AudioPlayer:
    def __init__(self):
        self.current_song = None
        self.songs = []
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
        self.data, self.frame_rate = sf.read(self.current_song)
        self.length = len(self.data) / self.frame_rate
        self.stream = sd.OutputStream(callback=self.callback, channels=2, samplerate=self.frame_rate)
        self.stream.start()

    def callback(self, out_data, frames, time, status):
        start = int(self.current_pos * self.frame_rate)
        stop = start + frames
        if self.is_playing:
            # print('stop:', stop)  # Debugging
            # print('Length:', len(self.data))  # Debugging
            if stop >= len(self.data) - frames:
                self.stop_song()
                # print('Every time?')  # Debugging
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

    def speed_up(self):
        pass

    def slow_down(self):
        pass

    def get_song_duration(self):
        return self.length

    def get_song_position(self):
        if self.stream is not None:
            return self.current_pos
        else:
            return -1

    def set_song_position(self, param):
        pass

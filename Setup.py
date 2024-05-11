import os
import Effects
import Functionality

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog


class UIController:
    def __init__(self, widgets):
        self.func = Functionality.AudioPlayer()
        self.widgets = widgets

        self.is_shuffled, self.is_playing = False, False
        self.volume_speed = 1.0

        self.song_progress_timer = QTimer()
        # noinspection PyUnresolvedReferences
        self.song_progress_timer.timeout.connect(self.update_song_progress)
        self.widgets['plus10_button'].clicked.connect(self.func.fast_forward)
        self.widgets['minus10_button'].clicked.connect(self.func.rewind)

        self.volume_bar_setup()
        self.progress_bar_setup()

    def volume_bar_setup(self):
        volume_bar = self.widgets['volume_bar']
        volume_bar.hide()
        volume_bar.setRange(0, 100)
        volume_bar.setValue(0)
        volume_bar.setTickInterval(10)

    def progress_bar_setup(self):
        progress_bar = self.widgets['song_progress']
        progress_bar.setRange(0, 1000)
        progress_bar.setValue(0)
        progress_bar.setTickInterval(5)

    def toggle_pause_play(self, play_button):
        if self.is_playing:  # Playing -> Stopped
            self.func.pause_song()
            play_button.setIcon(QIcon("assets/Play.png"))
            self.is_playing = not self.is_playing
            self.song_progress_timer.stop()
        else:  # Stopped -> Playing
            self.func.resume_song()
            play_button.setIcon(QIcon("assets/Pause.png"))
            self.is_playing = not self.is_playing
            self.song_progress_timer.start(500)

    def toggle_shuffle(self, shuffle_button):  # disabling the button should be done when doing the backend stuff
        Effects.default_clicked_animation(shuffle_button, 500)

        if self.is_shuffled:  # Shuffled -> Not Shuffled
            shuffle_button.setIcon(QIcon("assets/ShuffleInactive.png"))
            self.is_shuffled = not self.is_shuffled
        else:  # Not Shuffled -> Shuffled
            shuffle_button.setIcon(QIcon("assets/ShuffleActive.png"))
            self.is_shuffled = not self.is_shuffled

    def toggle_speed(self, speed_button):
        if self.volume_speed == 1.0:
            self.volume_speed = 1.25
            speed_button.setIcon(QIcon("assets/x1.2Speed.png"))
        elif self.volume_speed == 1.25:
            self.volume_speed = 1.5
            speed_button.setIcon(QIcon("assets/x1.5Speed.png"))
        elif self.volume_speed == 1.5:
            self.volume_speed = 2.0
            speed_button.setIcon(QIcon("assets/x2Speed.png"))
        else:
            self.volume_speed = 1.0
            speed_button.setIcon(QIcon("assets/x1Speed.png"))
        # print(volume_speed)  # Debugging

    def volume_level(self, event):
        # svc = SystemVolumeController()
        volume_bar = self.widgets['volume_bar']
        value = volume_bar.maximum() - ((volume_bar.maximum() - volume_bar.minimum()) *
                                        event.y()) / volume_bar.height()
        volume_bar.setValue(int(value))
        # print(value)  # Debugging
        # svc.set_volume(value)

    def open_file(self, main_window, folder_button):
        # the _ for the filter used, which I don't need
        file_name, _ = QFileDialog.getOpenFileName(main_window, "Select song", "D:/Downloads/Audio/",
                                                   "Audio Files (*.mp3 *.wav)")
        QTimer.singleShot(50, lambda: Effects.enable_animation(folder_button))

        if file_name:
            folder_name = os.path.dirname(file_name)
            if not main_window.pause_button.isEnabled():
                widget_keys = ['pause_button', 'next_button', 'previous_button', 'plus10_button', 'minus10_button',
                               'volume_button', 'shuffle_button', 'effects_button', 'volume_speed', 'song_progress']
                for key in widget_keys:
                    Effects.enable_animation(self.widgets[key])
                Effects.util_bar_animation(main_window.util_bar_animation)

            self.toggle_pause_play(main_window.pause_button)
            self.set_song_name(os.path.basename(file_name))
            self.func.current_song = file_name
            self.func.play_song()
            self.func.get_audio_files(folder_name)

    def set_song_name(self, text):
        song_name = self.widgets['song_name']
        song_name.setText(text)
        Effects.glow_effect(song_name)

    def update_song_progress(self):
        progress_bar = self.widgets['song_progress']
        song_position = self.func.get_song_position()
        song_duration = self.func.get_song_duration()
        if song_position == -1:
            self.toggle_pause_play(self.widgets['pause_button'])
            print('please work')
            return

        current = self.widgets['song_progress'].value()
        progress = (song_position / song_duration) * 1000
        self.widgets['song_progress'].setValue(int(progress))
        Effects.progress_bar_animation(progress_bar, current, progress)
        print(progress)

    @staticmethod
    def toggle_slider(volume_bar):
        Effects.show_slider_animation(volume_bar)


def song_progress(progress_slider, event):
    range_start = progress_slider.minimum()
    range_end = progress_slider.maximum()
    range_width = range_end - range_start
    relative_x = event.x() / progress_slider.width()
    value = range_start + (range_width * relative_x)
    progress_slider.setValue(int(value))
    # print(value)  # Debugging
    # print(progress_slider.value())

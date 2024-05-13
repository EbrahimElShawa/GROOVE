import os
import Effects
import Functionality

from PyQt5.QtCore import QTimer, Qt, QPoint
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog


class UIController:
    def __init__(self, widgets):
        self.func = Functionality.AudioPlayer()
        self.widgets = widgets

        self.is_shuffled, self.is_playing, self.finished = False, False, False
        self.volume_speed = 1.0

        self.song_progress_timer = QTimer()
        # noinspection PyUnresolvedReferences
        self.song_progress_timer.timeout.connect(self.update_song_progress)

        self.set_changes(self.widgets['plus10_button'], self.func.fast_forward)
        self.set_changes(self.widgets['minus10_button'], self.func.rewind)

        self.volume_bar_setup()
        self.progress_bar_setup()

    def volume_bar_setup(self):
        volume_bar = self.widgets['volume_bar']
        volume_bar.hide()
        volume_bar.setRange(0, 100)
        volume_bar.setValue(20)
        volume_bar.setTickInterval(10)

    def progress_bar_setup(self):
        progress_bar = self.widgets['song_progress']
        progress_bar.setRange(0, 1000)
        progress_bar.setValue(0)
        progress_bar.setTickInterval(5)

    def toggle_pause_play(self):
        pause_button = self.widgets['pause_button']
        if self.is_playing:  # Playing -> Stopped
            self.func.pause_song()
            pause_button.setIcon(QIcon("assets/Play.png"))
            self.is_playing = not self.is_playing
            self.song_progress_timer.stop()
        else:  # Stopped -> Playing
            if self.finished:
                self.func.play_song()
                self.toggle_utility_buttons()
                self.finished = False
            else:
                self.func.resume_song()
            pause_button.setIcon(QIcon("assets/Pause.png"))
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

    def toggle_utility_buttons(self):
        widget_keys = ['plus10_button', 'minus10_button', 'effects_button']
        if self.widgets['effects_button'].isEnabled():
            for key in widget_keys:
                Effects.disable_animation(self.widgets[key])
        else:
            for key in widget_keys:
                Effects.enable_animation(self.widgets[key])

    def volume_level(self, event, value, slider=False):
        if slider:
            self.func.volume = value / 50
            return
        volume_bar = self.widgets['volume_bar']
        value = int(volume_bar.maximum() - ((volume_bar.maximum() - volume_bar.minimum()) *
                                            event.y()) / volume_bar.height())
        volume_bar.setValue(value)
        set_volume_level(self.widgets['volume_level'], value)
        self.func.volume = value / 50
        # print(value)  # Debugging

    def set_changes(self, widget, function):
        widget.clicked.connect(function)
        widget.clicked.connect(self.update_song_progress)

    def open_file(self, main_window, folder_button):
        # the _ for the filter used, which I don't need
        file_name, _ = QFileDialog.getOpenFileName(main_window, "Select song", "D:/Downloads/Audio/",
                                                   "Audio Files (*.mp3 *.wav)")
        QTimer.singleShot(50, lambda: Effects.enable_animation(folder_button))

        if file_name:
            Effects.move_animation(self.widgets['song_progress'], b'value', self.widgets['song_progress'].value(), 0)
            if not main_window.pause_button.isEnabled():
                widget_keys = ['pause_button', 'next_button', 'previous_button', 'plus10_button', 'minus10_button',
                               'volume_button', 'shuffle_button', 'effects_button', 'volume_speed', 'song_progress']
                for key in widget_keys:
                    Effects.enable_animation(self.widgets[key])
                self.widgets['time_label'].show()
                Effects.util_bar_animation(main_window.util_bar_animation)

            self.set_song_name(os.path.basename(file_name))
            self.func.current_song = file_name

            if not self.is_playing:
                self.toggle_pause_play()
            self.func.play_song()

            folder_name = os.path.dirname(file_name)
            self.func.get_audio_files(folder_name)
            self.give_context(folder_name)

    def set_song_name(self, text):
        song_name = self.widgets['song_name']
        song_name.setText(text)
        song_name.setAlignment(Qt.AlignCenter)
        Effects.glow_effect(song_name)

    def update_song_progress(self):
        progress_bar = self.widgets['song_progress']
        song_position = self.func.get_song_position()
        song_duration = self.func.get_song_duration()

        if song_position == -1:
            self.finished = True
            self.toggle_pause_play()
            self.toggle_utility_buttons()
            return

        current = progress_bar.value()
        progress = (song_position / song_duration) * 1000

        self.update_time_label(self.widgets['time_label'], song_position, progress)
        Effects.move_animation(progress_bar, b'value', current, progress)
        # print(progress) # Debugging

    @staticmethod
    def update_time_label(time_label, song_position, progress):
        minutes = int(song_position // 60)  # // for only the integer part
        seconds = int(song_position % 60)

        if minutes < 10:
            minutes = f'0{minutes}'
        if seconds < 10:
            seconds = f'0{seconds}'

        time_label.setText(f'{minutes}:{seconds}')
        time_label.setAlignment(Qt.AlignCenter)

        new_position = QPoint(int(80 + progress * 0.98), 120)  # Base x-axis for time_label = 78
        Effects.move_animation(time_label, b'pos', time_label.pos(), new_position)

    def song_progress(self, event):
        progress_slider = self.widgets['song_progress']
        range_start = progress_slider.minimum()
        range_end = progress_slider.maximum()
        range_width = range_end - range_start
        relative_x = event.x() / progress_slider.width()
        value = range_start + (range_width * relative_x)
        progress_slider.setValue(int(value))
        if value >= 999:
            self.finished = True
        # print(value)  # Debugging
        # song_progress.sliderReleased.connect(lambda: self.func.set_song_position(song_progress.value())) da heck?!

    @staticmethod
    def toggle_slider(volume_bar):
        Effects.show_slider_animation(volume_bar)

    def give_context(self, folder_name):
        context_label = self.widgets['context_label']
        if context_label.text() == f'Importing music from: {folder_name}/':
            return

        context_label.setText(f'Importing music from: {folder_name}/')
        context_label.show()
        QTimer.singleShot(5000, lambda: Effects.fading_label_animation(context_label))


def set_volume_level(volume_label, value):
    volume_label.setText(f'{value}')
    volume_label.setAlignment(Qt.AlignCenter)

    volume_label.show()
    if hasattr(volume_label, 'timer'):
        print('Timer is active')
        volume_label.animation_countdown.stop()
        if hasattr(volume_label, 'animation'):
            volume_label.animation.stop()
    # Create a new timer and start the animation after the delay
    volume_label.animation_countdown = QTimer()
    volume_label.animation_countdown.setSingleShot(True)
    # noinspection PyUnresolvedReferences
    volume_label.animation_countdown.timeout.connect(lambda: Effects.fading_label_animation(volume_label))
    volume_label.animation_countdown.start(2500)



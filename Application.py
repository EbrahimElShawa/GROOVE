from warnings import filterwarnings

from PyQt5 import uic
from PyQt5.QtCore import QTimer, QEvent
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout

import Effects
import Setup

filterwarnings("ignore", category=DeprecationWarning)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('Application.ui', self)
        self.waveform_layout = QVBoxLayout()

        # Set the QVBoxLayout instance as the layout of the central widget
        self.centralWidget().setLayout(self.waveform_layout)

        self.widgets = {"previous_button": self.previous_button, "plus10_button": self.plus10_button,
                        "folder_button": self.folder_button, "effects_button": self.effects_button,
                        "minus10_button": self.minus10_button, "volume_button": self.volume_button,
                        "shuffle_button": self.shuffle_button, "volume_speed": self.volume_speed,
                        "pause_button": self.pause_button, "next_button": self.next_button,
                        "song_progress": self.song_progress, "song_name": self.song_name,
                        "time_label": self.time_label, "volume_level": self.volume_level,
                        "utility_bar": self.utility_bar, "volume_bar": self.volume_bar,
                        "context_label": self.context_label, "waveform_widget": self.waveform_widget,
                        "waveform_layout": self.waveform_layout}

        self.initial_setup()
        self.link_effects()
        self.setup = Setup.UIController(self.widgets)

    def eventFilter(self, source, event):
        if event.type() == QEvent.MouseButtonPress and isinstance(source, QWidget):
            if self.volume_bar.isAncestorOf(source):
                if self.volume_bar.rect().contains(event.pos()):
                    self.setup.volume_level(event, None)

            elif self.volume_bar.isVisible():
                self.volume_bar.hide()
                self.volume_level.hide()
                QTimer.singleShot(50, lambda: Effects.enable_animation(self.volume_button))

            if self.song_progress.isAncestorOf(source):
                if self.song_progress.rect().contains(event.pos()):
                    self.setup.song_progress(event)
                    # BackEnd.set_song_position(self.song_progress, event)

        return super(MainWindow, self).eventFilter(source, event)

    def initial_setup(self):
        QApplication.instance().installEventFilter(self)  # basically, it installs the event filter so whenever an
        # event happens in the application, it will be checked by the eventFilter method first before the event is
        # processed by the application. This is useful for handling events that are not handled by the application.
        self.widgets['waveform_widget'] = Setup.WaveformWidget(self.waveform_widget)

        widget_keys = ['pause_button', 'next_button', 'previous_button', 'plus10_button', 'minus10_button',
                       'volume_button', 'shuffle_button', 'effects_button', 'volume_speed', 'song_progress']
        for key in widget_keys:
            Effects.disable_animation(self.widgets[key], dur=0)

        self.shuffle_button.clicked.connect(lambda: self.setup.toggle_shuffle(self.shuffle_button))
        self.volume_speed.clicked.connect(lambda: self.setup.toggle_speed(self.volume_speed))
        self.folder_button.clicked.connect(lambda: self.setup.open_file(self, self.folder_button))
        QTimer.singleShot(50, lambda: self.volume_bar.valueChanged.
                          connect(lambda: self.setup.volume_level(None, self.volume_bar.value(), True)))
        self.effects_button.clicked.connect(lambda: self.setup.open_effects())

        self.time_label.hide()
        self.volume_level.hide()
        self.context_label.hide()

    def link_effects(self):
        self.pause_button.pressed.connect(lambda: Effects.default_pressed_animation(self.pause_button))
        self.pause_button.released.connect(
            lambda: QTimer.singleShot(50, lambda: Effects.default_released_animation(self.pause_button)))
        self.pause_button.clicked.connect(lambda: self.setup.toggle_pause_play())

        self.next_button.pressed.connect(lambda: Effects.default_pressed_animation(self.next_button))
        self.next_button.released.connect(
            lambda: QTimer.singleShot(50, lambda: Effects.default_released_animation(self.next_button)))
        self.next_button.clicked.connect(lambda: Effects.default_clicked_animation(self.next_button, 1500))

        self.previous_button.pressed.connect(lambda: Effects.default_pressed_animation(self.previous_button))
        self.previous_button.released.connect(
            lambda: QTimer.singleShot(50, lambda: Effects.default_released_animation(self.previous_button)))
        self.previous_button.clicked.connect(lambda: Effects.default_clicked_animation(self.previous_button, 1500))

        self.plus10_button.pressed.connect(lambda: Effects.default_pressed_animation(self.plus10_button))
        self.plus10_button.released.connect(
            lambda: QTimer.singleShot(50, lambda: Effects.default_released_animation(self.plus10_button)))
        self.plus10_button.clicked.connect(lambda: Effects.default_clicked_animation(self.plus10_button, 100))

        self.minus10_button.pressed.connect(lambda: Effects.default_pressed_animation(self.minus10_button))
        self.minus10_button.released.connect(
            lambda: QTimer.singleShot(50, lambda: Effects.default_released_animation(self.minus10_button)))
        self.minus10_button.clicked.connect(lambda: Effects.default_clicked_animation(self.minus10_button, 100))

        self.volume_button.pressed.connect(lambda: Effects.default_pressed_animation(self.volume_button))
        self.volume_button.released.connect(
            lambda: QTimer.singleShot(50, lambda: Effects.default_released_animation(self.volume_button)))
        self.volume_button.clicked.connect(lambda: (Effects.disable_animation(self.volume_button),
                                                    Effects.show_slider_animation(self.volume_bar)))

        self.shuffle_button.pressed.connect(lambda: Effects.default_pressed_animation(self.shuffle_button))
        self.shuffle_button.released.connect(
            lambda: QTimer.singleShot(50, lambda: Effects.default_released_animation(self.shuffle_button)))

        self.volume_speed.pressed.connect(lambda: Effects.default_pressed_animation(self.volume_speed))
        self.volume_speed.released.connect(
            lambda: QTimer.singleShot(50, lambda: Effects.default_released_animation(self.volume_speed)))

        self.folder_button.pressed.connect(lambda: Effects.default_pressed_animation(self.folder_button))
        self.folder_button.released.connect(
            lambda: QTimer.singleShot(50, lambda: Effects.default_released_animation(self.folder_button, 45)))
        self.folder_button.clicked.connect(lambda: Effects.disable_animation(self.folder_button))

        self.effects_button.pressed.connect(lambda: Effects.default_pressed_animation(self.effects_button))
        self.effects_button.released.connect(
            lambda: QTimer.singleShot(50, lambda: Effects.default_released_animation(self.effects_button, 50)))
        self.effects_button.clicked.connect(lambda: Effects.disable_animation(self.effects_button))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("assets/Groove.ico"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

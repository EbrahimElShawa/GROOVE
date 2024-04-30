from PyQt5 import QtGui
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QGraphicsDropShadowEffect


class Effects:
    def __init__(self):
        pass

    @staticmethod
    def setup_glow_effect(button):
        effect = QGraphicsDropShadowEffect()
        effect.setColor(QtGui.QColor("white"))
        effect.setOffset(0, 0)
        button.setGraphicsEffect(effect)

        animation = QPropertyAnimation(effect, b"blurRadius")
        animation.setDuration(3000)  # 3000 milliseconds = 3 seconds
        animation.setStartValue(0)  # No glow
        animation.setEndValue(10)  # Maximum glow
        animation.setLoopCount(-1)  # Loop indefinitely
        animation.setEasingCurve(QEasingCurve.OutCubic)

        button.clicked.connect(lambda: Effects.toggle_animation(animation))

    @staticmethod
    def toggle_animation(animation):
        if animation.state() == QPropertyAnimation.Running:
            animation.stop()
        else:
            animation.start()


# import necessary libraries for BackEnd
class BackEnd:
    def __init__(self):
        pass

    def load_audio(self, file_path):
        pass

    def speed_change(self, sound, speed=1.0):
        pass

    def add_reverb(self, audio):
        pass

    # add other methods related to back-end functionalities

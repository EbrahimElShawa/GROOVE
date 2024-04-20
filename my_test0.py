from PyQt5 import uic
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsOpacityEffect


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('test0.ui', self)

        # Create an instance of QGraphicsOpacityEffect
        self.effect = QGraphicsOpacityEffect(self.shuffle_button)

        # Set the effect to the shuffle_button
        self.shuffle_button.setGraphicsEffect(self.effect)

        # Create an instance of QPropertyAnimation
        self.animation = QPropertyAnimation(self.effect, b"opacity")

        # Set the duration of the animation
        self.animation.setDuration(1000)  # 1000 milliseconds = 1 second

        # Set the start and end values of the animation
        self.animation.setStartValue(1)  # Fully opaque
        self.animation.setEndValue(0)  # Fully transparent

        # Set the easing curve of the animation
        self.animation.setEasingCurve(QEasingCurve.OutCubic)

        # Connect the clicked signal of the shuffle_button to the start of the animation
        self.shuffle_button.clicked.connect(self.animation.start)

    def on_shuffle_button_clicked(self):
        print("Shuffle button clicked!")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

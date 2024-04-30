from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QMainWindow
from Functionality import Effects


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('test0.ui', self)
        Effects.setup_glow_effect(self.shuffle_button)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

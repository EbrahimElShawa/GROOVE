import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QIcon, QColor

class IconButton(QPushButton):
    def __init__(self, icon_path, parent=None):
        super().__init__(parent)
        self.setIcon(QIcon(icon_path))
        self.setIconSize(self.size())
        self.setFlat(True)  # Make the button flat without any border or background
        self.setStyleSheet("background-color: transparent; border: none;")  # Set background and border to transparent

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Icon-Only Button Example")
        self.setGeometry(100, 100, 200, 200)

        layout = QVBoxLayout()

        # Create an icon button
        icon_button = IconButton("P:/University/Utility Pictures/Tomato.png")
        layout.addWidget(icon_button)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())


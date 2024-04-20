# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test0.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AudioProcessor(object):
    def setupUi(self, AudioProcessor):
        AudioProcessor.setObjectName("AudioProcessor")
        AudioProcessor.setWindowModality(QtCore.Qt.ApplicationModal)
        AudioProcessor.setEnabled(True)
        AudioProcessor.resize(1200, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AudioProcessor.sizePolicy().hasHeightForWidth())
        AudioProcessor.setSizePolicy(sizePolicy)
        AudioProcessor.setMinimumSize(QtCore.QSize(1200, 700))
        AudioProcessor.setMaximumSize(QtCore.QSize(1200, 700))
        AudioProcessor.setStyleSheet("")
        self.main_window = QtWidgets.QWidget(AudioProcessor)
        palette = QtGui.QPalette()
        gradient = QtGui.QLinearGradient(1.0, 0.0, 1.0, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 142, 255, 254))
        gradient.setColorAt(1.0, QtGui.QColor(0, 26, 75))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 1.0, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 142, 255, 254))
        gradient.setColorAt(1.0, QtGui.QColor(0, 26, 75))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 1.0, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 142, 255, 254))
        gradient.setColorAt(1.0, QtGui.QColor(0, 26, 75))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 1.0, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 142, 255, 254))
        gradient.setColorAt(1.0, QtGui.QColor(0, 26, 75))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 1.0, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 142, 255, 254))
        gradient.setColorAt(1.0, QtGui.QColor(0, 26, 75))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 1.0, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 142, 255, 254))
        gradient.setColorAt(1.0, QtGui.QColor(0, 26, 75))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 1.0, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 142, 255, 254))
        gradient.setColorAt(1.0, QtGui.QColor(0, 26, 75))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 1.0, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 142, 255, 254))
        gradient.setColorAt(1.0, QtGui.QColor(0, 26, 75))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 1.0, 0.5)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(85, 142, 255, 254))
        gradient.setColorAt(1.0, QtGui.QColor(0, 26, 75))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.main_window.setPalette(palette)
        self.main_window.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:0.5, stop:0 rgba(85, 142, 255, 254), stop:1 rgba(0, 26, 75, 255));")
        self.main_window.setObjectName("main_window")
        self.utilityBar = QtWidgets.QWidget(self.main_window)
        self.utilityBar.setEnabled(True)
        self.utilityBar.setGeometry(QtCore.QRect(0, 580, 1200, 120))
        self.utilityBar.setMinimumSize(QtCore.QSize(1200, 120))
        self.utilityBar.setMaximumSize(QtCore.QSize(1200, 120))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(29, 0, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 0, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 0, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 0, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 0, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 0, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 0, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 0, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(29, 0, 112))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.utilityBar.setPalette(palette)
        self.utilityBar.setToolTipDuration(0)
        self.utilityBar.setStyleSheet("QWidget {\n"
"    border-radius: 25px 25px 0px 0px;\n"
"    background-color: #1D0070;\n"
"}")
        self.utilityBar.setObjectName("utilityBar")
        self.play_button = QtWidgets.QPushButton(self.utilityBar)
        self.play_button.setEnabled(True)
        self.play_button.setGeometry(QtCore.QRect(585, 30, 50, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_button.sizePolicy().hasHeightForWidth())
        self.play_button.setSizePolicy(sizePolicy)
        self.play_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.play_button.setToolTip("")
        self.play_button.setToolTipDuration(-1)
        self.play_button.setWhatsThis("")
        self.play_button.setStyleSheet("\n"
"QPushButton:pressed {\n"
"        padding: 3px;\n"
"    }")
        self.play_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_button.setIcon(icon)
        self.play_button.setIconSize(QtCore.QSize(50, 50))
        self.play_button.setFlat(False)
        self.play_button.setObjectName("play_button")
        self.effButton1 = QtWidgets.QPushButton(self.main_window)
        self.effButton1.setEnabled(True)
        self.effButton1.setGeometry(QtCore.QRect(700, 140, 40, 35))
        self.effButton1.setAutoFillBackground(False)
        self.effButton1.setStyleSheet("QPushButton {\n"
"    color: rgb(190, 200, 186);\n"
"    border-style: outset;\n"
"border-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.17, y1:0.147727, x2:0.556818, y2:0.614, stop:0 rgba(218, 149, 255, 255), stop:1 rgba(9, 20, 84, 255));\n"
"}\n"
"\n"
"\n"
"")
        self.effButton1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("assets/Effects.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.effButton1.setIcon(icon1)
        self.effButton1.setIconSize(QtCore.QSize(35, 35))
        self.effButton1.setObjectName("effButton1")
        self.song_name = QtWidgets.QLabel(self.main_window)
        self.song_name.setGeometry(QtCore.QRect(450, 10, 500, 60))
        self.song_name.setMinimumSize(QtCore.QSize(491, 0))
        self.song_name.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.125, x2:1, y2:1, stop:0 rgba(88, 88, 88, 255), stop:1 rgba(187, 187, 187, 255));\n"
"font: 14pt \"Forte\";\n"
"color: rgb(255, 255, 255);\n"
"text-align: center;\n"
"border-radius: 15px;")
        self.song_name.setObjectName("song_name")
        AudioProcessor.setCentralWidget(self.main_window)
        self.actionWelcome = QtWidgets.QAction(AudioProcessor)
        self.actionWelcome.setObjectName("actionWelcome")

        self.retranslateUi(AudioProcessor)
        QtCore.QMetaObject.connectSlotsByName(AudioProcessor)

    def retranslateUi(self, AudioProcessor):
        _translate = QtCore.QCoreApplication.translate
        AudioProcessor.setWindowTitle(_translate("AudioProcessor", "Audio Proc. 1"))
        self.song_name.setText(_translate("AudioProcessor", "<html><head/><body><p align=\"center\"><span style=\" color:#ffffff;\">The name of the Song</span></p></body></html>"))
        self.actionWelcome.setText(_translate("AudioProcessor", "Welcome!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AudioProcessor = QtWidgets.QMainWindow()
    ui = Ui_AudioProcessor()
    ui.setupUi(AudioProcessor)
    AudioProcessor.show()
    sys.exit(app.exec_())

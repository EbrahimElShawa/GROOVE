import random

from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QSize, QTimer, QRect
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QGraphicsDropShadowEffect


def default_pressed_animation(widget):
    widget.animation = QPropertyAnimation(widget, b"iconSize")
    widget.animation.setDuration(100)
    widget.animation.setStartValue(widget.iconSize())
    widget.animation.setEndValue(widget.iconSize() * 0.95)
    widget.animation.setEasingCurve(QEasingCurve.OutCubic)
    widget.animation.start()


def default_released_animation(widget, sz=70):
    widget.animation = QPropertyAnimation(widget, b"iconSize")
    widget.animation.setDuration(100)
    widget.animation.setStartValue(widget.iconSize())
    widget.animation.setEndValue(QSize(sz, sz))
    widget.animation.setEasingCurve(QEasingCurve.OutCubic)
    widget.animation.start()


def default_clicked_animation(button, period=800):
    disable_animation(button)
    QTimer.singleShot(period, lambda: enable_animation(button))


def disable_animation(widget, end_value=0.65, dur=80):  # disabling the button should be done when doing the backend stuff
    widget.setEnabled(False)

    effect = QGraphicsOpacityEffect(widget)
    widget.setGraphicsEffect(effect)
    widget.animation = QPropertyAnimation(effect, b"opacity")
    widget.animation.setStartValue(1)
    widget.animation.setEndValue(end_value)
    widget.animation.setDuration(dur)
    widget.animation.start()


def enable_animation(widget, start_value=0.65):
    widget.setEnabled(True)

    effect = QGraphicsOpacityEffect(widget)
    widget.setGraphicsEffect(effect)
    widget.animation = QPropertyAnimation(effect, b"opacity")
    widget.animation.setStartValue(start_value)
    widget.animation.setEndValue(1)
    widget.animation.setDuration(100)
    widget.animation.start()


def show_slider_animation(volume_bar):
    start_rect = QRect(volume_bar.x(), volume_bar.y() + 30, volume_bar.width(), volume_bar.height())
    end_rect = volume_bar.geometry()
    volume_bar.show()

    volume_bar.geometry_animation = QPropertyAnimation(volume_bar, b"geometry")
    volume_bar.geometry_animation.setDuration(50)
    volume_bar.geometry_animation.setStartValue(start_rect)
    volume_bar.geometry_animation.setEndValue(end_rect)
    volume_bar.geometry_animation.start()


def glow_effect(widget):
    effect = QGraphicsDropShadowEffect()
    effect.setColor(get_random_color(has_green=True))
    # I want the effect to be outside the button by a little bit
    effect.setOffset(0)
    widget.setGraphicsEffect(effect)

    # Animation for the "growing" phase
    widget.grow_animation = QPropertyAnimation(effect, b"blurRadius")
    widget.grow_animation.setDuration(2000)  # 1500 milliseconds = 1.5 seconds
    widget.grow_animation.setStartValue(50)  # No glow
    widget.grow_animation.setEndValue(300)  # Maximum glow
    widget.grow_animation.setEasingCurve(QEasingCurve.OutInSine)

    # Animation for the "shrinking" phase
    widget.shrink_animation = QPropertyAnimation(effect, b"blurRadius")
    widget.shrink_animation.setDuration(1000)  # 1500 milliseconds = 1.5 seconds
    widget.shrink_animation.setStartValue(300)  # Maximum glow
    widget.shrink_animation.setEndValue(50)  # No glow
    widget.shrink_animation.setEasingCurve(QEasingCurve.OutInSine)

    widget.grow_animation.start()
    # noinspection PyUnresolvedReferences
    widget.grow_animation.finished.connect(widget.shrink_animation.start)
    # noinspection PyUnresolvedReferences
    widget.shrink_animation.finished.connect(widget.grow_animation.start)


def util_bar_animation(widget):
    effect = QGraphicsDropShadowEffect(widget)
    effect.setColor(QColor(0, 255, 255))  # Light blue color
    effect.setOffset(0)
    widget.setGraphicsEffect(effect)

    widget.grow_animation = QPropertyAnimation(effect, b"blurRadius")
    widget.grow_animation.setDuration(250)
    widget.grow_animation.setStartValue(0)
    widget.grow_animation.setEndValue(250)
    widget.grow_animation.setEasingCurve(QEasingCurve.OutInSine)

    widget.shrink_animation = QPropertyAnimation(effect, b"blurRadius")
    widget.shrink_animation.setDuration(250)
    widget.shrink_animation.setStartValue(250)
    widget.shrink_animation.setEndValue(0)
    widget.shrink_animation.setEasingCurve(QEasingCurve.OutInSine)

    widget.grow_animation.start()
    # noinspection PyUnresolvedReferences
    widget.grow_animation.finished.connect(widget.shrink_animation.start)
    # noinspection PyUnresolvedReferences
    widget.shrink_animation.finished.connect(widget.deleteLater)


def get_random_color(has_green):
    if has_green:
        red = random.randrange(256)
        green = random.randrange(150)
        blue = random.randrange(150)
    else:
        red = random.randrange(256)
        green = random.randrange(256)
        blue = random.randrange(150)

    return QColor(red, green, blue)


def move_animation(widget, prob, old_value, new_value):
    widget.animation = QPropertyAnimation(widget, prob)
    widget.animation.setDuration(500)
    widget.animation.setStartValue(old_value)
    widget.animation.setEndValue(new_value)
    widget.animation.setEasingCurve(QEasingCurve.InOutQuad)
    widget.animation.start()


def fading_label_animation(widget):
    effect = QGraphicsOpacityEffect(widget)
    widget.setGraphicsEffect(effect)

    widget.animation = QPropertyAnimation(effect, b"opacity")
    widget.animation.setDuration(1000)
    widget.animation.setStartValue(1)
    widget.animation.setEndValue(0)
    widget.animation.setEasingCurve(QEasingCurve.InOutQuad)

    widget.animation.start()
    # noinspection PyUnresolvedReferences
    widget.animation.finished.connect(effect.deleteLater)
    # noinspection PyUnresolvedReferences
    widget.animation.finished.connect(widget.hide)


class Effects:
    def __init__(self):
        pass

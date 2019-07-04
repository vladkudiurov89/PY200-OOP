import os

os.environ[
    'QT_QPA_PLATFORM_PLUGIN_PATH'] = 'C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\PySide2\\plugins\\platforms'

import sys

# Подключаем модули QApplication и QLabel
from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPainter, QBrush
from PySide2.QtCore import Qt, QPoint

# Импортируйте свой файл с фигурами
from PY_200_2_1_figure import Rectangle, Figure, Ellipse


class FigureWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Рисовалка фигур')
        self.__figures = []

    def set_figures(self, figures):
        self.__figures = figures

    def paintEvent(self, event):
        painter = QPainter(self)
        reset_brush = painter.brush()
        for figure in self.__figures:
            if not isinstance(figure, Figure):
                continue

            if isinstance(figure, Rectangle):
                painter.setBrush(QBrush(Qt.red))
                painter.drawRect(figure.a(), figure.b(), figure.w(), figure.h())
                continue

            if isinstance(figure, Ellipse):
                painter.setBrush(QBrush(Qt.green))
                painter.drawEllipse(figure.a(), figure.b(), figure.w(), figure.h())
                continue

            if isinstance(figure, CloseFigure):
                painter.setBrush(QBrush(Qt.blue))
                points = []
                for point in figure:
                    points.append(QPoint(point['x'], point['y']))
                painter.drawPolygon(points)
                continue


if __name__ == '__main__':
    app = QApplication(sys.argv)
    figure_widget = FigureWidget()

    # Создайте список фигур
    figures = [Rectangle(10, 20, 100, 200), Rectangle(100, 20, 50, 100)]
    # figures_1 = [Ellipse(10, 20), Ellipse(100, 20)]

    figure_widget.set_figures(figures)

    figure_widget.show()
    sys.exit(app.exec_())

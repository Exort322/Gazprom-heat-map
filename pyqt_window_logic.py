from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QDoubleValidator
from plt_graph import HeatMap
from pyqt_MainWindow_interface import *


class HeatMapWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, data):
        super().__init__()
        self.setupUi(self)

        # Создаем валидатор, разрешающий только числа с плавающей точкой
        validator = QDoubleValidator(self)
        validator.setNotation(QDoubleValidator.StandardNotation)  # Обычная запись
        self.depth_lineEdit.setValidator(validator)

    def plot(self, data):
        try:
            # Создаем экземпляр HeatMap
            self.heatmap = HeatMap(*data)

            # Вызываем метод chart для создания графика
            self.heatmap.chart()

            # Очищаем предыдущий график, если он был
            for i in reversed(range(self.graph_layout.count())):
                self.graph_layout.itemAt(i).widget().setParent(None)

            # Добавляем новый график в виджет
            self.graph_layout.addWidget(self.heatmap.canvas)

            # Обновляем отображение
            self.heatmap.canvas.draw()
        except Exception as e:
            print(e)

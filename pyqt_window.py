import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from plt_graph import HeatMap
class HeatMapWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Установка основной конфигурации окна
        self.setWindowTitle('Тепловая карта')
        self.setGeometry(100, 100, 800, 600)

        # Создание центрального виджета и вертикального расположения
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # Создание FigureCanvas для отображения графика
        self.canvas = FigureCanvas(Figure(figsize=(10, 8)))
        layout.addWidget(self.canvas)

        # Установка центрального виджета
        self.setCentralWidget(central_widget)

        # Пример данных
        grid_x, grid_y = np.meshgrid(np.linspace(0, 100, 100), np.linspace(0, 100, 100))
        grid_z = np.sin(grid_x / 10) * np.cos(grid_y / 10)
        heatmap = HeatMap(grid_x, grid_y, grid_z, 0, 100, 0, 100, 10)

        # Построение графика
        heatmap.chart(self.canvas)


# Основной код для запуска PyQt приложения
app = QApplication(sys.argv)
window = HeatMapWindow()
window.show()
sys.exit(app.exec_())
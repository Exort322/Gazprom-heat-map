from PyQt5.QtWidgets import QPushButton, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QFont
from plt_graph import HeatMap


class HeatMapWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()
        # Установка основной конфигурации окна
        self.setWindowTitle('Тепловая карта')
        self.setFixedSize(1400, 700)

        self.load = QPushButton(self)
        self.load.setGeometry(1100, 600, 250, 50)
        self.load.setText("Загрузить график")
        self.load.setFont(QFont("Arial", 11))
        self.load.clicked.connect(lambda: self.plot(data))

        # Контейнер для графика
        self.graph_widget = QWidget(self)
        self.graph_widget.setGeometry(0, 50, 700, 600)

        # Лейаут для размещения графиков
        self.graph_layout = QVBoxLayout(self.graph_widget)

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

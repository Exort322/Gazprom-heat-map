from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5.QtGui import QDoubleValidator
from plt_graph import HeatMap
from pyqt_MainWindow_interface import *
from file_dialog import *
from interpolate import *


class HeatMapWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Создаем валидатор, разрешающий только числа с плавающей точкой
        validator = QDoubleValidator(self)
        validator.setNotation(QDoubleValidator.StandardNotation)  # Обычная запись
        self.depth_lineEdit.setValidator(validator)

        self.file_path_btn.clicked.connect(self.choice_file)
        # строка с указанием пути
        self.path_label = QLabel(self.centralwidget)
        self.path_label.setGeometry(10, 135, 400, 30)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.path_label.setFont(font)

        # подключение кнопки загрузки графика
        self.load_btn.clicked.connect(self.plot)
        # путь к csv файлу
        self.file_path = None

    def choice_file(self):
        # получение пути к файлу
        ex = File_dialog()
        filepath = ex.openFileNameDialog()
        if filepath != None:
            self.file_path = filepath

        if self.file_path:
            # Добавление надписи с путем
            self.path_label.clear()
            self.path_label.setText(self.file_path)
            self.path_label.show()

    def plot(self):
        try:
            """Загрузка графика"""
            depth = float(self.depth_lineEdit.text().replace(",", "."))  # Глубина для построения тепловой карты

            data = InterpolateData(depth, self.file_path)  # Получение интерполированных данных
            interp_data = InterpolateData.interpolate(data)

            graph = HeatMap(*interp_data)  # Отрисовка графика
            graph.chart()



        except Exception as e:
            print(e)

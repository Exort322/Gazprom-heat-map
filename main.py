from interpolate import *
from PyQt5.QtWidgets import QApplication
from pyqt_window_logic import *
import sys


if __name__ == "__main__":
    depth = 45  # Глубина для построения тепловой карты
    data = InterpolateData(depth, "thermometric_measurements.csv")
    interp_data = InterpolateData.interpolate(data)
    # Основной код для запуска PyQt приложения
    app = QApplication(sys.argv)
    window = HeatMapWindow(interp_data)
    window.show()
    sys.exit(app.exec_())
from PyQt5.QtWidgets import QApplication
from pyqt_window_logic import *
import sys

if __name__ == "__main__":
    # Основной код для запуска PyQt приложения
    app = QApplication(sys.argv)
    window = HeatMapWindow()
    window.show()
    sys.exit(app.exec_())

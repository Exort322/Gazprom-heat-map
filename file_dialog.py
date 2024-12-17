from PyQt5.QtWidgets import QWidget, QFileDialog


class File_dialog(QWidget):

    def __init__(self):
        super().__init__()

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Выберите файл", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            return fileName

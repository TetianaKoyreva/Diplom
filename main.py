import sys
import pymysql
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

from ui_main import Ui_MainWindow

class LaborProtection(QMainWindow):
    def __init__(self):
        super(LaborProtection, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LaborProtection()
    window.show()


    sys.exit(app.exec())


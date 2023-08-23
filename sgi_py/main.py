import sys
from models.main_page import *
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox

if __name__ == "__main__":
    qt = QApplication(sys.argv)
    loadUi = MainPage() 
    loadUi.show()
    qt.exec_()
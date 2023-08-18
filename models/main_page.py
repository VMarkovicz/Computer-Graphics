import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QPainter, QBrush, QPen, QMouseEvent
from PyQt5.QtCore import Qt
from design.design import *
import pyautogui

class MainPage(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphics.setScene(self.scene)
        self.setWindowButton.clicked.connect(self.paintEvent)
        self.pen = QtGui.QPen(QtCore.Qt.green)
        self.initial_point = None
        self.final_point = None

        """ 
        for i in range(16): 455 no x, 106 y
            for j in range(16):
                r = QtCore.QRectF(QtCore.QPointF(i*side, j*side), QtCore.QSizeF(side, side))
                self.scene.addRect(r, self.pen) """

    def mouseDoubleClickEvent(self, event): #point
        r = QtCore.QRectF(event.pos(), QtCore.QSizeF(5, 5))
        self.scene.addRect(r, self.pen)

    """ def mousePressEvent(self, event): #line
        self.initial_point = event.pos()
        r = QtCore.QLineF(QtCore.QPointF(10,10),QtCore.QPointF(50,50))
        self.scene.addLine(r,self.pen)
    def mouseReleaseEvent(self, event):
        self.final_point = event.pos()
        r = QtCore.QLineF(self.initial_point,self.final_point)
        self.scene.addLine(r,self.pen) """
        

    


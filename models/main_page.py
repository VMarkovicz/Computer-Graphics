import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QPainter, QBrush, QPen, QMouseEvent, QPolygon, QPolygonF
from PyQt5.QtCore import Qt
import pyautogui

from design.design import *

class MainPage(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphics.setScene(self.scene)
        self.setWindowButton.clicked.connect(self.paintEvent)
        self.pen = QtGui.QPen(QtCore.Qt.green, 3)
        self.brush = QtGui.QBrush(QtCore.Qt.red)
        self.initial_point = None
        self.final_point = None
        self.point_button.clicked.connect(self.criar_ponto)
        self.inicia_eixo()
        self.pen = QtGui.QPen(QtCore.Qt.black,5)
        self.line_button.clicked.connect(self.criar_linha)
        self.triangle_button.clicked.connect(self.criar_triangulo)
        self.zoomInButton.clicked.connect(self.zoom_in)
        self.zoomOutButton.clicked.connect(self.zoom_out)
        
    def inicia_eixo(self):
        reta_x = QtCore.QLineF(QtCore.QPointF(-500,0), QtCore.QPointF(500,0))
        self.scene.addLine(reta_x, self.pen)
        reta_y = QtCore.QLineF(QtCore.QPointF(0,-500), QtCore.QPointF(0, 500))
        self.scene.addLine(reta_y, self.pen)
        

    
    def criar_ponto(self):
        x = int(self.x_point.text())
        y = int(self.y_point.text()) * -1
        ponto = QtCore.QPointF(x, y)
        r = QtCore.QRectF(ponto, QtCore.QSizeF(5,5))
        self.scene.addRect(r, self.pen)

    def criar_linha(self):
        x1 = int(self.line_x1_point.text())
        y1 = int(self.line_y1_point.text()) * -1
        x2 = int(self.line_x2_point.text())
        y2 = int(self.line_y2_point.text()) * -1
        line = QtCore.QLineF(QtCore.QPointF(x1,y1), QtCore.QPointF(x2,y2))
        self.scene.addLine(line, self.pen)

    def criar_triangulo(self):
        x1 = int(self.triangle_x1_point.text())
        x2 = int(self.triangle_x2_point.text())
        x3 = int(self.triangle_x3_point.text())
        y1 = int(self.triangle_y1_point.text()) * -1
        y2 = int(self.triangle_y2_point.text()) * -1
        y3 = int(self.triangle_y3_point.text()) * -1
        triangle = QtGui.QPolygonF()
        triangle.append(QtCore.QPointF(x1,y1))
        triangle.append(QtCore.QPointF(x2,y2))
        triangle.append(QtCore.QPointF(x3,y3))
        self.scene.addPolygon(triangle, self.pen,self.brush)
    
    @QtCore.pyqtSlot()
    def zoom_in(self):
        print('zoom function')
        scale_tr = QtGui.QTransform()
        scale_tr.scale(1.5, 1.5)

        tr = self.graphics.transform() * scale_tr
        self.graphics.setTransform(tr)

    @QtCore.pyqtSlot()
    def zoom_out(self):
        scale_tr = QtGui.QTransform()
        scale_tr.scale(1.5, 1.5)

        scale_inverted, invertible = scale_tr.inverted()

        if invertible:
            tr = self.graphics.transform() * scale_inverted
            self.graphics.setTransform(tr)

    


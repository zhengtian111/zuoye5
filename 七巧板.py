import sys
from random import randint
from math import sqrt
from PIL import ImageGrab

from PyQt5 import uic
from PyQt5.QtCore import QPointF, Qt
from PyQt5.QtGui import QBrush, QPolygonF
from PyQt5.QtWidgets import QMainWindow, QGraphicsScene, QGraphicsPolygonItem, QGraphicsRectItem, QGraphicsItem, \
    QApplication

# pyinstaller -F -i D:/python_project/something_interesting/选修课/zuoye/zuoye5/myico.ico -w  七巧板.py

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('qqb.ui', self)
        self.scene = QGraphicsScene(0, 0, 400, 400)
        self.graphicsView.setScene(self.scene)
        self.init_shapes()
        self.Rotate1.clicked.connect(self.onRotate1)
        self.Rotate2.clicked.connect(self.onRotate2)
        self.Shuffle.clicked.connect(self.onShuffle)
        self.save.triggered.connect(self.screenshot)
        self.close1.triggered.connect(self.close)
        # self.MoveUp.clicked.connect(self.onMoveUp)
        # self.pushButtonMoveDown.clicked.connect(self.onMoveDown)

    def draw_polygon3(self, x1, y1, x2, y2, x3, y3, x, y, color=0):
        polygon3 = QGraphicsPolygonItem(QPolygonF([QPointF(x1, y1), QPointF(x2, y2), QPointF(x3, y3)]))
        if color == 1:
            polygon3.setBrush(QBrush(Qt.gray))
        elif color == 2:
            polygon3.setBrush(QBrush(Qt.green))
        else:
            polygon3.setBrush(QBrush(Qt.red))
        polygon3.setPos(x, y)
        polygon3.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.scene.addItem(polygon3)

    def draw_polygon4(self, x1, y1, x2, y2, x3, y3, x4, y4, x, y):
        polygon4 = QGraphicsPolygonItem(QPolygonF([QPointF(x1, y1), QPointF(x2, y2), QPointF(x3, y3), QPointF(x4, y4)]))
        polygon4.setBrush(QBrush(Qt.blue))
        polygon4.setPos(x, y)
        polygon4.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.scene.addItem(polygon4)

    def draw_rect(self, x1, y1, x2, y2, x, y):
        rect = QGraphicsRectItem(x1, y1, x2, y2)
        rect.setBrush(QBrush(Qt.yellow))
        rect.setPos(x, 200)
        rect.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
        self.scene.addItem(rect)

    # x:-300~500, y:-100~300
    def init_shapes(self):
        self.draw_polygon3(0, 0, 0, 200, 200, 200, randint(-300, 500), randint(-100, 300), 1)  # 三角形1
        self.draw_polygon3(0, 0, 0, 200, 200, 200, randint(-300, 500), randint(-100, 300))  # 三角形2
        self.draw_polygon3(0, 0, 0, 100 * sqrt(2), 100 * sqrt(2), 100 * sqrt(2), randint(-300, 500), randint(-100, 300),
                           2)  # 三角形3
        self.draw_polygon3(0, 0, 0, 100, 100, 100, randint(-300, 500), randint(-100, 300), 1)  # 三角形4
        self.draw_polygon3(0, 0, 0, 100, 100, 100, randint(-300, 500), randint(-100, 300))  # 三角形5
        self.draw_rect(0, 0, 100, 100, randint(-300, 500), randint(-100, 300))  # 矩形
        self.draw_polygon4(0, 0, 0, 100 * sqrt(2), 100 / sqrt(2), 100 * sqrt(2) * 3 / 2, 100 / sqrt(2), 100 / sqrt(2),
                           randint(-300, 500), randint(-100, 300))  # 平行四边形1

    def onRotate1(self, evt):
        items = self.scene.selectedItems()
        for item in items:
            item.setRotation(45 + item.rotation())

    def onRotate2(self, evt):
        items = self.scene.selectedItems()
        for item in items:
            item.setRotation(-45 + item.rotation())

    def onShuffle(self, evt):
        self.scene.clear()
        self.init_shapes()

    def screenshot(self):
        pic = ImageGrab.grab(bbox=(self.window().x(), self.window().y(),
                                   self.window().x() + self.window().width(),
                                   self.window().y() + self.window().height() + 30))
        pic.save("picture.jpg")

    def close(self):
        self.window().close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

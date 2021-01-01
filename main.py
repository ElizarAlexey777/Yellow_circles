import sys
from random import randint as r

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

SCREEN_SIZE = [500, 500]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('yellow_c.ui', self)
        self.do_paint = False
        self.initUI()

    def initUI(self):
        self.generate_circle_btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.gen_c(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def gen_c(self, qp):
        rand_size = r(10, 500)
        rand_p = [r(10, 480), r(10, 480)]

        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(rand_p[0], rand_p[1], rand_size, rand_size)
        self.do_paint = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
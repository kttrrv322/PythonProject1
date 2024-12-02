import sys
import random
import io
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPointF
from PyQt6.QtWidgets import QWidget, QApplication

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>729</width>
    <height>605</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QPushButton" name="pushButton">
   <property name="geometry">
    <rect>
     <x>310</x>
     <y>500</y>
     <width>93</width>
     <height>28</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)
        self.coords_ = []
        self.qp = QPainter()
        self.flag = False
        self.status = None
        self.pushButton.clicked.connect(self.mm)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        R = random.randint(20, 100)
        self.qp.setBrush(QColor(*[random.randint(0, 255) for _ in range(3)]))
        self.qp.drawEllipse(QPointF(self.coords_[0], self.coords_[1]), R, R)

    def initUI(self):
        design = io.StringIO(template)
        uic.loadUi(design, self)

    def mm(self):
        self.coords_ = [random.randint(1, 729), random.randint(1, 605)]
        self.drawf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
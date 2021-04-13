from __future__ import (absolute_import, division, print_function)
from qtpy import QtWidgets, QtCore, QtGui


class View(QtWidgets.QWidget):

    doSomethingSignal = QtCore.Signal()

    def __init__(self, parent=None):
        super(View, self).__init__(parent)

        self.button = QtWidgets.QPushButton('Hi', self)
        self.button.setStyleSheet("background-color:lightgrey")
        # connect button to signal
        self.button.clicked.connect(self.btn_click)

        self.label = QtWidgets.QLabel()
        self.label.setText("Button")

        # add widgets to layout
        self.sub_layout = QtWidgets.QHBoxLayout()
        self.sub_layout.addWidget(self.label)
        self.sub_layout.addWidget(self.button)

        grid = QtWidgets.QVBoxLayout(self)
        grid.addLayout(self.sub_layout)

        self.value = QtWidgets.QLineEdit()
        grid.addWidget(self.value)


        # set the layout for the view widget
        self.setLayout(grid)

    #send signals
    def btn_click(self):
        print ("hellow from view")
        self.doSomethingSignal.emit()

    def getValue(self):
        return float(self.value.text())
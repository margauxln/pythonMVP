from __future__ import (absolute_import,division,print_function)

from PyQt5 import QtWidgets

import sys
import view
import presenter
import model

"""
A wrapper class for setting the main window
"""
class Demo(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Demo,self).__init__(parent)

        self.window = QtWidgets.QMainWindow()
        my_view = view.View()
        data_model = model.DataGenerator()
        colour_list = data_model.line_colours()

        self.presenter = presenter.Presenter(my_view, data_model, colour_list)
        # set the view for the main window
        self.setCentralWidget(my_view)
        self.setWindowTitle("view tutorial")


def get_qapplication_instance():
    if QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication.instance()
    else:
        app = QtWidgets.QApplication(sys.argv)
    return app

app = get_qapplication_instance()
window = Demo()
window.show()
app.exec_()
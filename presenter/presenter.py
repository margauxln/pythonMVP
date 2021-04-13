from __future__ import (absolute_import, division, print_function)

class Presenter(object):

    # pass the view and model into the presenter
    def __init__(self, view):
        self.view = view

        self.view.doSomethingSignal.connect(self.handleButton)

    # handle signals
    def handleButton(self):
        value = self.view.getValue()
        print("Value is "+str(value))


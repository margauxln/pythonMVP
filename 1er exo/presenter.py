from __future__ import (absolute_import, division, print_function)

class Presenter(object):

    # pass the view and model into the presenter
    def __init__(self, view, data_model, colour_list):
        self.view = view
        self.data_model = data_model

        self.view.setColours(colour_list)
        # connect statements
        self.view.plotSignal.connect(self.updatePlot)

    # handle signals
    def updatePlot(self):
        freq = self.view.getFreq()
        color = self.view.getColor()
        phase = self.view.getPhase()
        grid = self.view.getGridLines()
        print("Freq is "+str(freq)+" "+str(color)+" "+str(phase)+" "+str(grid))


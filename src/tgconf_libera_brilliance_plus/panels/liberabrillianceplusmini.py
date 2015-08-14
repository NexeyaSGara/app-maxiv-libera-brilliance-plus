#!/usr/bin/env python

# Code implementation generated from reading ui file 'libera_brilliance_plus_mini.ui'
#
# Created: Wed Aug 12 11:40:33 2015 
#      by: Taurus UI code generator 3.3.0
#
# WARNING! All changes made in this file will be lost!

__docformat__ = 'restructuredtext'

import sys
import PyQt4.Qt as Qt
from PyQt4 import QtGui, QtCore
from ui_libera_brilliance_plus import Ui_LiberaBrilliancePlusMini
from taurus.qt.qtgui.panel import TaurusWidget
from PyQt4.Qwt5 import QwtPlot, QwtSymbol, QwtPlotMarker, QwtText
import PyTango
from taurus.qt.qtgui.plot.curvesAppearanceChooserDlg import CurveAppearanceProperties
from mytauruscurvedialog import myTaurusCurveDialog

class LiberaBrilliancePlusMini(TaurusWidget):
    l_plot = None
    trigger = QtCore.pyqtSignal()
    def __init__(self, parent=None, designMode=False):
        TaurusWidget.__init__(self, parent, designMode=designMode)
        
        self._ui = Ui_LiberaBrilliancePlusMini()
        self._ui.setupUi(self)

        self._ui.taurusCurveDialog = myTaurusCurveDialog(self)
        self._ui.taurusCurveDialog.setObjectName("taurusCurveDialog")
        self._ui.gridLayout.addWidget(self._ui.taurusCurveDialog, 0, 0, 1, 1)

        self.l_plot = self._ui.taurusCurveDialog.get_active_plot()
        self.sym = QwtSymbol(QwtSymbol.Ellipse, QtGui.QBrush(QtCore.Qt.blue), QtGui.QPen(QtCore.Qt.blue), QtCore.QSize(10, 10))
        self.sym_old = QwtSymbol(QwtSymbol.Ellipse, QtGui.QBrush(QtCore.Qt.gray), QtGui.QPen(QtCore.Qt.gray), QtCore.QSize(4, 4))
        self.l_plot.set_axis_limits('left', -0.003, 0.003)
        self.l_plot.set_axis_title('left', "Y")
        self.l_plot.set_axis_unit('left', "mm")
        self.l_plot.set_axis_limits('bottom', -0.003, 0.003)
        self.l_plot.set_axis_title('bottom', "X")
        self.l_plot.set_axis_unit('bottom', "mm")
        self.x = 0
        self.y = 0
        self.list_mark = []
        self.apply_color = True
        self.trigger.connect(self.update_plot)
        
    
    @classmethod
    def getQtDesignerPluginInfo(cls):
        ret = TaurusWidget.getQtDesignerPluginInfo()
        ret['module'] = 'liberabrillianceplusmini'
        ret['group'] = 'Taurus Display'
        ret['container'] = ':/designer/frame.png'
        ret['container'] = False
        return ret

    def setModel(self, models):
        from guiqwt.styles import style_generator        
        self._ui.taurusTrend.style = style_generator("brmgcykG")
        self._ui.taurusTrend.setModel(models[:2])
        index = models[0].rfind("/")
        self.model = models[0][:index]
        self.dev = PyTango.DeviceProxy(self.model)
        self.id1 = self.dev.subscribe_event('XPosSP', PyTango.EventType.CHANGE_EVENT, self.handle_x)
        self.id2 = self.dev.subscribe_event('YPosSP', PyTango.EventType.CHANGE_EVENT, self.handle_y)
        self._ui.taurusTrend_2.setModel(models[2])

    def handle_x(self, evt):
        if evt.attr_value is not None:
            if evt.attr_value.value != self.x:
	        self.x = evt.attr_value.value / 1e9

    def handle_y(self, evt):
        if evt.attr_value is not None:
            if evt.attr_value.value != self.y:
	        self.y = evt.attr_value.value / 1e9
                self.mark = QwtPlotMarker()
                self.mark.setSymbol(self.sym)
                self.mark.attach(self.l_plot)
	        self.mark.setValue(self.x, self.y)
                if len(self.list_mark) > 10:
                    self.list_mark[0].setVisible(False)
                    l_mark = self.list_mark[0]
                    self.list_mark.pop(0)
                for mark in self.list_mark:
                    mark.setSymbol(self.sym_old)
                self.list_mark.append(self.mark)
                self.trigger.emit()

    def update_plot(self):
        if self.l_plot is not None:
            self.l_plot.replot()
        
def main():
    app = Qt.QApplication(sys.argv)
    w = LiberaBrilliancePlusMini()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

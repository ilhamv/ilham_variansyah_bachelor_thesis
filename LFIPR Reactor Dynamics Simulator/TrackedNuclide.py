# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\TrackedNuclide.ui'
#
# Created: Sat May 05 08:25:33 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TrackedNuclide(object):
    def setupUi(self, TrackedNuclide):
        TrackedNuclide.setObjectName(_fromUtf8("TrackedNuclide"))
        TrackedNuclide.resize(640, 480)
        self.verticalLayout = QtGui.QVBoxLayout(TrackedNuclide)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.mplwidgetI = MatplotlibWidget(TrackedNuclide)
        self.mplwidgetI.setObjectName(_fromUtf8("mplwidgetI"))
        self.verticalLayout.addWidget(self.mplwidgetI)
        self.mplwidgetXe = MatplotlibWidget(TrackedNuclide)
        self.mplwidgetXe.setObjectName(_fromUtf8("mplwidgetXe"))
        self.verticalLayout.addWidget(self.mplwidgetXe)

        self.retranslateUi(TrackedNuclide)
        QtCore.QMetaObject.connectSlotsByName(TrackedNuclide)

    def retranslateUi(self, TrackedNuclide):
        TrackedNuclide.setWindowTitle(_translate("TrackedNuclide", "Konsentrasi Nuklida", None))

from matplotlibwidget import MatplotlibWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    TrackedNuclide = QtGui.QWidget()
    ui = Ui_TrackedNuclide()
    ui.setupUi(TrackedNuclide)
    TrackedNuclide.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\BeginningBurnup.ui'
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

class Ui_Awal(object):
    def setupUi(self, Awal):
        Awal.setObjectName(_fromUtf8("Awal"))
        Awal.resize(534, 158)
        self.gridLayout = QtGui.QGridLayout(Awal)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(Awal)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Castellar"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.splitter = QtGui.QSplitter(Awal)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.label = QtGui.QLabel(self.splitter)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBoxBU = QtGui.QComboBox(self.splitter)
        self.comboBoxBU.setObjectName(_fromUtf8("comboBoxBU"))
        self.comboBoxBU.addItem(_fromUtf8(""))
        self.comboBoxBU.addItem(_fromUtf8(""))
        self.comboBoxBU.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        self.pushButtonMulai = QtGui.QPushButton(Awal)
        self.pushButtonMulai.setObjectName(_fromUtf8("pushButtonMulai"))
        self.gridLayout.addWidget(self.pushButtonMulai, 2, 0, 1, 1)

        self.retranslateUi(Awal)
        QtCore.QMetaObject.connectSlotsByName(Awal)

    def retranslateUi(self, Awal):
        Awal.setWindowTitle(_translate("Awal", "Simulator LFIPR", None))
        self.label_3.setText(_translate("Awal", "Simulator Dinamika Reaktor Titik LFIPR", None))
        self.label.setText(_translate("Awal", "Burnup : ", None))
        self.comboBoxBU.setItemText(0, _translate("Awal", "0 MWd/ton (BOL)", None))
        self.comboBoxBU.setItemText(1, _translate("Awal", "20677,5 MWd/ton (MOL)", None))
        self.comboBoxBU.setItemText(2, _translate("Awal", "41355 MWd/ton (EOL)", None))
        self.pushButtonMulai.setText(_translate("Awal", "Mulai!!", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Awal = QtGui.QWidget()
    ui = Ui_Awal()
    ui.setupUi(Awal)
    Awal.show()
    sys.exit(app.exec_())


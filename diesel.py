# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diesel.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(484, 444)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 60, 450, 335))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_4.setFont(font)
        self.doubleSpinBox_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_4.setDecimals(4)
        self.doubleSpinBox_4.setMaximum(10000.0)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout.addWidget(self.doubleSpinBox_4, 1, 1, 1, 1)
        self.doubleSpinBox_9 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_9.setFont(font)
        self.doubleSpinBox_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_9.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_9.setDecimals(4)
        self.doubleSpinBox_9.setMinimum(-1000.0)
        self.doubleSpinBox_9.setMaximum(10000.0)
        self.doubleSpinBox_9.setObjectName("doubleSpinBox_9")
        self.gridLayout.addWidget(self.doubleSpinBox_9, 8, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.doubleSpinBox_11 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_11.setFont(font)
        self.doubleSpinBox_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_11.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_11.setDecimals(4)
        self.doubleSpinBox_11.setMinimum(-1000.0)
        self.doubleSpinBox_11.setMaximum(10000.0)
        self.doubleSpinBox_11.setObjectName("doubleSpinBox_11")
        self.gridLayout.addWidget(self.doubleSpinBox_11, 10, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.doubleSpinBox_10 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_10.setFont(font)
        self.doubleSpinBox_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_10.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_10.setDecimals(4)
        self.doubleSpinBox_10.setMinimum(-1000.0)
        self.doubleSpinBox_10.setMaximum(10000.0)
        self.doubleSpinBox_10.setObjectName("doubleSpinBox_10")
        self.gridLayout.addWidget(self.doubleSpinBox_10, 9, 1, 1, 1)
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_6.setFont(font)
        self.doubleSpinBox_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_6.setDecimals(4)
        self.doubleSpinBox_6.setMaximum(10000.0)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.gridLayout.addWidget(self.doubleSpinBox_6, 5, 1, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_3.setFont(font)
        self.doubleSpinBox_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_3.setDecimals(4)
        self.doubleSpinBox_3.setMaximum(10000.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout.addWidget(self.doubleSpinBox_3, 3, 1, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_5.setFont(font)
        self.doubleSpinBox_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_5.setDecimals(4)
        self.doubleSpinBox_5.setMaximum(10000.0)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout.addWidget(self.doubleSpinBox_5, 4, 1, 1, 1)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_7.setFont(font)
        self.doubleSpinBox_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_7.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_7.setDecimals(4)
        self.doubleSpinBox_7.setMaximum(10000.0)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.gridLayout.addWidget(self.doubleSpinBox_7, 6, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_8.setFont(font)
        self.doubleSpinBox_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_8.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox_8.setDecimals(4)
        self.doubleSpinBox_8.setMinimum(-1000.0)
        self.doubleSpinBox_8.setMaximum(10000.0)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.gridLayout.addWidget(self.doubleSpinBox_8, 7, 1, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.doubleSpinBox.setDecimals(4)
        self.doubleSpinBox.setMaximum(10000.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(20, 20, 451, 31))
        self.label_16.setStyleSheet("background-color: rgb(208, 208, 208);")
        self.label_16.setObjectName("label_16")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 410, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_11.setText(_translate("Dialog", "Average price of fuel(USD/gal)"))
        self.label_10.setText(_translate("Dialog", "Average price of oil(USD/gal)"))
        self.label_4.setText(_translate("Dialog", "Diesel efficiency(%)"))
        self.label_9.setText(_translate("Dialog", "Lifecycle(years)"))
        self.label_8.setText(_translate("Dialog", "Specific consumption of oil(gal/kWh)"))
        self.label_5.setText(_translate("Dialog", "Price per kWh generated(USD/kWh)"))
        self.label_2.setText(_translate("Dialog", "Price per kWh installed(USD/kW)"))
        self.label_7.setText(_translate("Dialog", "Specific consumption of fuel(gal/kWh)"))
        self.label_6.setText(_translate("Dialog", "Factor of the initial capital cost invested(%)"))
        self.label_3.setText(_translate("Dialog", "Minimum ratio allowed"))
        self.label_16.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">Parameters Diesel Generator</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

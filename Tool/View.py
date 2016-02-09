# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
#
# Created: Sun Jan 17 21:06:35 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.setEnabled(True)
        Widget.resize(700, 427)
        Widget.setMinimumSize(QtCore.QSize(700, 427))
        Widget.setMaximumSize(QtCore.QSize(700, 427))
        self.textEdit = QtGui.QTextEdit(Widget)
        self.textEdit.setGeometry(QtCore.QRect(30, 30, 521, 51))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtGui.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(580, 30, 91, 51))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtGui.QTextBrowser(Widget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 130, 641, 281))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtGui.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(30, 90, 680, 21))
        self.label.setObjectName("label")
        self.label.setText(QtGui.QApplication.translate("Widget", " ", None, QtGui.QApplication.UnicodeUTF8))
        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QtGui.QApplication.translate("Widget", "CSV-Reader", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Widget", "Ok", None, QtGui.QApplication.UnicodeUTF8))




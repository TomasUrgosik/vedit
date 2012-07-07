# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editview.ui'
#
# Created: Sat Jul  7 11:05:09 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_EditView(object):
    def setupUi(self, EditView):
        EditView.setObjectName("EditView")
        EditView.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(EditView)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtGui.QTextEdit(EditView)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)

        self.retranslateUi(EditView)
        QtCore.QMetaObject.connectSlotsByName(EditView)

    def retranslateUi(self, EditView):
        EditView.setWindowTitle(QtGui.QApplication.translate("EditView", "Form", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    EditView = QtGui.QWidget()
    ui = Ui_EditView()
    ui.setupUi(EditView)
    EditView.show()
    sys.exit(app.exec_())


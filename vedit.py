#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
from PySide.QtGui import QFileDialog, QMainWindow, QApplication, QWidget
from PySide import QtCore
from mainwindow import Ui_MainWindow
from editview import Ui_EditView

class EditView(QWidget, Ui_EditView):
    def __init__(self, parent=None):
        super(EditView, self).__init__(parent)
        self.setupUi(self)
        self.saved = None

    def setPath(self, path):
        self.path = path
    
    def getPath(self):
        return self.path

    def setSaved(self, saved):
        self.saved = saved

    def getSaved(self):
        return self.saved


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.tab_list = {}
        self.actionNew.triggered.connect(self.addTab)
        self.actionSave_As.triggered.connect(self.saveActiveTabAs)

    def addTab(self):
        view = EditView()
        x = self.tabWidget.addTab(view, u"")
        self.tabWidget.setTabText(x, unicode(x))
        #print(self.tabWidget.count())

    def closeTab(i):
        pass
    def saveActiveTabAs(self):
        view = self.tabWidget.currentWidget()
        filename = QFileDialog.getSaveFileName(self)[0]
        if filename is not u'':
            f = codecs.open(filename, 'w', 'utf-8')
            f.write(view.textEdit.toPlainText())
            f.close()
            print  self.tabWidget.currentWidget().getSaved()
            if self.tabWidget.currentWidget().getSaved() == True:
                print 'Alredy Saved'
            else:
                self.tabWidget.currentWidget().setSaved(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

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
        self.path = None

    def setPath(self, path):
        self.path = path
    
    def getPath(self):
        return self.path

    def setSaved(self, saved):
        self.saved = saved

    def getSaved(self):
        return self.saved
    
    def save(self):
        try:
            f = codecs.open(self.getPath(), 'w', 'utf-8')
            f.write(self.textEdit.toPlainText())
            self.setSaved(True)
            f.close()
        except IOError as e:
            self.saveAs()
    
    def saveAs(self):
        self.setPath(QFileDialog.getSaveFileName(self)[0])
        if self.getPath() is not u'':
            self.save()
    
    def open(self):
        self.setPath(QFileDialog.getOpenFileName(self)[0])
        f = codecs.open(self.getPath(), 'r', 'utf-8')
        self.textEdit.setPlainText(f.read())
        f.close
    
    def openTab(self): #TODO
        pass

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.addTab()
        self.actionNew.triggered.connect(self.addTab)
        self.actionSave_As.triggered.connect(self.saveAs)
        self.actionSave.triggered.connect(self.save)
        self.actionOpen.triggered.connect(self.open)
        self.actionOpen_Tab.triggered.connect(self.openTab)

    def addTab(self):
        view = EditView()
        x = self.tabWidget.addTab(view, u"")
        self.tabWidget.setTabText(x, unicode(x))
        return view
       
    def save(self):
        self.tabWidget.currentWidget().save()

    def saveAs(self):
        self.tabWidget.currentWidget().saveAs()

    def open(self):
        self.tabWidget.currentWidget().open()

    def openTab(self):
        pass #TODO

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

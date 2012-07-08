#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import codecs
from PySide.QtGui import QFileDialog, QMainWindow, QApplication, QWidget, QMessageBox
from PySide import QtCore
from mainwindow import Ui_MainWindow
from editview import Ui_EditView

class EditView(QWidget, Ui_EditView):
    def __init__(self, parent=None):
        super(EditView, self).__init__(parent)
        self.setupUi(self)
        self.saved = None
        self.path = None
        self.index = None
        self.actionText_Changed.triggered.connect(self.textChanged)


    def textChanged(self):
        self.setSaved(False)
    
    def setIndex(self, index):
        self.index = index

    def getIndex(self):
        return self.index

    def setPath(self, path):
        self.path = path
    
    def getTabName(self):
        try:
            if self.getSaved() is False:
                return self.getPath().split('/')[-1] + ' *'
            else:
                return self.getPath().split('/')[-1]
        except AttributeError:
            return u'Empty'

    def getPath(self):
        return self.path

    def setSaved(self, saved): 
        self.saved = saved
        window.updateTabName(self)

    def getSaved(self):
        return self.saved
    
    def save(self):
        try:
            f = codecs.open(self.getPath(), 'w', 'utf-8')
            f.write(self.textEdit.toPlainText())
            self.setSaved(True)
            f.close()
        except (IOError, TypeError):
            self.saveAs()
    
    def saveAs(self):
        self.setPath(QFileDialog.getSaveFileName(self)[0])
        if self.getPath() is not u'':
            self.save()
        else:
            self.setSaved(False)
    
    def open(self):
        try:
            self.setPath(QFileDialog.getOpenFileName(self)[0])
            f = codecs.open(self.getPath(), 'r', 'utf-8')
            self.textEdit.setPlainText(f.read())
            self.setSaved(True)
            f.close
        except IOError:
            self.setPath(None)
    
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
        self.actionClose_Tab.triggered.connect(self.closeTab)

    def addTab(self):
        view = EditView()
        view.setIndex(self.tabWidget.addTab(view, u""))
        self.tabWidget.setTabText(view.getIndex(), view.getTabName())
        return view
       
    def save(self):
        self.tabWidget.currentWidget().save()

    def saveAs(self):
        self.tabWidget.currentWidget().saveAs()
        self.updateTabName(self.tabWidget.currentWidget())
    def open(self):
        self.tabWidget.currentWidget().open()
        self.updateTabName(self.tabWidget.currentWidget())
    
    def openTab(self):
        self.addTab().open()

    def closeTab(self):
        if self.tabWidget.currentWidget().getSaved() is True:
            self.tabWidget.removeTab(self.tabWidget.currentWidget().getIndex())
        else:
            confirmBox = QMessageBox()
            confirmBox.setText('The document has been modified.')
            confirmBox.setInformativeText('Do you want to save your changes?')
            confirmBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            confirmBox.setDefaultButton(QMessageBox.Save)
            confirm = confirmBox.exec_()
            if confirm == QMessageBox.Save:
                self.tabWidget.currentWidget().save()
                self.closeTab()
            elif confirm == QMessageBox.Discard:
                self.tabWidget.removeTab(self.tabWidget.currentWidget().getIndex())
            elif confirm == QMessageBox.Cancel:
                pass
            else:
                raise ValueError(confirm)
    
    def updateTabName(self, tab):
        self.tabWidget.setTabText(self.tabWidget.indexOf(tab), self.tabWidget.currentWidget().getTabName())

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

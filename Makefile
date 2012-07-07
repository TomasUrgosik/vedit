all: gui
	python vedit.py

gui:
	pyside-uic -x mainwindow.ui > mainwindow.py
	pyside-uic -x editview.ui > editview.py

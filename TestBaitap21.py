from PyQt6.QtWidgets import QApplication, QMainWindow

from Chuong1_Ham.baitap21.ui.MainWindow21Ext import MainWindow21Ext

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindow21Ext()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()

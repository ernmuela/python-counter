import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QTableWidget,QTableWidgetItem,QPushButton
from PyQt5           import uic
from PyQt5.QtCore    import *
from PyQt5.QtGui     import *
from time            import sleep

class ContadorRFID(QDialog): 

 def __init__(self):
  QDialog.__init__(self)
  self.resize(300, 300)
  self.setWindowTitle("RFID")
  self.etiqueta = QLabel(self)
  uic.loadUi("ContadorRFID.ui",self)

 def Cuenta(self,sample_count):
  self.tableWidget.setRowCount(len(sample_count))
  self.tableWidget.setColumnCount(len(sample_count[0]))
  for row in range(0,len(sample_count)):
    sleep(2)
    for col in range(0,len(sample_count[row])):
      self.tableWidget.setItem(row,col,QTableWidgetItem(sample_count[row][col]))
   
app          = QApplication(sys.argv)
sample_count = [["959",5],["991",2],["9005",4]]
dialogo      = ContadorRFID()
dialogo.show()
dialogo.Cuenta(sample_count)
# Run the main Qt loop
sys.exit(app.exec_())




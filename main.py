#!"C:\Program Files\Python 3.7\python.exe"
# -*- coding: utf-8 -*-
#@author: Quiñones Carhuaz Liam

import pyautogui as pag
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from ventana import Ui_MainWindow
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # establecer ancho y altura fijos
        tamano = pag.size()
        self.setFixedWidth(250) 
        self.setFixedHeight(80)
        resolution = f"{tamano[0],tamano[1]}"
        new_resolution = ""    
        for k in resolution:
            if k not in ("(",")"):
                new_resolution += k
        self.ui.label_content_resolucion.setText(new_resolution)
           
    def actualizar(self):
        # obtener posicion actual y mostrarlo en pantalla
        pos = pag.position()
        cord_x = str(pos[0])
        cord_y = str(pos[1]) 
        self.ui.label_contentx.setText(cord_x)
        self.ui.label_contenty.setText(cord_y)    

app = QtWidgets.QApplication([])
application = mywindow()
# establecer el timer y actualizar los datos
timer = QTimer()
timer.timeout.connect(application.actualizar)
timer.setInterval(100)
timer.start()

application.show()
sys.exit(app.exec())
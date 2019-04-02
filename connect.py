#!/usr/bin/python3

#un bouton, dont le signal clicked est connecté à une fonction. simple, efficace.

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

@pyqtSlot()
def on_click():
	print('PyQt5 button click') 
 
my_app = QApplication(sys.argv)


bouton = QPushButton("clique... monique!")
bouton.clicked.connect(on_click)
bouton.show()

sys.exit(my_app.exec_())
 
 

	

from PyQt5 import QtGui,QtWidgets

import sys

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()

window.show()
window.setGeometry(50,50,500,300)
window.setWindowTitle("ClipBoard")
sys.exit(app.exec_())

from PyQt5 import QtGui,QtWidgets,QtCore
import sys

class Gui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("ClipBoard!")
        #self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))

        self.setWindowIcon(QtGui.QIcon("AppIcon29x29.png"))

        extractAction = QtWidgets.QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()
        self.home()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
    def home(self):
        btn = QtWidgets.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,0)
        self.show()
    def close_application(self):

        print("whooaaaa so custom!!!")
        sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    GUI = Gui()
    sys.exit(app.exec_())

from PyQt5.QtWidgets import *
from AppKit import NSPasteboard, NSArray,NSStringPboardType
import sys

class Gui(QMainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("ClipBoard!")

        self._main = QWidget()
        self.setCentralWidget(self._main)
        self.Layout = QVBoxLayout(self._main)
        self.createLabelsForClipBoardContents()
        extractAction = QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)
        QAction("FFA",self)
        self.statusBar()
        self.home()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)
    def createLabelsForClipBoardContents(self):
        horizontalLayout = QHBoxLayout()

        timeLabel = QLabel("time")
        pb = NSPasteboard.generalPasteboard()
        textInClipBoard = pb.stringForType_(NSStringPboardType)
        textInClipBoardLabel = QLabel(textInClipBoard)
        horizontalLayout.addWidget(timeLabel)
        horizontalLayout.addWidget(textInClipBoardLabel)
        self.Layout.addLayout(horizontalLayout)
    def home(self):
        btn = QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(400,300)
        self.show()

    def close_application(self):

        print("whooaaaa so custom!!!")
        sys.exit()


if __name__ == "__main__":
    qapp = QApplication(sys.argv)
    app = Gui()
    app.show()
    sys.exit(qapp.exec_())

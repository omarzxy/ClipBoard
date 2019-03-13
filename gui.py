from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from AppKit import NSPasteboard, NSArray,NSStringPboardType
import sys
from datetime import datetime

class Gui(QMainWindow):
    def __init__(self):
        super(Gui, self).__init__()
        self.setGeometry(50, 50, 700, 500)
        self.setWindowTitle("ClipBoard")
        self.setStyleSheet("font-family: Avenir Next;")
        self._main = QWidget()
        self.setCentralWidget(self._main)
        self.Layout = QVBoxLayout(self._main)
        self.createMenu()
        self.createLabelsForClipBoardContents()
        self.createLabelsForClipBoardContents()


    def createMenu(self):
        """
        Creates a menuBar and sets the color of the menuBar
        """
        extractAction = QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)
        mainMenu = self.menuBar()
        mainMenu.setStyleSheet("background-color:#98B7DA;")
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        convertMenu = mainMenu.addMenu('Convert')
        syncMenu = mainMenu.addMenu('sync')
        fileMenu.addAction(extractAction)
        mainMenu.setNativeMenuBar(False)
    def createLabelsForClipBoardContents(self):
        dateAndTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        horizontalLayout = QHBoxLayout()

        timeLabel = QLabel(dateAndTime)
        timeLabel.setMinimumWidth(80)
        timeLabel.setMaximumHeight(50)
        timeLabel.setAlignment(Qt.AlignCenter)
        timeLabel.setStyleSheet("background-color:#4A90E2;"
                                " border: 1px;"
                                "border-radius:3px;"
                                "border-color:black;"
                                "border-style:solid;")
        pb = NSPasteboard.generalPasteboard()
        textInClipBoard = pb.stringForType_(NSStringPboardType)
        print(type(textInClipBoard))
        textInClipBoardLabel = QTextEdit(textInClipBoard)
        textInClipBoardLabel.setStyleSheet("background-color:#FFFFFF;")
        horizontalLayout.addWidget(timeLabel)
        horizontalLayout.addWidget(textInClipBoardLabel)
        self.Layout.addLayout(horizontalLayout)
    def close_application(self):
        pass


def setCustomSize(x, width, height):
    '''
    setCustomSize is a function used repeatly to set a Fixed size for each
    Widget. We use this method as a quick fix because otherwise the widgets will fill
    to expand the remaining area in the layout.Each widget that uses setCustomSize will
    never adjust its size when the main window decreases in size this is a bug and
    will need to be fixed.
    '''

    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(x.sizePolicy().hasHeightForWidth())
    x.setSizePolicy(sizePolicy)
    x.setMinimumSize(QtCore.QSize(width, height))
    x.setMaximumSize(QtCore.QSize(width, height))

if __name__ == "__main__":
    qapp = QApplication(sys.argv)
    app = Gui()
    qapp.setStyle('Fusion')
    app.show()
    sys.exit(qapp.exec_())

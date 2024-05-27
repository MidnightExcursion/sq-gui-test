# Native Package | sys
import sys

# External Packages | PyQt5
from PyQt5.QtWidgets import QMainWindow,QApplication, QTabWidget

from app.tabs.central_tab import CentralTab

from app.static.constants import _APPLICATION_NAME, _WINDOW_MAIN_APP_WIDTH, _WINDOW_MAIN_APP_HEIGHT

class App(QMainWindow):

    def __init__(self):
        
        super().__init__()
        

        # Set the name of the application:
        self.title = _APPLICATION_NAME
        self.setWindowTitle(self.title)

        # Configure the geometry of the application window:
        self.window_left = 0
        self.window_top = 0
        self.window_width = _WINDOW_MAIN_APP_WIDTH
        self.window_height = _WINDOW_MAIN_APP_HEIGHT
        self.setGeometry(self.window_left, self.window_top, self.window_width, self.window_height)

        # Initalize additional UI:
        self.initializeUI()

    def initializeUI(self):

        # Initialize PyQT's "central widget"
        self.central_widget = QTabWidget()
        self.setCentralWidget(self.central_widget)

        # Initialize the central widget's tabs:
        self.tab1 = CentralTab()

        # Add the tab to the central widget
        self.central_widget.addTab(self.tab1, "Main Display")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()

    # window2 = StripChartWindow()
    # window2.show()
    sys.exit(app.exec_())

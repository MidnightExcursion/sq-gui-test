# External Packages | PyQTt5
from PyQt5.QtWidgets import QWidget, QGridLayout, QFrame, QVBoxLayout, QLabel, QTextEdit

class LoggingTab(QTextEdit):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):
        
        layout = QGridLayout()

        # Section 1
        section1 = QFrame()
        section1_layout = QVBoxLayout()
        section1_layout.addWidget(QLabel("Logging"))
        section1_layout.addWidget(QTextEdit())
        section1.setLayout(section1_layout)

        layout.addWidget(section1, 0, 0)  # Row 0, Column 0

        self.setLayout(layout)

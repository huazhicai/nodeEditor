from PyQt5.QtWidgets import *


class QDMNodeContentWidget(QWidget):
    def __init__(self, node, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)  # 内容盒子距外边框
        self.setLayout(self.layout)

        self.wdg_lable = QLabel("Some Title")
        self.layout.addWidget(self.wdg_lable)
        self.layout.addWidget(QTextEdit("foo"))

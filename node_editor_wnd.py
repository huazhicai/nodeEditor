import os

from PyQt5.QtCore import Qt, QFile
from PyQt5.QtGui import QBrush, QPen, QFont, QColor
from PyQt5.QtWidgets import *

from node_graphics_view import QDMGraphicsView
from node_node import Node
from node_scene import Scene


class NodeEditorWnd(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.stylesheet_filename = current_dir + '/qss/nodestyle.qss'
        self.loadStylesheet(self.stylesheet_filename)
        # 控件设置
        self.initUI()

    def initUI(self):
        # 设置窗口几何位置、大小， 屏幕左上角为坐标原点
        self.setGeometry(0, 100, 900, 800)

        # 布局设置
        self.layout = QVBoxLayout()
        # 设置左侧、顶部、右侧和底部边距，以便在布局周围使用。
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)  # 加载设置参数

        # 在视图场景中事件传递是View->Scene->Item这样的顺序
        # create graphics scene场景
        self.scene = Scene()
        # self.grScene = self.scene.grScene

        node = Node(self.scene)

        # create graphics view 创建图形视图
        # The QGraphicsView class provides a widget
        # for displaying the contents of a QGraphicsScene
        # graphicsView->setSceneRect(10,10,100,100)
        self.view = QDMGraphicsView(self.scene.grScene, self)
        self.layout.addWidget(self.view)

        self.setWindowTitle("Node Editor")
        # self.show()

        self.addDebugContent()

    def addDebugContent(self):
        greenBrush = QBrush(Qt.green)
        outlinePen = QPen(Qt.darkYellow)
        outlinePen.setWidth(2)

        # 场景中心为原点，左和上为负坐标，控件左上角我左边参考点
        rect = self.scene.grScene.addRect(-100, -100, 80, 100, outlinePen, greenBrush)
        rect.setFlag(QGraphicsItem.ItemIsMovable)

        # 没写坐标默认在场景坐标系原点
        text = self.scene.grScene.addText("This is my Awesome text!", QFont("Ubuntu"))
        text.setFlag(QGraphicsItem.ItemIsSelectable)
        text.setFlag(QGraphicsItem.ItemIsMovable)
        text.setDefaultTextColor(QColor.fromRgbF(1.0, 1.0, 1.0))

        # 添加控件
        widget1 = QPushButton("Hello World")
        proxy1 = self.scene.grScene.addWidget(widget1)
        proxy1.setFlag(QGraphicsItem.ItemIsMovable)
        proxy1.setPos(0, 30)

        widget2 = QTextEdit()
        proxy2 = self.scene.grScene.addWidget(widget2)
        proxy2.setFlag(QGraphicsItem.ItemIsSelectable)
        proxy2.setPos(0, 60)

        # 场景坐标系中，直线从左到又两个点的坐标
        line = self.scene.grScene.addLine(-200, -200, 400, -100, outlinePen)
        line.setFlag(QGraphicsItem.ItemIsMovable)
        line.setFlag(QGraphicsItem.ItemIsSelectable)

    def loadStylesheet(self, filename):
        print("STYLE loading:", filename)
        file = QFile(filename)
        file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = file.readAll()
        # qApp = QApplication.instance()
        QApplication.instance().setStyleSheet(str(stylesheet, encoding='utf-8'))

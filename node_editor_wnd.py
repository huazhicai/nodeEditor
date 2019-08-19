from PyQt5.QtWidgets import *

from node_graphics_scene import QDMGraphicsScene


class NodeEditorWnd(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 控件设置
        self.initUI()

    def initUI(self):
        # 设置窗口几何位置、大小
        self.setGeometry(200, 200, 800, 600)

        # 布局设置
        self.layout = QVBoxLayout()
        # 设置左侧、顶部、右侧和底部边距，以便在布局周围使用。
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)  # 加载设置参数

        # 在视图场景中事件传递是View->Scene->Item这样的顺序
        # create graphics scene场景
        self.grScene = QDMGraphicsScene()

        # create graphics view 创建图形视图
        # The QGraphicsView class provides a widget
        # for displaying the contents of a QGraphicsScene
        # graphicsView->setSceneRect(10,10,100,100)
        self.view = QGraphicsView(self)
        self.view.setScene(self.grScene)  # 视图加载场景
        self.layout.addWidget(self.view)

        self.setWindowTitle("Node Editor")
        self.show()

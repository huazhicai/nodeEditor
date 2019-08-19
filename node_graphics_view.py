from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QGraphicsView


class QDMGraphicsView(QGraphicsView):
    def __init__(self, grScene, parent=None):
        super().__init__(parent)
        self.grScene = grScene

        self.initUI()

        self.setScene(self.grScene)

    def initUI(self):
        # 消除圆形图片锯齿问题 后面使用drawPixmap绘图。
        self.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing | QPainter.TextAntialiasing | QPainter.SmoothPixmapTransform)
        # 视口更新模式：刷新界面
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        # self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)   # 隐藏滚动条
        # self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

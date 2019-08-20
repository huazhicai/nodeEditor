from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QDMGraphicsNode(QGraphicsItem):
    """图形节点项目"""

    def __init__(self, node, title="Node Graphics Item", parent=None):
        super().__init__(parent)

        self._title_color = Qt.yellow
        self._title_font = QFont("Ubuntu", 10)

        self.width = 180  # 盒子尺寸
        self.height = 240
        self.edge_size = 10.0  # 边缘转角半径尺寸，小于等于title_height
        self.title_height = 24.0  # 标题区高度
        self._padding = 10.0  # 盒子边与盒子内部元素的距离

        self._pen_default = QPen(QColor("#7F000000"))
        # 被选择后外边框线的颜色
        self._pen_selected = QPen(QColor("#FFFFA637"))

        # 标题区颜色背景刷
        self._brush_title = QBrush(QColor("#FF313131"))
        self._brush_background = QBrush(QColor("#E3212121"))

        self.initTitle()
        self.title = title

        self.initUI()

    def boundingRect(self):
        """
        QRectF 构造矩形， 矩形左上右下角坐标（0，0）矩形长宽（），
        鼠标点击此区域能够选择矩形节点图
        """
        return QRectF(
            0,
            0,
            self.height,
            self.height
        ).normalized()

    def initUI(self):
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)

    def initTitle(self):
        self.title_item = QGraphicsTextItem(self)
        self.title_item.setDefaultTextColor(self._title_color)
        self.title_item.setFont(self._title_font)
        self.title_item.setPos(self._padding, 0)  # x方向的距内边宽
        self.title_item.setTextWidth(
            # 设置文本宽度，超过宽度就换行，2padding，充满后就正好居中
            self.width - 2 * self._padding
        )

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self.title_item.setPlainText(self._title)  # 纯文本

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        """"动词画，paint谓词做为方法命名，把节点图形描画出在场景中"""
        # title
        # QPainterPath 类（绘图路径）提供了一个容器，用于绘图操作，可以创建和重用图形形状。
        path_title = QPainterPath()
        # 非零弯曲规则, 只填充图形内的点
        path_title.setFillRule(Qt.WindingFill)
        # 绘制圆角矩形
        path_title.addRoundedRect(0, 0, self.width, self.title_height, self.edge_size, self.edge_size)
        # 因为画了四个圆角，需要把下面两个圆角回填回来
        path_title.addRect(0, self.title_height - self.edge_size, self.edge_size, self.edge_size)
        path_title.addRect(self.width - self.edge_size, self.title_height - self.edge_size, self.edge_size,
                           self.edge_size)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_title)
        painter.drawPath(path_title.simplified())

        # content
        path_content = QPainterPath()
        path_content.setFillRule(Qt.WindingFill)
        path_content.addRoundedRect(0, self.title_height, self.width, self.height - self.title_height, self.edge_size,
                                    self.edge_size)
        path_content.addRect(0, self.title_height, self.edge_size, self.edge_size)
        path_content.addRect(self.width - self.edge_size, self.title_height, self.edge_size, self.edge_size)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_background)
        painter.drawPath(path_content.simplified())

        # outline
        path_outline = QPainterPath()
        # 画圆角矩形
        path_outline.addRoundedRect(0, 0, self.width, self.height, self.edge_size, self.edge_size)
        painter.setPen(self._pen_default if not self.isSelected() else self._pen_selected)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path_outline.simplified())

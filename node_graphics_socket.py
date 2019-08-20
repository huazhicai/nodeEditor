from PyQt5.QtCore import QRectF
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class QDMGraphicsSocket(QGraphicsItem):
    """绘制接口"""
    def __init__(self, parent=None):
        super().__init__(parent)

        self.radius = 6.0
        self.outline_width = 1.0
        self._color_background = QColor("#FFFF7700")
        self._color_outline = QColor("#FF000000")

        self._pen = QPen(self._color_outline)
        self._pen.setWidthF(self.outline_width)
        self._brush = QBrush(self._color_background)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        # painting circle
        painter.setBrush(self._brush)
        painter.setPen(self._pen)
        painter.drawEllipse(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius)

    def boundingRect(self):
        """限制绘图的边界 所有的绘图都必须在这个区域的内部，这个区域是矩形的"""
        return QRectF(
            -self.radius - self.outline_width,
            -self.radius - self.outline_width,
            2 * (self.radius + self.outline_width),
            2 * (self.radius + self.outline_width)
        )
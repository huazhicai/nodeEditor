import math

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QDMGraphicsScene(QGraphicsScene):
    """图形场景绘制"""
    def __init__(self, scene, parent=None):
        super().__init__(parent)

        # 控件设置
        self.gridSize = 20  # 栅格栏距离
        self.gridSquares = 5  # 网格方块个数6*6

        self._color_background = QColor("#393939")
        self._color_light = QColor("#2f2f2f")
        self._color_dark = QColor("#292929")

        # 亮光笔，用亮色, 宽度设置为1
        self._pen_light = QPen(self._color_light)
        self._pen_light.setWidth(1)
        self._pen_dark = QPen(self._color_dark)
        self._pen_dark.setWidth(2)


        self.setBackgroundBrush(self._color_background)  # 刷背景色

    def setGrScene(self, width, height):
        """设置图形场景矩形框的相对视图位置和尺寸"""
        self.setSceneRect(-width // 2, -height // 2, width, height)

    def drawBackground(self, painter, rect):
        """
        绘画者绘制矩形栅格背景
        """
        super().drawBackground(painter, rect)

        # create grid创建网格, 数据往大了取
        left = int(math.floor(rect.left()))     # -399 有一个像素的边框
        right = int(math.ceil(rect.right()))    # 399
        top = int(math.floor(rect.top()))       # -299
        bottom = int(math.ceil(rect.bottom()))  # 299
        # 负数取模：-1%3=2
        first_left = left - (left % self.gridSize)  # -400
        first_top = top - (top % self.gridSize)     # -300

        # compute all lines to be drawn， 第一条线画到边框上去
        lines_light, lines_dark = [], []
        for x in range(first_left, right, self.gridSize):
            if x % (self.gridSize * self.gridSquares) != 0:
                lines_light.append(QLine(x, top, x, bottom))
            else:
                lines_dark.append(QLine(x, top, x, bottom))

        for y in range(first_top, bottom, self.gridSize):
            if y % (self.gridSquares*self.gridSize) != 0:
                lines_light.append(QLine(left, y, right, y))
            else:
                lines_dark.append(QLine(left, y, right, y))

        # draw the lines
        painter.setPen(self._pen_light)
        painter.drawLines(*lines_light)

        painter.setPen(self._pen_dark)
        painter.drawLines(*lines_dark)

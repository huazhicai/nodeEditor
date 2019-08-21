from node_graphics_node import QDMGraphicsNode
from node_content_widget import QDMNodeContentWidget
from node_socket import *


class Node(object):
    """节点作为QgraphicsItem,需通过场景来展示"""

    def __init__(self, scene, title="Undefined Node", inputs=[], outputs=[]):
        self.scene = scene
        self.title = title

        # 节点内容控件，在节点上，先完成内容控件，再用于节点图绘制
        self.content = QDMNodeContentWidget(self)
        # 图形节点对象
        self.grNode = QDMGraphicsNode(self)



        self.scene.addNode(self)  # 节点加入场景中
        self.scene.grScene.addItem(self.grNode)  # 在图形场景中加入图形节点项目

        self.socket_spacing = 22

        # create socket for inputs and outputs
        self.inputs = []
        self.outputs = []
        counter = 0
        for item in inputs:
            socket = Socket(node=self, index=counter, position=LEFT_BOTTOM, socket_type=item)
            counter += 1
            self.inputs.append(socket)

        counter = 0
        for item in outputs:
            socket = Socket(node=self, index=counter, position=LEFT_TOP, socket_type=item)
            counter += 1
            self.outputs.append(socket)

    @property
    def pos(self):
        return self.grNode.pos()  # QPointF

    def setPos(self, x, y):
        self.grNode.setPos(x, y)

    def getSocketPosition(self, index, position):
        x = 0 if (position in (LEFT_TOP, LEFT_BOTTOM)) else self.grNode.width

        if position in (LEFT_BOTTOM, RIGHT_BOTTOM):
            # start from bottom
            y = self.grNode.height - self.grNode.edge_size - self.grNode._padding - index * self.socket_spacing
        else:
            # start from top
            y = self.grNode.title_height + self.grNode._padding + self.grNode.edge_size + index * self.socket_spacing

        return [x, y]

    def updateConnectedEdges(self):
        for socket in self.inputs + self.outputs:
            if socket.hasEdge():
                socket.edge.updatePositions()

from node_graphics_node import QDMGraphicsNode
from node_content_widget import QDMNodeContentWidget


class Node(object):
    """节点作为QgraphicsItem,需通过场景来展示"""
    def __init__(self, scene, title="Undefined Node"):
        self.scene = scene
        self.title = title

        self.content = QDMNodeContentWidget()
        self.grNode = QDMGraphicsNode(self)

        self.scene.addNode(self)  # 节点加入场景中
        self.scene.grScene.addItem(self.grNode)  # 在图形场景中加入图形节点项目

        self.inputs = []
        self.outputs = []

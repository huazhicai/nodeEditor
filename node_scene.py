from node_graphics_scene import QDMGraphicsScene


class Scene(object):
    """基础场景"""
    def __init__(self):
        self.nodes = []  # 场景中的节点容器，用来接收节点
        self.edges = []  # 场景中的边缘容器，用来接收边缘

        self.scene_width = 6400
        self.scene_height = 6400

        self.initUI()

    def initUI(self):
        self.grScene = QDMGraphicsScene(self)
        self.grScene.setGrScene(self.scene_width, self.scene_height)

    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, edge):
        self.edges.append(edge)

    def removeNode(self, node):
        self.nodes.remove(node)

    def removeEdge(self, edge):
        self.edges.remove(edge)

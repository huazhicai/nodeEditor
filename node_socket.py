from node_graphics_socket import QDMGraphicsSocket

LEFT_TOP = 1
LEFT_BOTTOM = 2
RIGHT_TOP = 3
RIGHT_BOTTOM = 4


class Socket:
    def __init__(self, node, index, position=LEFT_TOP):

        self.node = node
        self.index = index
        self.position = LEFT_TOP

        # 绘制图形插座， 是在绘制好的图形节点上绘制插座，所以要传入绘制好的图形节点作为参数
        self.grSocket = QDMGraphicsSocket(self.node.grNode)
        # self.grSocket 对象会到其父类中寻找setPos方法，实现位置设置
        self.grSocket.setPos(*self.node.getSocketPosition(index, position))

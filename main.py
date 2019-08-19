import sys
from PyQt5.QtWidgets import *

from node_editor_wnd import NodeEditorWnd

if __name__ == '__main__':
    # 1. 创建一个应用程序对象,传入参数列表
    app = QApplication(sys.argv)

    # 2. 控件的操作
    # 2.1 创建控件
    wnd = NodeEditorWnd()

    # 2.3 展示控件
    wnd.show()
    # 3. 应用程序的执行, 进入到消息循环
    sys.exit(app.exec_())

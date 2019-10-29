import os
import sys

from PyQt5.QtWidgets import QApplication

from editor.editor_window import NodeEditorWindow


def main():
    app = QApplication(sys.argv)

    mainWindow = NodeEditorWindow()
    mainWindow.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

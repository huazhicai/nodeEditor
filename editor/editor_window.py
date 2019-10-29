from PyQt5.QtCore import QSettings, QPoint, QSize, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction, QTabWidget, QSizePolicy

from editor.utils import resource_path


class TabWidget(QTabWidget):
    doubleClickSignal = pyqtSignal()

    def __init__(self):
        super().__init__()

    def mouseDoubleClickEvent(self, event):
        """鼠标双击事件，双击发射信号，新建一个tab"""
        self.doubleClickSignal.emit()


class NodeEditorWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.createActions()
        self.createMenus()

        self.readSettings()
        self.writeSettings()

    def crateTabWidget(self):
        self.tabWidget = TabWidget()
        self.tabWidget.setSizePolicy(QSizePolicy.Preferred,
                                     QSizePolicy.Ignored)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setTabShape(QTabWidget.Triangular)

        self.tabWidget.tabCloseRequested.connect(self.closeTab)
        self.tabWidget.doubleClickSignal.connect(self.addTab())
        self.tabWidget.setStyleSheet('#pane {margin:0; padding: 0}')

    def closeTab(self, index):
        widget = self.tabWidget.widget(index)

    def addTab(self, isTemplate=False):
        pass

    def createActions(self):
        self.deleteAction = QAction(
            QIcon(resource_path('./images/delete.png')),
            '&Delete item',
            self,
            shortcut='Del',
            statusTip='Delete a item',
            triggered=self.deleteItem)
        self.runGraphAction = QAction(
            QIcon(resource_path('./images/run.png')),
            '&Run graph file',
            self,
            shortcut='Shift+F10',
            statusTip='Execute file',
            triggered=self.runGraph)
        self.newGraphAction = QAction(
            QIcon(resource_path('./images/filenew.png')),
            '&New graph',
            self,
            shortcut='Ctrl+N',
            statusTip='create a new graph',
            triggered=self.newGraph)
        self.openGraphAction = QAction(
            QIcon(resource_path('./images/fileopen.png')),
            '&Open graph',
            self,
            shortcut='Ctrl+O',
            statusTip='open a graph',
            triggered=self.openGraph)
        self.openTemplateAction = QAction(
            QIcon(resource_path('./images/template.png')),
            '&Open Template',
            self,
            shortcut='',
            statusTip='open meta template',
            triggered=self.openTemplate)
        self.closeGraphAction = QAction(
            QIcon(resource_path('./images/fileclose.png')),
            '&Close graph',
            self,
            shortcut='Ctrl+W',
            statusTip='close a graph',
            triggered=self.closeGraph)
        self.saveAction = QAction(
            QIcon(resource_path('./images/filesave.png')),
            '&Save',
            self,
            shortcut='Ctrl+S',
            statusTip='save',
            triggered=self.save)

        self.exportGraphAction = QAction(
            QIcon(resource_path('./images/image.png')),
            '&Export Image',
            self,
            shortcut='',
            statusTip='export to image',
            triggered=self.exportGraph)
        self.convertFileAction = QAction(
            QIcon(resource_path('./images/convert.png')),
            '&Convert File',
            self,
            shortcut='',
            statusTip='convert a graph file',
            triggered=self.convertFile)
        self.exitAction = QAction(
            QIcon(resource_path('./images/exit.png')),
            '&Exit',
            self,
            shortcut='Ctrl+Q',
            statusTip='exit',
            triggered=self.exitMe)
        self.copyAction = QAction(
            QIcon(resource_path('images/copy.png')),
            '&Copy',
            self,
            shortcut='Ctrl+C',
            statusTip='copy an item',
            triggered=self.copyItem)
        self.cutAction = QAction(
            QIcon(resource_path('images/cut.png')),
            '&Cut',
            self,
            shortcut='Ctrl+X',
            statusTip='cut an item',
            triggered=self.cutItem)
        self.pasteAction = QAction(
            QIcon(resource_path('images/paste.png')),
            '&Paste',
            self,
            shortcut='Ctrl+V',
            statusTip='paste an item',
            triggered=self.pasteItem)
        self.resizeSceneAction = QAction(
            QIcon(resource_path('images/resize.png')),
            '&Resize scene',
            self,
            shortcut='',
            statusTip='resize current scene size',
            triggered=self.resizeScene)
        self.undoAction = QAction(
            QIcon(resource_path('images/undo.png')),
            '&Undo',
            self,
            shortcut='Ctrl+Z',
            statusTip='Undo previous operation',
            triggered=self.undo)
        self.redoAction = QAction(
            QIcon(resource_path('images/redo.png')),
            '&Redo',
            self,
            shortcut='Ctrl+Shift+Z',
            statusTip='Redo previous operation',
            triggered=self.redo)
        self.findAction = QAction(
            QIcon(resource_path('images/find.png')),
            '&Find',
            self,
            shortcut='Ctrl+F',
            statusTip='Find item',
            triggered=self.find_)
        self.replaceAction = QAction(
            QIcon(resource_path('images/replace.png')),
            '&Replace',
            self,
            shortcut='Ctrl+H',
            statusTip='Replace some values',
            triggered=self.replace
        )
        self.aboutAction = QAction(
            QIcon(''),
            '&About',
            self,
            shortcut='',
            statusTip='about me',
            triggered=self.aboutMe)
        self.widerAction = QAction(
            QIcon(''),
            '&Wider',
            self,
            shortcut='Ctrl+=',
            statusTip='item wider',
            triggered=self.itemWider)
        self.thinnerAction = QAction(
            QIcon(''),
            '&Thinner',
            self,
            shortcut='Ctrl+-',
            statusTip='item thinner',
            triggered=self.itemThinner)
        self.foldAction = QAction(
            QIcon(resource_path('images/fold.png')),
            '&Fold',
            self,
            shortcut='Ctrl+M',
            statusTip='fold item',
            triggered=self.itemFold)
        self.unfoldAction = QAction(
            QIcon(resource_path('images/unfold.png')),
            '&Unfold',
            self,
            shortcut='Ctrl+Shift+M',
            statusTip='unfold item',
            triggered=self.itemUnfold)
        self.commentAction = QAction(
            QIcon(''),
            '&Comment',
            self,
            shortcut='Ctrl+T',
            statusTip='add comment',
            triggered=self.commentItem)
        self.freeCommentAction = QAction(
            QIcon(''),
            '&Free Comment',
            self,
            shortcut='Ctrl+G',
            statusTip='add free comment',
            triggered=self.freeComment)
        self.showQuickAction = QAction(
            QIcon(''),
            '&Show Quick Bar',
            self,
            shortcut='',
            statusTip='show the quick bar',
            triggered=self.showQuick)
        self.hideQuickAction = QAction(
            QIcon(''),
            '&Hide Quick Bar',
            self,
            shortcut='',
            statusTip='hide the quick bar',
            triggered=self.hideQuick)
        self.enterFullScreenAction = QAction(
            QIcon(''),
            '&Enter Full Screen',
            self,
            shortcut='',
            statusTip='enter full screen',
            triggered=self.enterFull)
        self.exitFullScreenAction = QAction(
            QIcon(''),
            '&Exit Full Screen',
            self,
            shortcut='Esc',
            statusTip='exit full screen',
            triggered=self.exitFull)

    def newGraph(self):
        pass

    def runGraph(self):
        pass

    def openGraph(self):
        pass

    def openTemplate(self):
        pass

    def save(self):
        pass

    def closeGraph(self):
        pass

    def exportGraph(self):
        pass

    def convertFile(self):
        pass

    def exitMe(self):
        pass

    def deleteItem(self):
        pass
        # 当前标签场景
        # graphicWidget = self.tabWidget.currentWidget()
        # if not isinstance(graphicWidget, widgets.GraphWidget):
        #     return
        # graphicWidget.deleteItem()

    def copyItem(self):
        pass

    def cutItem(self):
        pass

    def pasteItem(self):
        pass

    def resizeScene(self):
        pass

    def undo(self):
        pass

    def redo(self):
        pass

    def find_(self):
        pass

    def replace(self):
        pass

    def aboutMe(self):
        pass

    def itemWider(self):
        pass

    def itemThinner(self):
        pass

    def itemFold(self):
        pass

    def itemUnfold(self):
        pass

    def commentItem(self):
        pass

    def freeComment(self):
        pass

    def showQuick(self):
        pass

    def hideQuick(self):
        pass

    def enterFull(self):
        pass

    def exitFull(self):
        pass

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu('&File')
        self.fileMenu.addAction(self.newGraphAction)
        self.fileMenu.addAction(self.runGraphAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.openGraphAction)
        self.fileMenu.addAction(self.openTemplateAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.closeGraphAction)
        self.fileMenu.addAction(self.exportGraphAction)
        self.fileMenu.addAction(self.convertFileAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)

        self.editMenu = self.menuBar().addMenu('&Edit')
        self.editMenu.addAction(self.deleteAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.undoAction)
        self.editMenu.addAction(self.redoAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.copyAction)
        self.editMenu.addAction(self.cutAction)
        self.editMenu.addAction(self.pasteAction)
        self.fileMenu.addSeparator()
        self.editMenu.addAction(self.findAction)
        self.editMenu.addAction(self.replaceAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.resizeSceneAction)

        self.itemMenu = self.menuBar().addMenu('&Item')
        self.itemMenu.addAction(self.widerAction)
        self.itemMenu.addAction(self.thinnerAction)
        self.itemMenu.addAction(self.foldAction)
        self.itemMenu.addAction(self.unfoldAction)
        self.itemMenu.addAction(self.commentAction)
        self.itemMenu.addAction(self.freeCommentAction)

        self.viewMenu = self.menuBar().addMenu('&View')
        self.viewMenu.addAction(self.showQuickAction)
        self.viewMenu.addAction(self.hideQuickAction)
        self.viewMenu.addAction(self.enterFullScreenAction)
        self.viewMenu.addAction(self.exitFullScreenAction)

        self.aboutMenu = self.menuBar().addMenu('&Help')
        self.aboutMenu.addAction(self.aboutAction)

    def readSettings(self):
        settings = QSettings()
        pos = settings.value('pos', QPoint(100, 100))
        size = settings.value('size', QSize(600, 600))
        self.move(pos)
        self.resize(size)

    def writeSettings(self):
        settings = QSettings()
        settings.setValue('pos', self.pos())
        settings.setValue('size', self.size())

from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QWidget, QToolBar, QPushButton

class AbstractWindow(QMainWindow):
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__()
    
    def setupSidebarLayout(self,sidebarLayout, mainLayout):
        layout = QHBoxLayout()
        left = QWidget()
        left.setLayout(sidebarLayout)

        right = QWidget()
        right.setLayout(mainLayout)
        
        layout.addWidget(left)
        layout.addWidget(right)
        layout.setStretch(0, 3)
        layout.setStretch(1, 7)

        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setLayout(layout)


    # automatizing setting the ToolBar for the app 
    def setToolBar(self, menuItems):
        tools = QToolBar()
        self.addToolBar(tools)
        for item in menuItems :
            tools.addWidget(item)
    

class QPrimaryButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.setStyleSheet("background-color: indigo;color:white;font-weight:bold;")


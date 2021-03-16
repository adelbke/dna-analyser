# -*- coding: utf-8 -*-

"""This module provides views to manage the contacts table."""

from PyQt5.QtWidgets import (
    QLabel, QPushButton, QVBoxLayout
)

from .settings import window_title
from .components import AbstractWindow, QPrimaryButton



class Window(AbstractWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__()
        self.setWindowTitle(window_title)

        self.setupUI()

    def setupUI(self):
        """Setup the main window's GUI."""
        # Create Buttons
        self.addButton = QPrimaryButton("Add")
        self.deleteButton = QPushButton("Delete")
        self.clearAllButton = QPushButton("clear all")

        self.setToolBar([
            QPushButton('hello'),
            QPushButton('world')
        ])

        # Lay out the GUI
        sidebarLayout = QVBoxLayout()
        sidebarLayout.addWidget(self.addButton)
        sidebarLayout.addWidget(self.deleteButton)
        sidebarLayout.addWidget(self.clearAllButton)


        mainLayout = QVBoxLayout()
        label = QLabel()
        label.setText("Hello world")
        mainLayout.addWidget(label)

        self.setupSidebarLayout(sidebarLayout, mainLayout)



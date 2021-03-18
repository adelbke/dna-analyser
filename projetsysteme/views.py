# -*- coding: utf-8 -*-

"""This module provides views to manage the contacts table."""

import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QLabel, QLayout, QPushButton, QVBoxLayout
)

from .settings import window_title
from .components import AbstractWindow, SidebarLayout, MainLayout



class Window(AbstractWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__()
        self.setWindowTitle(window_title)
        self.setMenuItems()
        self.setupUI()


    def setupUI(self):
        """Setup the main window's GUI."""
        # Lay out the GUI
        self.sidebarLayout = SidebarLayout()
        self.mainLayout = MainLayout()
        self.setupMainLayout(self.sidebarLayout, self.mainLayout)


    

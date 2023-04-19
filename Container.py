import sys 
if sys.version_info.major == 2:
    from PySide.QtGui import *
    from PySide.QtCore import *
    
if sys.version_info.major == 3:    
    from PySide2.QtWidgets import *
    from PySide2.QtGui import *
    from PySide2.QtCore import *
class Header(QWidget):
    """Header class for collapsible group"""

    def __init__(self, name, content_widget):
        """Header Class Constructor to initialize the object.

        Args:
            name (str): Name for the header
            content_widget (QtWidgets.QWidget): Widget containing child elements
        """
        super(Header, self).__init__()
        self.content = content_widget
        self.expand_ico = QPixmap(":teDownArrow.png")
        self.collapse_ico = QPixmap(":teRightArrow.png")
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        stacked = QStackedLayout(self)
        stacked.setStackingMode(QStackedLayout.StackAll)
        self.background = QLabel()
        self.background.setStyleSheet("QLabel{ background-color: rgb(93, 93, 93); border-radius:2px}")

        self.widget = QWidget()
        self.layout = QHBoxLayout(self.widget)

        self.icon = QLabel()
        self.icon.setPixmap(self.expand_ico)
        self.layout.addWidget(self.icon)
        self.layout.setContentsMargins(11, 0, 11, 0)

        font = QFont()
        font.setBold(True)
        self.label = QLabel(name)
        self.label.setFont(font)

        self.layout.addWidget(self.label)
        self.layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        stacked.addWidget(self.widget)
        stacked.addWidget(self.background)
        self.background.setMinimumHeight(self.layout.sizeHint().height() * 1.5)

    def mousePressEvent(self, *args):
        """Handle mouse events, call the function to toggle groups"""
        self.expand() if not self.content.isVisible() else self.collapse()

    def expand(self):
        self.content.setVisible(True)
        self.icon.setPixmap(self.expand_ico)

    def collapse(self):
        self.content.setVisible(False)
        self.icon.setPixmap(self.collapse_ico)


class Container(QWidget):
    """Class for creating a collapsible group similar to how it is implement in Maya

        Examples:
            Simple example of how to add a Container to a QVBoxLayout and attach a QGridLayout

            >>> layout = QtWidgets.QVBoxLayout()
            >>> container = Container("Group")
            >>> layout.addWidget(container)
            >>> content_layout = QtWidgets.QGridLayout(container.contentWidget)
            >>> content_layout.addWidget(QtWidgets.QPushButton("Button"))
    """
    def __init__(self, name, color_background=False):
        """Container Class Constructor to initialize the object

        Args:
            name (str): Name for the header
            color_background (bool): whether or not to color the background lighter like in maya
        """
        super(Container, self).__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self._content_widget = QWidget()
        if color_background:
            self._content_widget.setStyleSheet(".QWidget{background-color: rgb(73, 73, 73); "
                                               "margin-left: 2px; margin-right: 2px}")
        self.header = Header(name, self._content_widget)
        layout.addWidget(self.header)
        layout.addWidget(self._content_widget)

        # assign header methods to instance attributes so they can be called outside of this class
        self.collapse = self.header.collapse
        self.expand = self.header.expand
        self.toggle = self.header.mousePressEvent

    @property
    def contentWidget(self):
        """Getter for the content widget

        Returns: Content widget
        """
        return self._content_widget

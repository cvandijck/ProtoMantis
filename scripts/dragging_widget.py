from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

from protomantis.ui.componentwidget import ComponentWidget


def clicked():
    print("click as normal!")


if __name__ == "__main__":
    app = QApplication([])

    # app.setOverrideCursor(Qt.CursorShape.WaitCursor)
    # do lengthy process
    # app.restoreOverrideCursor()

    window = QMainWindow()
    window.resize(800, 600)

    component = ComponentWidget("Button", window)
    component.clicked.connect(clicked)

    window.show()
    app.exec()

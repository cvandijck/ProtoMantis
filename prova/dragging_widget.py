from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class DraggablePushButton(QPushButton):
    DEADZONE = 3

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__mousePressPos = None
        self.__mouseMovePos = None

    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        
        if event.button() == Qt.MouseButton.LeftButton:
            self.__mousePressPos = event.globalPosition()
            self.__mouseMovePos = event.globalPosition()

        super(DraggablePushButton, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            # adjust offset from clicked point to origin of widget
            curr_pos = self.mapToGlobal(self.pos())
            global_pos = event.globalPosition()
            diff = global_pos - self.__mouseMovePos
            new_pos = self.mapFromGlobal(curr_pos + diff.toPoint())

            # clip
            new_pos.setX(max(0, new_pos.x()))
            new_pos.setY(max(0, new_pos.y()))
            new_pos.setX(min(new_pos.x(), self.parentWidget().width() - self.width()))
            new_pos.setY(min(new_pos.y(), self.parentWidget().height() - self.height()))

            self.move(new_pos)
            self.__mouseMovePos = global_pos

        super(DraggablePushButton, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPosition() - self.__mousePressPos
            if moved.manhattanLength() > self.DEADZONE:
                event.ignore()
                return

        super(DraggablePushButton, self).mouseReleaseEvent(event)


def clicked():
    print("click as normal!")


if __name__ == "__main__":
    app = QApplication([])
    window = QMainWindow()
    window.resize(800, 600)

    button = DraggablePushButton("Button", window)
    button.clicked.connect(clicked)

    window.show()
    app.exec()

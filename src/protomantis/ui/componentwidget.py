from PyQt6.QtCore import Qt, QPoint
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import QPushButton, QApplication, QWidget


def get_constrained_cursor_pos(cursor: QCursor, parent: QWidget):
    top_left = parent.pos()
    bottom_right = QPoint(top_left.x() + parent.width(), top_left.y() + parent.height())

    new_cursor_pos = QPoint(cursor.pos())
    new_cursor_pos.setX(min(max(top_left.x(), new_cursor_pos.x()), bottom_right.x()))
    new_cursor_pos.setY(min(max(top_left.y(), new_cursor_pos.y()), bottom_right.y()))
    print(cursor.pos(), new_cursor_pos)
    return new_cursor_pos


class ComponentWidget(QPushButton):
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

        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            # adjust offset from clicked point to origin of widget
            global_pos = event.globalPosition()
            curr_pos = self.mapToGlobal(self.pos())
            diff = global_pos - self.__mouseMovePos
            new_pos = self.mapFromGlobal(curr_pos + diff.toPoint())

            self.move(new_pos)
            # constrained_cursor_pos = get_constrained_cursor_pos(self.cursor(), self.parentWidget())
            # self.cursor().setPos(constrained_cursor_pos)
            self.__mouseMovePos = global_pos

        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPosition() - self.__mousePressPos
            if moved.manhattanLength() > self.DEADZONE:
                event.ignore()
                return

        super().mouseReleaseEvent(event)

    def moveConstrained(self, pos: QPoint):
        new_pos = QPoint(min(max(0, pos.x()), self.parentWidget().width() - self.width()),
                         min(max(0, pos.y()), self.parentWidget().height() - self.height()))
        self.move(new_pos)

        # diff = new_pos - pos
        # cursor = self.cursor()
        # cursor_pos = cursor.pos()
        # new_cursor_pos = cursor_pos + diff
        # print(f'{new_cursor_pos=}')
        # cursor.setPos(new_cursor_pos)

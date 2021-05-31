from PySide6 import QtCore
from PySide6.QtWidgets import QLabel

class QLabelWithPosition(QLabel):
    on_display = QtCore.Signal(bool) 
    mouseMove = QtCore.Signal(object) 
    mousePress = QtCore.Signal(object)
    mouseRelease = QtCore.Signal(object)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._loaded = False
        self.show()
        self.setMouseTracking(True)

#    def showEvent(self, event):
#        if not self._loaded:
#            self._loaded=True
#        self.on_display.emit(self._loaded)

    def mouseMoveEvent(self, event):
        # print(event.x(), event.y())
        #print("button:", event.button())
        #print("buttons:", event.buttons())
        #print("moving")
        self.mouseMove.emit(event)
        #return event

    def mousePressEvent(self, event):
        #print(event.x(), event.y())
        #print("button press:", event.button())
        #print("buttons:", event.buttons())
        #print(dir(event.buttons()))
        self.mousePress.emit(event)

    def mouseReleaseEvent(self, event):
        #print("button release:", event.button())
        self.mouseRelease.emit(event)


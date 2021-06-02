import sys
import os
import numpy as np
import cv2
#from Functions import *
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import *
from gui.ui_main import Ui_MainWindow
from PySide6.QtGui import QImage, QPixmap


class MainWindow(QMainWindow):

    def __init__(self, app):
        # QMainWindow.__init__(self)
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.label_channel = 1
        self.d = 112
        self.SIDE = 480
        self.INTERVAL = self.SIDE/self.d
        self.HIGH_CONTRAST = False
        self.HIGH_CONTRAST_MOUSE = False
        self.SHOW_MASK = True
        self.SHOW_GRIDS = False 
        self.display_timer = QtCore.QTimer()
        self.load_dirs()
        self.img_th = None
        self.timer = QtCore.QTimer()
        self.ORI_IMG = None
        self.LEFT_BUTTON_DOWN = False
        self.MODE = 0
        self.BRUSHES = [1, 3, 5, 7, 9, 13, 17, 21]
        self.BRUSH_SIZE = self.BRUSHES[1]
        self.MAT = None
        self.MASK = None
        self.MOUSE_MASK = np.zeros((self.SIDE, self.SIDE)).astype(np.uint8)
        self.LAST_X = None
        self.LAST_Y = None
        self.CURRENT_IDX = None
        self.setup_functions()
        self.show()
       
    def init_mat(self):
        return np.zeros((self.d, self.d, self.label_channel))
        
    def setup_functions(self):
        self.ui.pushButton_images.clicked.connect(self.reset_image_list)
        self.ui.pushButton_set_label.clicked.connect(self.reset_label_dir)
        # Load image and mat
        self.ui.listWidget.itemDoubleClicked.connect(lambda item: self.load_image_and_mat(item))
        # Set mode
        self.ui.pushButton_brush.clicked.connect(lambda: self.set_mode(0))
        self.ui.pushButton_eraser.clicked.connect(lambda: self.set_mode(1))
        self.ui.checkBox_highlight_mask.stateChanged.connect(self.set_highcontrast_mask)
        self.ui.checkBox_highlight_mouse.stateChanged.connect(self.set_highcontrast_mouse)
        self.ui.checkBox_showmask.stateChanged.connect(self.set_showmask)
        # Brush size
        self.ui.pushButton_brush_1.clicked.connect(lambda: self.set_brush_size(0))
        self.ui.pushButton_brush_2.clicked.connect(lambda: self.set_brush_size(1))
        self.ui.pushButton_brush_3.clicked.connect(lambda: self.set_brush_size(2))
        self.ui.pushButton_brush_4.clicked.connect(lambda: self.set_brush_size(3))
        self.ui.pushButton_brush_5.clicked.connect(lambda: self.set_brush_size(4))
        self.ui.pushButton_brush_6.clicked.connect(lambda: self.set_brush_size(5))
        self.ui.pushButton_brush_7.clicked.connect(lambda: self.set_brush_size(6))
        self.ui.pushButton_brush_8.clicked.connect(lambda: self.set_brush_size(7))
        # Set image label
        self.ui.label_image.mouseMove.connect(lambda event: self.update_image_label(event))
        self.ui.label_image.mousePress.connect(lambda event: self.mouse_press(event))
        self.ui.label_image.mouseRelease.connect(lambda event: self.mouse_release(event))
        # Read & save mat
        self.ui.pushButton_save.clicked.connect(self.save_mat)
        self.ui.pushButton_next.clicked.connect(lambda: self.select_next_image(True))
        self.ui.pushButton_back.clicked.connect(lambda: self.select_next_image(False))

    def load_dirs(self):
        try:
            with open('dir.txt', 'r') as f:
                self.IMAGE_DIR = f.readline().rstrip('\n')
                self.LABEL_DIR = f.readline()
            assert os.path.exists(self.IMAGE_DIR)
            assert os.path.exists(self.LABEL_DIR)

        except BaseException as e:
            print(e)
            self.IMAGE_DIR = os.getcwd()
            self.LABEL_DIR = os.getcwd()
        finally:
            # set label text
            self.ui.label_label_dir.setText(self.LABEL_DIR)
            # set image list
            all_file = os.listdir(self.IMAGE_DIR)
            self.image_list = [i for i in all_file if i.endswith(".png") or i.endswith(".jpg")]
            self.image_list.sort(key=lambda x:x[:-4])
            self.ui.listWidget.clear()
            for i, f in enumerate(self.image_list):
                item = QListWidgetItem()
                item.setText(f)
                self.ui.listWidget.insertItem(i, item)

    def write_dirs(self):
        with open('dir.txt', 'w') as f:
            f.writelines([self.IMAGE_DIR, '\n', self.LABEL_DIR])

    def select_next_image(self, Next):
        if self.CURRENT_IDX is None:
            return
        if Next: # Next
            self.CURRENT_IDX += 1
        else: # Back
            self.CURRENT_IDX -= 1
        if self.CURRENT_IDX < 0:
            self.CURRENT_IDX = 0
        elif self.CURRENT_IDX >= len(self.image_list):
            self.CURRENT_IDX = len(self.image_list) - 1
        self.ui.listWidget.setCurrentRow(self.CURRENT_IDX)
        self.load_image_and_mat(self.ui.listWidget.currentItem())

    def set_mode(self, mode):
        self.MODE = mode

    def set_brush_size(self, size_idx):
        self.BRUSH_SIZE = self.BRUSHES[size_idx]
        self.update_image_label(None)

    def reset_label_dir(self):
        label_dir = QtWidgets.QFileDialog.getExistingDirectory()
        if not label_dir:
            return
        else:
            self.LABEL_DIR = label_dir
        self.ui.label_label_dir.setText(self.LABEL_DIR)
        self.write_dirs()

    def reset_image_list(self):
        image_dir = QtWidgets.QFileDialog.getExistingDirectory()
        if not image_dir:
            return
        else:
            self.IMAGE_DIR = image_dir
        all_file = os.listdir(self.IMAGE_DIR)
        self.image_list = [i for i in all_file if i.endswith(".png") or i.endswith(".jpg") or i.endswith(".bmp")]
        self.image_list.sort(key=lambda x:x[:-4])
        self.ui.listWidget.clear()
        for i, f in enumerate(self.image_list):
            item = QListWidgetItem()
            item.setText(f)
            self.ui.listWidget.insertItem(i, item)
        self.write_dirs()

    def mouse_press(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.LEFT_BUTTON_DOWN = True
            self.update_image_label(event)

    def mouse_release(self, event):
        if event.button() == QtCore.Qt.MouseButton.LeftButton:
            self.LEFT_BUTTON_DOWN = False
        
    def set_highcontrast_mask(self):
        self.HIGH_CONTRAST = self.ui.checkBox_highlight_mask.isChecked()
        self.update_image_label(None)

    def set_highcontrast_mouse(self):
        self.HIGH_CONTRAST_MOUSE = self.ui.checkBox_highlight_mouse.isChecked()
        self.update_image_label(None)

    def set_showmask(self):
        self.SHOW_MASK = self.ui.checkBox_showmask.isChecked()
        self.update_image_label(None)

    def save_mat(self):
        np.save(self.LABEL_PATH, self.MAT)
        self.ui.statusbar.showMessage("Saved mask at: {}".format(self.LABEL_PATH), 8000)
        print("Saved mask at: {}".format(self.LABEL_PATH))

    def load_image_and_mat(self, item):
        if item is None:
            return
        image_name = item.text()
        self.CURRENT_IDX = self.ui.listWidget.currentRow()
        # set name
        self.ui.label_filename.setText(image_name)
        # load image
        self.ORI_IMG = cv2.imread(os.path.join(self.IMAGE_DIR, image_name))
        self.ORI_IMG = cv2.resize(self.ORI_IMG, (self.SIDE, self.SIDE))
        self.ORI_IMG = cv2.cvtColor(self.ORI_IMG, cv2.COLOR_BGR2RGB)
        self.channel = self.ORI_IMG.shape[2]
        # load mat and mask
        self.LABEL_PATH = os.path.join(self.LABEL_DIR, image_name[:image_name.find('.')] + '.npy')
        # set blank mask
        self.MASK = np.zeros((self.SIDE, self.SIDE)).astype(np.uint8)
        if os.path.isfile(self.LABEL_PATH):
            try:
                # load mat
                self.MAT = np.load(self.LABEL_PATH)
                # load mask from mat
                for i in range(self.d):
                    for j in range(self.d):
                        if self.MAT[i, j] == 1:
                            n = 225
                        else:
                            n = 0
                        start_pt = (int(j * self.INTERVAL), int(i * self.INTERVAL))
                        end_pt = (int((j + 1) * self.INTERVAL), int((i + 1) * self.INTERVAL))
                        self.MASK = cv2.rectangle(self.MASK, start_pt, end_pt, n, -1)
            except BaseException as e:
                print("error during loading mask")
                print(type(e).__name__, ':', str(e))
                self.MAT = self.init_mat()
                self.MASK = np.zeros((self.SIDE, self.SIDE)).astype(np.uint8)
        else:
            self.MAT = self.init_mat()
        # load image on image_label
        self.update_image_label(None)

    def update_mat_and_mask(self, event):
        if self.LEFT_BUTTON_DOWN:
            offset = int((self.BRUSH_SIZE - 1) / 2)
            grid_x = int((self.d * event.x()) / self.SIDE)
            grid_y = int((self.d * event.y()) / self.SIDE)
            if self.MODE == 0:  # Brush
                n = 255  # for mask
                m = 1  # for mat
            elif self.MODE == 1:  # Eraser
                n = 0
                m = 0
            # Mat mask
            start_pt = (int((grid_x - offset) * self.INTERVAL), int((grid_y - offset) * self.INTERVAL))
            end_pt = (int((grid_x + 1 + offset) * self.INTERVAL), int((grid_y + 1 + offset) * self.INTERVAL))
            self.MASK = cv2.rectangle(self.MASK, start_pt, end_pt, n, -1)
            # Mat
            coords = [grid_y - offset, grid_y + offset + 1, grid_x - offset, grid_x + offset +1]
            y0, y1, x0, x1 = np.clip(coords, 0, self.SIDE)
            self.MAT[y0:y1, x0:x1] = m

    def update_mouse_mask(self, move_event):
        self.MOUSE_MASK = np.zeros((self.SIDE, self.SIDE)).astype(np.uint8)
        if not move_event and self.LAST_X is not None and self.LAST_Y is not None:
            x, y = self.LAST_X, self.LAST_Y
        elif move_event:
            x, y = move_event.x(), move_event.y()
            self.LAST_X, self.LAST_Y = x, y  # if mouse not move
        else:
            return
        offset = int((self.BRUSH_SIZE-1)/2)
        grid_x = int((self.d*x)/self.SIDE) 
        grid_y = int((self.d*y)/self.SIDE)
        n = 255
        start_pt = (int((grid_x-offset)*self.INTERVAL), int((grid_y-offset)*self.INTERVAL))
        end_pt = (int((grid_x+1+offset)*self.INTERVAL), int((grid_y+1+offset)*self.INTERVAL))
        self.MOUSE_MASK = cv2.rectangle(self.MOUSE_MASK, start_pt, end_pt, n, -1)

    def apply_mask(self):
        # Apply mouse mask
        if self.HIGH_CONTRAST_MOUSE:
            MOUSE_MASK_CH3 = cv2.cvtColor(self.MOUSE_MASK, cv2.COLOR_GRAY2RGB) # 255, background 0, 3 channels
            MOUSE_MASK_CH3 = 2 * (-(MOUSE_MASK_CH3 / 255))  # -2, background 0
            MOUSE_MASK_CH3 = MOUSE_MASK_CH3 + 1  # -1, background 1
            MOUSE_MASK_CH3 = MOUSE_MASK_CH3.astype(np.uint8)
            self.IMG_SHOW *= MOUSE_MASK_CH3
        else:
            self.IMG_SHOW[:, :, 0] = cv2.addWeighted(self.ORI_IMG[:, :, 0], 1, self.MOUSE_MASK, 0.6, 0)
            self.IMG_SHOW[:, :, 2] = cv2.addWeighted(self.ORI_IMG[:, :, 2], 1, self.MOUSE_MASK, 0.6, 0)
        # Apply mat mask
        if self.SHOW_MASK is True:
            if self.HIGH_CONTRAST:
                self.IMG_SHOW[:, :, 1] = cv2.addWeighted(self.IMG_SHOW[:, :, 1], 0.8, self.MASK, 0.9, 0)
            else:
                self.IMG_SHOW[:, :, 1] = cv2.addWeighted(self.IMG_SHOW[:, :, 1], 1, self.MASK, 0.2, 0)

    def update_image_label(self, move_event):
        if self.ORI_IMG is None:
            return
        else:
            self.IMG_SHOW = self.ORI_IMG.copy()
            self.update_mouse_mask(move_event)
            if move_event is not None:
                # self.update_mouse_mask(move_event)
                self.update_mat_and_mask(move_event)
            self.apply_mask()
            # Show image on QLabel
            bytesPerLine = self.channel * self.SIDE
            convertToQtFormat = QImage(self.IMG_SHOW.data, self.SIDE, self.SIDE, bytesPerLine, QImage.Format_RGB888)
            #self.img_show = convertToQtFormat.scaled(self.SIDE, self.SIDE, QtCore.Qt.KeepAspectRatio)
            self.ui.label_image.setPixmap(QPixmap.fromImage(convertToQtFormat))

		    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow(app)
    # app.aboutToQuit.connect(window.on_exit)
    sys.exit(app.exec_())

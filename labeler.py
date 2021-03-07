import cv2
import numpy as np
import os
import tkinter as tk
import copy
import sys
import argparse


def init_mat():
    MAT = np.zeros((d, d, 1))
    return MAT


def draw_grids(img):
    img = img.copy()
    for i in range(1, d):
        x = int(i*INTERVAL)
        cv2.line(img, (x, 0), (x, SIDE), 255) 
        cv2.line(img, (0, x), (SIDE, x), 255)
    return img    


def add_grids(img):
    green_channel = img[:,:,1]
    img[:,:,1] = cv2.bitwise_or(green_channel,  GRIDS,  mask=green_channel)  
    return img


def add_mask(img):
    global MOUSE_MASK, MASK
    if SHOW_MASK:  # show mask on green channel
        if HIGH_CONTRAST:
            img[:,:,1] = cv2.addWeighted(ori_img[:,:,1], 0.8, MASK, 0.9, 0)
        else:
            img[:,:,1] = cv2.addWeighted(ori_img[:,:,1], 1, MASK, 0.2, 0)
    img[:,:,0] = cv2.addWeighted(ori_img[:,:,0], 1, MOUSE_MASK, 0.6, 0)
    img[:,:,2] = cv2.addWeighted(ori_img[:,:,2], 1, MOUSE_MASK, 0.6, 0)
    return img


def update_mask(x, y, n):
    global MASK
    offset = int((BRUSH_SIZE-1)/2)
    grid_x = int((d*x)/SIDE) 
    grid_y = int((d*y)/SIDE)
    if n != 0:
        n = 255
    start_pt = (int((grid_x-offset)*INTERVAL), int((grid_y-offset)*INTERVAL))
    end_pt = (int((grid_x+1+offset)*INTERVAL), int((grid_y+1+offset)*INTERVAL))
    MASK = cv2.rectangle(MASK, start_pt, end_pt, n, -1)


def update_mat(x, y, n):
    offset = int((BRUSH_SIZE-1)/2)
    grid_x = int((d*x)/SIDE) 
    grid_y = int((d*y)/SIDE)
    #MAT[grid_y, grid_x] = n 
    coords = [grid_y-offset, grid_y+offset+1, grid_x-offset, grid_x+offset+1]
    y0, y1, x0, x1 = np.clip(coords, 0, SIDE)
    MAT[y0:y1, x0:x1] = n


def update_mouse_mask(x=None, y=None):
    global MOUSE_MASK, LAST_X, LAST_Y
    if (not x) and (not y):
        x, y = LAST_X, LAST_Y
    LAST_X, LAST_Y = x, y
    MOUSE_MASK = np.zeros((SIDE, SIDE)).astype(np.uint8)
    offset = int((BRUSH_SIZE-1)/2)
    grid_x = int((d*x)/SIDE) 
    grid_y = int((d*y)/SIDE)
    n=255
    start_pt = (int((grid_x-offset)*INTERVAL), int((grid_y-offset)*INTERVAL))
    end_pt = (int((grid_x+1+offset)*INTERVAL), int((grid_y+1+offset)*INTERVAL))
    MOUSE_MASK = cv2.rectangle(MOUSE_MASK, start_pt, end_pt, n, -1)


def mousecontrol(event, x, y, flags, param):
    global STAT
    n = 1 # draw by default
    if MODE != 0: # erase mode
        n = 0
    if event == cv2.EVENT_LBUTTONDOWN:
        STAT = 1 # LBUTTONTDOWN
        update_mat(x, y, n)
        update_mask(x, y, n)
    elif event == cv2.EVENT_MOUSEMOVE:
        if STAT == 1:
            update_mat(x, y, n)
            update_mask(x, y, n)
    elif event == cv2.EVENT_LBUTTONUP:
        STAT = 0
        LAST_GRID = None
    update_mouse_mask(x, y)


def save_mat():
    global LABEL_PATH
    #save_path = os.path.join(OUTPUT_PATH, '001')
    np.save(LABEL_PATH, MAT)
    print('save at: {}'.format(LABEL_PATH))


def update_whole_mask():
    ## update whole mask after load .npy
    global MASK, MAT
    d = MAT.shape[0]
    for i in range(d):
        for j in range(d):
            if MAT[i,j] == 1:
                n = 255
            else:
                n = 0
            start_pt = (int(j*INTERVAL), int(i*INTERVAL))
            end_pt = (int((j+1)*INTERVAL), int((i+1)*INTERVAL))
            MASK = cv2.rectangle(MASK, start_pt, end_pt, n, -1)


def labeller(img):
    global ori_img, MODE, SHOW_GRID, IMG_ITER, HIGH_CONTRAST, SHOW_MASK, MOUSE_MASK, BRUSH_SIZE, NEXT
    h, w = img.shape[:2]
    ori_img = cv2.resize(img, (SIDE, SIDE))
    #grid_img = add_grids(ori_img)
    cv2.namedWindow('grids')
    cv2.setMouseCallback('grids', mousecontrol)
    while True:
        masked_img = add_mask(ori_img.copy())
        if SHOW_GRID:
            grid_img = add_grids(masked_img)
        else:
            grid_img = masked_img
        cv2.imshow('grids', grid_img)
        #cv2.imshow('M', cv2.resize(MAT, (SIDE,SIDE)))
        k = cv2.waitKey(1) & 0xFF
        if k == 27: # exit
            #IMG_ITER = iter([])
            NEXT = 0
            break
        elif k == ord('e'): # erase
            MODE = 1
        elif k == ord('b'): # bursh
            MODE = 0
        elif k == ord('s'):
            save_mat()
        elif k == ord('g'):
            SHOW_GRID = not(SHOW_GRID)
        elif k == ord(']'):
            NEXT = 1
            break
        elif k == ord('['):
            NEXT = 2
            break 
        elif k == ord('x'):
            HIGH_CONTRAST = not(HIGH_CONTRAST)
        elif k == ord('r'):
            SHOW_MASK = not(SHOW_MASK)
            print('SHOW_MASK:', SHOW_MASK)
        elif k == ord('1'):
            BRUSH_SIZE = 1
            update_mouse_mask()
        elif k == ord('2'):
            BRUSH_SIZE = 3
            update_mouse_mask()
        elif k == ord('3'):
            BRUSH_SIZE = 5
            update_mouse_mask()
        elif k == ord('4'):
            BRUSH_SIZE = 7
            update_mouse_mask()
        elif k == ord('5'):
            BRUSH_SIZE = 9 
            update_mouse_mask()
        elif k == ord('6'):
            BRUSH_SIZE = 11
            update_mouse_mask()
    cv2.destroyAllWindows()
    

def main():
    global MASK, MAT, LABEL_PATH, IDX
    #img_name = next(IMG_ITER, None)
    #if img_name is None:
    #    exit()
    if NEXT == 1:
        IDX += 1
    elif NEXT == 2:
        IDX -= 1
    else:
        exit()
    img_name = IMG_LIST[IDX]
    img_path = os.path.join(IMG_DIR, img_name)
    print(img_path)
    LABEL_PATH = os.path.join(OUTPUT_PATH, img_name[:img_name.find('.')]+'.npy')
    if os.path.isfile(LABEL_PATH):
        MAT = np.load(LABEL_PATH)
        print(LABEL_PATH)
    else:
        MAT = init_mat()
        print('label:', 'None')
    img = cv2.imread(img_path)
    update_whole_mask()
    labeller(img)


## STAT
## 0: left button up, 1: left button down
STAT = 0
## MODE
## 0: bursh, 1: erase
MODE = 0
## HIGH MASK CONTRAST 
HIGH_CONTRAST = False
SHOW_MASK = True
SHOW_GRID = False
SIDE = 800
d = 112
INTERVAL = SIDE/d
BRUSH_LIST = [1, 3, 5]
BRUSH_SIZE = BRUSH_LIST[1] 
MAT= init_mat()
MASK = np.zeros((SIDE, SIDE)).astype(np.uint8)
MOUSE_MASK = np.zeros((SIDE, SIDE)).astype(np.uint8)
GRIDS = draw_grids(np.zeros((SIDE, SIDE)).astype(np.uint8))

IMG_DIR = './data-cnn/img'
IMG_ITER = iter(sorted(os.listdir(IMG_DIR)))
OUTPUT_PATH = './data-cnn/label'
IMG_LIST = list(IMG_ITER)
IDX = 0
## NEXT
# 0: exit, 1: next, 2: previous
NEXT = True

if __name__ == '__main__':
    #main('data-cnn/img/001.png')
    parser = argparse.ArgumentParser()
    parser.add_argument('start_img', nargs='?', type=str, default=None)
    FLAGS = parser.parse_args()
    start_img = FLAGS.start_img
    if start_img and start_img.find('.')<0:
        print('start')
        start_img = start_img+'.png'
        try:
            idx = IMG_LIST.index(start_img)
            IDX = idx
        except:
            print("Can't find", start_img)
    IDX -= 1
    while True:
        MASK = np.zeros((SIDE, SIDE)).astype(np.uint8)
        main()

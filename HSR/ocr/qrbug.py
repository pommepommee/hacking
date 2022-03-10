import numpy as np
import cv2
from matplotlib import cm
from PIL import Image
from pyzbar import pyzbar

flags = []
im = cv2.imread("hsr_qrbug.png")
M = 87
N = 87
tiles = [im[x:x+M,y:y+N] for x in range(0,im.shape[0],M) for y in range(0,im.shape[1],N)]
for tile in tiles:
    qr = cv2.QRCodeDetector()
    new = Image.fromarray(tile.astype(np.uint8))
    # data, points, _ = qr.detectAndDecode(tile)
    data = pyzbar.decode(new)
    flags.append((data[0].data).decode('ascii'))
for flag in flags:
    if '?' in flag:
        print(flag)
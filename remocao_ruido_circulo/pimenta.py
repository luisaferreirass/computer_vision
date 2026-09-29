import cv2
import sys
import numpy as np
import random
import matplotlib.pyplot as plt
import math

imgPath = cv2.imread(sys.argv[1], 0)
cx_real = int(sys.argv[2])
cy_real = int(sys.argv[3])
r_real = int(sys.argv[4])

img = cv2.imread(imgPath, 0)

# Aplicar o filtro
imgSemRuido = cv2.GaussianBlur(img, (3, 3), 0)
imgSemRuido = cv2.medianBlur(img, 3)

# Identificar o circulo

# Tirar as medidas

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.subplot(1, 2, 2)
plt.imshow(imgResultante, cmap='gray')
plt.title('PSNR = ' + str("%.2f" % cv2.PSNR(imgResultante, imgOriginal)))
plt.show()
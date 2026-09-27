import cv2
import sys
import numpy as np
import random
import matplotlib.pyplot as plt
import math

imgOriginal = cv2.imread(sys.argv[1], 0)
k = int(sys.argv[2])

img = cv2.imread('imgs/ruido' + str(k) + '.png', 0)

if k == 0:
    # Aumentei o tamanho do kernel de 2x2 para 3x3
    imgResultante = cv2.blur(img, (3, 3)) 
if k == 1:
    imgResultante = cv2.GaussianBlur(img, (3, 3), 0)
if k == 2:
    imgResultante = cv2.medianBlur(img, 3)
if k == 3:
    imgResultante = cv2.medianBlur(img, 3)
if k == 4:
    # Busca blocos semelelhantes em outras partes da imagem em vez da vizinhança
    imgResultante = cv2.fastNlMeansDenoising(img, h=30, templateWindowSize=7, searchWindowSize=21)
    #imgResultante = cv2.GaussianBlur(img, (9, 9), 0) #PSNR = 28.9
if k == 5:
    imgResultante = cv2.medianBlur(img, 3)
    imgResultante = cv2.medianBlur(img, 3) #Aplique 2x para retirar os ruidos brancos que ficaram

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.subplot(1, 2, 2)
plt.imshow(imgResultante, cmap='gray')
plt.title('PSNR = ' + str("%.2f" % cv2.PSNR(imgResultante, imgOriginal)))
plt.show()

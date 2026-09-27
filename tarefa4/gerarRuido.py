import cv2
import sys
import numpy as np
import random
import matplotlib.pyplot as plt
import math

def gerarRuidoSalPimenta(img, pSal, pPimenta):
    img = img.copy()
    h, w = img.shape
    for i in range(h):
        for j in range(w):
            n = random.random()
            if n < pSal:
                img[i][j] = 255
            
            n = random.random()
            if n < pPimenta:
                img[i][j] = 0
    return img

def gerarRuidoUniforme(img, f):
    img = img.copy()
    h, w = img.shape
    for i in range(h):
        for j in range(w):
            n = 0.5 - random.random()
            a = int(img[i][j]) + f*n
            a = max(0, min(255, a))
            img[i][j] = a
    return img

def gerarRuidoGaussiano(img, m, sd):
    img = img.copy()
    h, w = img.shape
    for i in range(h):
        for j in range(w):
            a = int(img[i][j]) + random.normalvariate(m, sd)
            a = max(0, min(255, a))
            img[i][j] = a
    return img

def gerarRuidoRayleigh(img, m):
    img = img.copy()
    h, w = img.shape
    for i in range(h):
        for j in range(w):
            a = int(img[i][j]) + np.random.rayleigh(m)
            a = max(0, min(255, a))
            img[i][j] = a
    return img

imgOriginal = cv2.imread(sys.argv[1], 0)

imgs = []
#ruido sal e pimenta leve
imgs.append(gerarRuidoSalPimenta(imgOriginal, 0.001, 0.001))
#ruido gaussiano leve
imgs.append(gerarRuidoGaussiano(imgOriginal, 0, 8))
#ruido sal moderado
imgs.append(gerarRuidoSalPimenta(imgOriginal, 0.02, 0))
#ruido pimenta moderado
imgs.append(gerarRuidoSalPimenta(imgOriginal, 0, 0.02))
#ruido gaussiano grave
imgs.append(gerarRuidoGaussiano(imgOriginal, 0, 30))
#ruido sal e pimenta grave
imgs.append(gerarRuidoSalPimenta(imgOriginal, 0.1, 0.1))

k = int(sys.argv[2])
img = imgs[int(sys.argv[2])]
cv2.imwrite('ruido' + str(k) + '.png', img)

print(cv2.PSNR(img, imgOriginal))

plt.subplot(2, 2, 1)
plt.imshow(imgOriginal, cmap='gray')
plt.subplot(2, 2, 3)
plt.imshow(img, cmap='gray')
plt.subplot(2, 2, 2)
plt.hist(imgOriginal.flatten(), bins=255)
plt.subplot(2, 2, 4)
plt.hist(img.flatten(), bins=255)
plt.show()

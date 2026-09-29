import cv2
import sys
import numpy as np
import random
import matplotlib.pyplot as plt
import math
imgPath = sys.argv[1]
cx_real = int(sys.argv[2])
cy_real = int(sys.argv[3])
r_real = int(sys.argv[4])

img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
altura, largura = img.shape
# Aplicar o filtro
#imgSemRuido = cv2.GaussianBlur(img, (3, 3), 0)
imgSemRuido = cv2.medianBlur(img, 9)

# Identificar o circulo
x_min = largura
x_max = 0
y_min = altura
y_max = 0

for x in range(largura):
    for y in range(altura):
        if imgSemRuido[y, x] != 0:
            if x < x_min:
                x_min = x
            elif x > x_max:
                x_max = x

            if y < y_min:
                y_min = y
            elif y > y_max:
                y_max = y

raio_x = (x_max - x_min) / 2
raio_y = (y_max - y_min) / 2
centro_x = x_min + raio_x
centro_y = y_min + raio_y

print(f"Raio (x, y): ({raio_x:.2f}, {raio_y:.2f})")
print(f"Centro (x, y): ({centro_x:.2f}, {centro_y:.2f})")

contours, heirarchy = cv2.findContours(imgSemRuido, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
img_bgr = cv2.cvtColor(imgSemRuido, cv2.COLOR_GRAY2BGR)
contour_img = cv2.drawContours(img_bgr, contours, -1, (0, 255, 0), 3)
contour_img[int(centro_y)][int(centro_x)] = (0, 255, 0)
contour_img = cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB)
# Tirar as medidas

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.subplot(1, 2, 2)
plt.imshow(contour_img)
plt.show()
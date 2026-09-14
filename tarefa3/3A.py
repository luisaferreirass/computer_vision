import cv2
import numpy as np
import os
import sys


if len(sys.argv) < 4:
    print("Uso correto: python script.py <t> <lt> <ht>")
    print("Exemplo: python script.py 100 50 150")
    sys.exit(1)
t = int(sys.argv[1])   # Limiar do Sobel
lt = int(sys.argv[2])  # Low threshold do Canny
ht = int(sys.argv[3])  # High threshold do Canny
img = cv2.imread('imgs/patch02.jpg', cv2.IMREAD_GRAYSCALE)

origem = img.copy()

laplacian = cv2.Laplacian(img, cv2.CV_64F)
laplacian_norm = cv2.normalize(np.abs(laplacian), None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobelx_norm = cv2.normalize(sobelx, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobely_norm = cv2.normalize(sobely, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)

magnitude = cv2.magnitude(sobelx, sobely)
_, sobel_thresholded = cv2.threshold(magnitude, t, 255, cv2.THRESH_BINARY)
sobel_thresholded = np.uint8(sobel_thresholded)

canny = cv2.Canny(img, lt, ht)

linha_superior = cv2.hconcat([img, laplacian_norm, sobelx_norm])
linha_inferior = cv2.hconcat([sobely_norm, sobel_thresholded, canny])

grid = cv2.vconcat([linha_superior, linha_inferior])
cv2.imshow('Filtros: Original | Laplacian | SobelX | SobelY | Sobel | Canny', grid)
cv2.waitKey(0)
cv2.destroyAllWindows()
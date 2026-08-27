# TAREFA 1B: o programa deve exibir na tela as ŷ imagens de patchųŴ.jpg a patchųŷ.jpg, um do lado do outro

import cv2

# Leituras das imagens = matrizes
img1 = cv2.imread('patch01.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('patch02.jpg', cv2.IMREAD_COLOR)
img3 = cv2.imread('patch03.jpg', cv2.IMREAD_COLOR)
img4 = cv2.imread('patch04.jpg', cv2.IMREAD_COLOR)

img = cv2.hconcat([img1, img2, img3, img4])

cv2.imshow('color image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# TAREFA 2E: Exibir a imagem livro.jpg e somente a área do livro em uma nova imagem


import cv2
import numpy as np

img = cv2.imread('imgs/livro.jpg')

pts_origem = np.float32([
    [60, 117],   # superior esquerdo
    [473, 29],   # superior direito
    [163, 777],  # inferior esquerdo
    [662, 653]   # inferior direito
])

largura = 380
altura = 535

pts_destino = np.float32([
    [0, 0],
    [largura, 0],
    [0, altura],
    [largura, altura]
])

matriz = cv2.getPerspectiveTransform(pts_origem, pts_destino)
livro_recortado = cv2.warpPerspective(img, matriz, (largura, altura))

cv2.imshow('Imagem Original (livro.jpg)', img)
cv2.imshow('Gabarito 2E - Livro Retificado', livro_recortado)
cv2.waitKey(0)
cv2.destroyAllWindows()
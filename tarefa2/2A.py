# TAREFA 2A: exibir foto06.jpg e o resultado da limiarizacao dessa imagem.
# O limiar deve ser parametro do programa. Nao usar funcao pronta de limiarizacao
# nem operacoes matriciais: percorrer a imagem pixel a pixel (operador pontual).

import cv2
import numpy as np
import sys

limiar = int(sys.argv[1]) if len(sys.argv) > 1 else 128

img = cv2.imread('imgs/foto06.jpg', cv2.IMREAD_GRAYSCALE)

saida = np.zeros_like(img)

altura, largura = img.shape
for i in range(altura):
    for j in range(largura):
        if img[i, j] >= limiar:
            saida[i, j] = 255

resultado = cv2.hconcat([img, saida])

titulo = 'Tarefa2a - original | limiarizada (limiar=%d)' % limiar
cv2.namedWindow(titulo, cv2.WINDOW_NORMAL)   # janela redimensionavel
cv2.resizeWindow(titulo, 1200, 600)
cv2.imshow(titulo, resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()

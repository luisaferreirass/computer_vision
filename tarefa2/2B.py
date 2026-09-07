# TAREFA 2B: exibir foto06.jpg, o resultado da transformacao logaritmica (clarear,
# para melhorar contraste da estatua a frente) e a logaritmica inversa (escurecer,
# para melhorar contraste da estatua ao fundo). Pode usar operacao matricial.

import cv2
import numpy as np

img = cv2.imread('imgs/foto06.jpg', cv2.IMREAD_GRAYSCALE)

img_f = img.astype(np.float64)

c = 255 / np.log(1 + 255)

log_f = c * np.log(1 + img_f)
log_img = np.clip(log_f, 0, 255).astype(np.uint8)

inv_f = np.exp(img_f / c) - 1
inv_img = np.clip(inv_f, 0, 255).astype(np.uint8)

resultado = cv2.hconcat([img, log_img, inv_img])

titulo = 'Tarefa2b - original | log | log inversa'
cv2.namedWindow(titulo, cv2.WINDOW_NORMAL)   # Janela redimensionavel
cv2.resizeWindow(titulo, 1200, 500)
cv2.imshow(titulo, resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()

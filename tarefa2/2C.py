# TAREFA 2C: exibir a imagem original e o resultado da equalizacao do histograma
# (pode utilizar cv2.equalizeHist).

import cv2

img = cv2.imread('imgs/foto06.jpg', cv2.IMREAD_GRAYSCALE)

equalizada = cv2.equalizeHist(img)

resultado = cv2.hconcat([img, equalizada])

titulo = 'Tarefa2c - original | equalizada'
cv2.namedWindow(titulo, cv2.WINDOW_NORMAL)
cv2.resizeWindow(titulo, 1200, 600) # Janela redimensionavel
cv2.imshow(titulo, resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()

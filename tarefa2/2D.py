#TAREFA 2D:  exibir a reconstrução da imagem foto06.jpg a partir dos pedaços a.jpg 
# (possui 10% do tamanho original), b.jpg (está rotacionada 90 graus), c.jpg e d.jpg

import cv2
import numpy as np

a = cv2.imread('imgs/a.jpg')
b = cv2.imread('imgs/b.jpg')
c = cv2.imread('imgs/c.jpg')
d = cv2.imread('imgs/d.jpg')


a_restaurada = cv2.resize(a, (0, 0), fx=10.0, fy=10.0, interpolation=cv2.INTER_CUBIC)
h, w = a_restaurada.shape[:2]

b_girada= cv2.rotate(b, cv2.ROTATE_90_COUNTERCLOCKWISE)
b_restaurada = cv2.resize(b_girada, (w, h))


altura, largura = c.shape[:2]
metade_largura = largura // 2
c_restaurada = c[:, 0:metade_largura]
d_restaurada = d[:, metade_largura:largura]

# Criar o canvas final inicializado em preto
largura_total = w * 2
altura_total = h * 2
canvas = np.zeros((altura_total, largura_total, 3), dtype=np.uint8)

# 5. Posicionar as partes via warpAffine (Translação simples)

# Quadrante A: Superior Esquerdo (0, 0)
M_a = np.float32([[1, 0, 0], [0, 1, 0]])
canvas = cv2.warpAffine(a_restaurada, M_a, (largura_total, altura_total), dst=canvas, borderMode=cv2.BORDER_TRANSPARENT)

# Quadrante B: Superior Direito (w, 0)
M_b = np.float32([[1, 0, w], [0, 1, 0]])
canvas = cv2.warpAffine(b_restaurada, M_b, (largura_total, altura_total), dst=canvas, borderMode=cv2.BORDER_TRANSPARENT)

# Quadrante D: Inferior Esquerdo (0, h)
M_d = np.float32([[1, 0, 0], [0, 1, h]])
canvas = cv2.warpAffine(d_restaurada, M_d, (largura_total, altura_total), dst=canvas, borderMode=cv2.BORDER_TRANSPARENT)

# Quadrante C: Inferior Direito (w, h)
M_c = np.float32([[1, 0, w], [0, 1, h]])
canvas = cv2.warpAffine(c_restaurada, M_c, (largura_total, altura_total), dst=canvas, borderMode=cv2.BORDER_TRANSPARENT)

# 6. Exibir resultado final corrigido
cv2.imshow('Reconstrucao via warpAffine Corrigida (Tarefa 2D)', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
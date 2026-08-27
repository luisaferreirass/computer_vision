# TAREFA 1A: o programa deve exibir as 6 imagens (em 2 linhas e 3 colunas) de tamanho 280x200:
# cinza (127), branca (255), listras verticais (30), listras horizontais (30), xadrez (30), aleatoria

import cv2
import numpy as np

LINHAS = 200
COLUNAS = 280
TAM_BLOCO = 30

img_cinza = np.full((LINHAS, COLUNAS), 127, dtype=np.uint8)

img_branca = np.full((LINHAS, COLUNAS), 255, dtype=np.uint8)

img_listras_verticais = np.zeros((LINHAS, COLUNAS), dtype=np.uint8)
for col in range(0, COLUNAS, TAM_BLOCO):
    if (col // TAM_BLOCO) % 2 == 0:
        cv2.rectangle(img_listras_verticais, (col, 0), (col + TAM_BLOCO, LINHAS), 255, -1)

img_listras_horizontais = np.zeros((LINHAS, COLUNAS), dtype=np.uint8)
for lin in range(0, LINHAS, TAM_BLOCO):
    if (lin // TAM_BLOCO) % 2 == 0:
        cv2.rectangle(img_listras_horizontais, (0, lin), (COLUNAS, lin + TAM_BLOCO), 255, -1)

img_xadrez = np.zeros((LINHAS, COLUNAS), dtype=np.uint8)
for lin in range(0, LINHAS, TAM_BLOCO):
    for col in range(0, COLUNAS, TAM_BLOCO):
        if ((lin // TAM_BLOCO) + (col // TAM_BLOCO)) % 2 == 0:
            cv2.rectangle(img_xadrez, (col, lin), (col + TAM_BLOCO, lin + TAM_BLOCO), 255, -1)

img_aleatoria = np.random.randint(0, 256, (LINHAS, COLUNAS), dtype=np.uint8)

linha1 = cv2.hconcat([img_cinza, img_branca, img_listras_verticais])
linha2 = cv2.hconcat([img_listras_horizontais, img_xadrez, img_aleatoria])
img = cv2.vconcat([linha1, linha2])

cv2.imshow('Tarefa1a', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

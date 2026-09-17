import cv2
import numpy as np
import sys


if len(sys.argv) < 3:
    print("Uso correto: python 3B.py <imagem> <t>")
    print("Exemplo: python 3B.py imgs/chessboard48.png 100")
    sys.exit(1)

caminho_imagem = sys.argv[1]
t = int(sys.argv[2])  # Limiar da magnitude do gradiente

img = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)
if img is None:
    print(f"Erro ao carregar a imagem: {caminho_imagem}")
    sys.exit(1)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3) # Calcula a intensidade da variação das cores
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

magnitude = cv2.magnitude(sobelx, sobely)
mask = magnitude > t # Filtra quem é borda e quem não é

gx = sobelx[mask] # só os valores de sobelx nos pixels de borda
gy = -sobely[mask]  # inverte o eixo y (imagem cresce p/ baixo) para o sistema cartesiano

if gx.size == 0:
    print("Nenhum pixel de borda encontrado com o limiar informado.")
    sys.exit(1)

angulos = np.arctan2(gy, gx)

# O tabuleiro possui bordas em duas direções perpendiculares, e o gradiente
# de cada borda tem ambiguidade de 180 graus (pode apontar para qualquer um
# dos lados).
angulos4 = 4 * angulos

# Média circular
seno_medio = np.mean(np.sin(angulos4))
cosseno_medio = np.mean(np.cos(angulos4))
angulo_medio4 = np.arctan2(seno_medio, cosseno_medio)

angulo = (angulo_medio4 / 4) % (np.pi / 2) # Retira a multiplicação por 4 e deixa no intervalo que o prof pediu

print(f"Rotacao do tabuleiro: {angulo:.4f} rad ({np.degrees(angulo):.2f} graus)")

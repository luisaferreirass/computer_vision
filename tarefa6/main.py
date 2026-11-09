import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(sys.argv[1])
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Máscara binária de cada cor (onde tiver disco é branco)
mask_red1 = cv2.inRange(img_hsv, np.array([0, 80, 60]), np.array([10, 255, 255]))
mask_red2 = cv2.inRange(img_hsv, np.array([170, 80, 60]), np.array([179, 255, 255]))
mask_red = cv2.bitwise_or(mask_red1, mask_red2)
mask_yellow = cv2.inRange(img_hsv, np.array([20, 70, 70]), np.array([38, 255, 255]))
mask_green = cv2.inRange(img_hsv, np.array([39, 70, 50]), np.array([90, 255, 255]))
mask_blue = cv2.inRange(img_hsv, np.array([85, 70, 60]), np.array([105, 255, 255]))

# Função que detecta circulos usando a transformada de Hough
def find_circles(mask):
    img_blur = cv2.GaussianBlur(
        mask,
        (9, 9),
        2
    )

    circles = cv2.HoughCircles(
        img_blur,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=20,
        param1=100,
        param2=15,
        minRadius=17,
        maxRadius=34
    )

    if circles is not None:
        circles = np.uint16(
            np.around(circles)
        )

        return circles[0]

    return []


# Detecção dos circulos das mascaras
circles_red = find_circles(mask_red)
circles_yellow = find_circles(mask_yellow)
circles_green = find_circles(mask_green)
circles_blue = find_circles(mask_blue)

# Função que agrupa circulos
# Circulos com centros próximo, são circulo externo e interno do mesmo disco
def cluster_circles(circles):

    return

# Agrupar ciclos detenctados nas mascaras
discos_red = cluster_circles(circulos_red)
discos_yellow = cluster_circles(circulos_yellow)
discos_green = cluster_circles(circulos_green)
discos_blue = cluster_circles(circulos_blue)

# Contar quantidade de discos de cada cor
count = {
    "Red": len(discos_red),
    "Yellow": len(discos_yellow),
    "Green": len(discos_green),
    "Blue": len(discos_blue)
}

# Exibir quandidade de discos
print("\nContagem de discos:")

for color, qtd in count.items():
    print(f"{color}: {qtd}")


# Identificar circulos na imagem

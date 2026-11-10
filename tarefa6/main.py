import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(sys.argv[1])
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
nome = sys.argv[1].replace("\\", "/").split("/")[-1].split(".")[0]
num_img = int(nome) if nome.isdigit() else 0

# Máscara binária de cada cor (onde tiver disco é branco)
mask_red1 = cv2.inRange(img_hsv, np.array([0, 80, 60]), np.array([10, 255, 255]))
mask_red2 = cv2.inRange(img_hsv, np.array([170, 80, 60]), np.array([179, 255, 255]))
mask_red = cv2.bitwise_or(mask_red1, mask_red2)
mask_yellow = cv2.inRange(img_hsv, np.array([20, 70, 70]), np.array([38, 255, 255]))
mask_green = cv2.inRange(img_hsv, np.array([39, 70, 50]), np.array([84, 255, 255]))
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
        maxRadius=45
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
    # Ordena do maior para o menor raio, assim o primeiro de cada grupo é o externo
    # int() para não estourar o uint16 ao subtrair coordenadas
    circles = sorted([(int(x), int(y), int(r)) for x, y, r in circles], key=lambda c: c[2], reverse=True)

    discos = []
    for x, y, r in circles:
        mesmo_disco = False
        for dx, dy, dr in discos:
            # Centro a menos de 1.4 * raio de um disco já aceito = mesmo disco
            if np.hypot(x - dx, y - dy) < 1.4 * dr:
                mesmo_disco = True
                break
        if not mesmo_disco:
            discos.append((x, y, r))

    return discos

# Agrupar ciclos detenctados nas mascaras
discos_red = cluster_circles(circles_red)
discos_yellow = cluster_circles(circles_yellow)
discos_green = cluster_circles(circles_green)
discos_blue = cluster_circles(circles_blue)

# Função que confere se o disco é real: pelo menos metade do anel
# (entre o círculo interno, 0.55 * r, e o externo) tem que ser da cor na máscara
# Elimina falsos positivos como sombra esverdeada dentro do furo de um disco amarelo
def disco_valido(mask, x, y, r, limiar=0.5):
    anel = np.zeros_like(mask)
    cv2.circle(anel, (x, y), r, 255, -1)
    cv2.circle(anel, (x, y), int(0.55 * r), 0, -1)
    return (mask[anel > 0] > 0).mean() >= limiar

# Às vezes o Hough só acha o círculo interno (raio bem menor que a mediana)
# Nesse caso converte para o externo (r / 0.55), para desenhar sempre o externo
r_med = np.median([r for x, y, r in discos_red + discos_yellow + discos_green + discos_blue])

def raio_externo(discos):
    return [(x, y, int(round(r / 0.55)) if r < 0.7 * r_med else r) for x, y, r in discos]

discos_red = [d for d in raio_externo(discos_red) if disco_valido(mask_red, *d)]
discos_yellow = [d for d in raio_externo(discos_yellow) if disco_valido(mask_yellow, *d)]
discos_green = [d for d in raio_externo(discos_green) if disco_valido(mask_green, *d)]
discos_blue = [d for d in raio_externo(discos_blue) if disco_valido(mask_blue, *d)]


# Imagens 6-8: discos maiores (raio > maxRadius) e muito sobrepostos
# Hough implementada do zero usando o fato de todo disco ter um círculo
# interno e um externo com razão de raios constante (0.55)

# Função que monta o acumulador (raio, y, x)
# Cada ponto de borda vota no centro andando ao longo do gradiente:
# - borda externa: o gradiente aponta para dentro do anel, centro a R na direção do gradiente
# - borda interna (furo): o gradiente aponta para fora do furo, centro a 0.55 * R no sentido oposto
# Um disco de verdade recebe votos das duas bordas no mesmo ponto
def hough_anel(mask, raios):
    img_blur = cv2.GaussianBlur(mask, (7, 7), 2).astype(np.float32)
    gx = cv2.Sobel(img_blur, cv2.CV_32F, 1, 0, ksize=3)
    gy = cv2.Sobel(img_blur, cv2.CV_32F, 0, 1, ksize=3)

    # Pontos de borda e direção do gradiente (vetor unitário) em cada um
    ys, xs = np.nonzero(cv2.Canny(mask, 50, 150))
    mag = np.hypot(gx[ys, xs], gy[ys, xs]) + 1e-6
    ux = gx[ys, xs] / mag
    uy = gy[ys, xs] / mag

    h, w = mask.shape
    acc = np.zeros((len(raios), h, w), np.float32)
    for i, R in enumerate(raios):
        for sentido, r in [(1, R), (-1, 0.55 * R)]:
            cx = np.round(xs + sentido * ux * r).astype(int)
            cy = np.round(ys + sentido * uy * r).astype(int)
            dentro = (cx >= 0) & (cx < w) & (cy >= 0) & (cy < h)
            np.add.at(acc[i], (cy[dentro], cx[dentro]), 1)
        # Suaviza e divide pelo perímetro (externo + interno),
        # assim o score é a fração do anel que foi encontrada
        acc[i] = cv2.GaussianBlur(acc[i], (0, 0), 2) / (2 * np.pi * (R + 0.55 * R))

    return acc

# Função que pega os picos do acumulador, do maior para o menor, apagando a
# vizinhança de cada um (supressão de não-máximos). Cada pico = 1 disco
def picos_acumulador(acc, raios, limiar, dist_min=0.7):
    melhor = acc.max(axis=0)
    idx_raio = acc.argmax(axis=0)

    discos = []
    while True:
        y, x = np.unravel_index(melhor.argmax(), melhor.shape)
        if melhor[y, x] < limiar:
            break
        R = int(raios[idx_raio[y, x]])
        discos.append((int(x), int(y), R))
        cv2.circle(melhor, (int(x), int(y)), int(dist_min * R), 0, -1)

    return discos

# Função que detecta os discos de uma cor e valida se a máscara tem anel ali
# Limiar 0.19 é baixo de propósito para não perder discos que estão bem cobertos
# por outros, mas descarta picos gerados por borda de outra cor vazando na máscara
def detectar_discos_anel(mask, raios):
    picos = picos_acumulador(hough_anel(mask, raios), raios, 0.0022)
    return [(x, y, R) for x, y, R in picos if disco_valido(mask, x, y, R, 0.19)]

if num_img >= 6:
    # Estima o raio dos discos na foto (todos têm o mesmo tamanho)
    # usando só as detecções mais fortes, numa faixa larga de raios
    raios_largos = list(range(40, 84, 2))
    raios_fortes = []
    for mask in [mask_red, mask_yellow, mask_green, mask_blue]:
        picos = picos_acumulador(hough_anel(mask, raios_largos), raios_largos, 0.0045, 0.5)
        raios_fortes += [r for x, y, r in picos]
    R_med = np.median(raios_fortes)

    # Detecção final só em R_med +- 10%, o que corta falsos positivos
    raios = list(range(int(0.9 * R_med), int(1.1 * R_med) + 1))
    discos_red = detectar_discos_anel(mask_red, raios)
    discos_yellow = detectar_discos_anel(mask_yellow, raios)
    discos_green = detectar_discos_anel(mask_green, raios)
    discos_blue = detectar_discos_anel(mask_blue, raios)

# Contar quantidade de discos de cada cor
count = {
    "Red": len(discos_red),
    "Yellow": len(discos_yellow),
    "Green": len(discos_green),
    "Blue": len(discos_blue)
}

# Gabarito de cada imagem (docs/gabarito.txt)
gabarito = {
    1: {"Red": 9, "Yellow": 9, "Green": 13, "Blue": 11},
    2: {"Red": 11, "Yellow": 10, "Green": 15, "Blue": 12},
    3: {"Red": 5, "Yellow": 6, "Green": 10, "Blue": 7},
    4: {"Red": 5, "Yellow": 6, "Green": 7, "Blue": 7},
    5: {"Red": 7, "Yellow": 7, "Green": 12, "Blue": 11},
    6: {"Red": 8, "Yellow": 10, "Green": 11, "Blue": 11},
    7: {"Red": 11, "Yellow": 11, "Green": 15, "Blue": 12},
    8: {"Red": 11, "Yellow": 11, "Green": 14, "Blue": 12}
}
total = gabarito.get(num_img, {})

# Exibir quandidade de discos (encontrados/total)
print("\nContagem de discos:")

for color, qtd in count.items():
    print(f"{color}: {qtd}/{total.get(color, '?')}")


# Identificar circulos na imagem
# Cor do círculo em tom mais escuro que o disco (BGR), para distinguir círculo e disco
img_result = img.copy()

for discos, cor in [(discos_red, (0, 0, 140)), (discos_yellow, (0, 140, 160)),
                    (discos_green, (0, 100, 0)), (discos_blue, (150, 70, 0))]:
    for x, y, r in discos:
        # Círculo externo com borda fina
        cv2.circle(img_result, (x, y), r, cor, 2)
        # Ponto no centro do disco
        cv2.circle(img_result, (x, y), 3, (0, 0, 0), -1)


# Escrever imagem final
cv2.imwrite("resultados/" + nome + "_resultado.jpg", img_result)

plt.imshow(cv2.cvtColor(img_result, cv2.COLOR_BGR2RGB))
plt.title("  ".join(f"{color}: {qtd}/{total.get(color, '?')}" for color, qtd in count.items()))
plt.axis("off")
plt.show()

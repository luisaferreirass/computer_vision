# Visão Computacional

Atividades práticas da disciplina de **Visão Computacional** (UFRN), implementadas em Python com OpenCV, NumPy e Matplotlib. O repositório cobre desde a geração e manipulação básica de imagens até filtragem de ruído, detecção de bordas e detecção de círculos com a Transformada de Hough (incluindo uma implementação própria).

## Estrutura

```
computer_vision/
├── tarefa1/                 # Geração e exibição de imagens, webcam + Canny
├── tarefa2/                 # Operadores pontuais e transformações geométricas
├── tarefa3/                 # Detecção de bordas e rotação de tabuleiro
├── tarefa4/                 # Atenuação de ruído (enunciado: "Tarefa 5")
├── tarefa6/                 # Contagem de discos coloridos com Hough
└── remocao_ruido_circulo/   # Estimativa de centro e raio de círculos com ruído
```

Cada pasta traz os scripts, as imagens de teste (`imgs/`) e, quando disponível, o enunciado em `docs/`.

## Tarefas

### Tarefa 1 — Fundamentos
- **1A:** gera e exibe em grade 6 imagens 280x200 (cinza, branca, listras verticais/horizontais, xadrez e ruído aleatório).
- **1B:** concatena lado a lado vários patches de imagem.
- **1C:** captura da webcam com o filtro de Canny aplicado, recebendo os dois limiares por linha de comando.

### Tarefa 2 — Operadores pontuais e geometria
- **2A:** limiarização implementada percorrendo pixel a pixel (sem função pronta nem operação matricial).
- **2B:** transformações logarítmica e logarítmica inversa para realce de contraste.
- **2C:** equalização de histograma.
- **2D:** reconstrução de uma imagem a partir de pedaços redimensionados e rotacionados (`resize`, `rotate`, `warpAffine`).
- **2E:** correção de perspectiva para extrair a capa de um livro (`getPerspectiveTransform`, `warpPerspective`).

### Tarefa 3 — Bordas e gradiente
- **3A:** Laplaciano, Sobel em x e y, magnitude do gradiente limiarizada e Canny com histerese.
- **3B:** estima o ângulo de rotação de um tabuleiro de xadrez em [0, π/2) a partir da direção do gradiente (Sobel + `arctan2`).

### Tarefa 4 / 5 — Atenuação de ruído
- `gerarRuido.py` gera 6 versões ruidosas de uma imagem (sal e pimenta, gaussiano, sal, pimenta, em diferentes intensidades).
- `atenuarRuido.py` aplica o melhor filtro encontrado para cada tipo de ruído e exibe o PSNR (`cv2.PSNR`) em relação à imagem original.

### Tarefa 6 — Contagem de discos coloridos
Conta os discos vermelhos, amarelos, verdes e azuis em 8 imagens e compara com o gabarito.
- Segmentação por cor no espaço **HSV** (uma máscara por cor).
- Imagens 1–5: `cv2.HoughCircles` + agrupamento de círculos interno/externo do mesmo disco + validação do anel na máscara para eliminar falsos positivos.
- Imagens 6–8 (muitas sobreposições): **Transformada de Hough implementada do zero**, explorando o fato de cada disco ter um círculo interno e outro externo com razão de raios constante (≈ 0,55). Cada ponto de borda vota no centro ao longo da direção do gradiente, seguido de supressão de não-máximos.
- Saída: contagem por cor no terminal/título e imagem com os círculos desenhados, salva em `resultados/`.

### Remoção de ruído e detecção de círculo
Imagens sintéticas de um círculo com diferentes ruídos (sem ruído, sal, pimenta, sal e pimenta, gaussiano) e `ground_truth.csv` com os valores reais. Os scripts filtram a imagem (gaussiano/mediana), estimam centro e raio do círculo e desenham o contorno encontrado.

## Como executar

Requisitos: Python 3 e as bibliotecas abaixo.

```bash
pip install opencv-python numpy matplotlib
```

Os scripts são executados de dentro da pasta de cada tarefa, por exemplo:

```bash
cd tarefa1 && python 1C.py 100 200                 # limiares do Canny
cd tarefa4 && python atenuarRuido.py cristo.jpg 3  # imagem de referência e índice do ruído (0–5)
cd tarefa6 && python main.py imgs/7.jpg            # imagem a ser analisada
cd remocao_ruido_circulo && python ruido_gaussiano.py C_gaussiano_r060.png <cx> <cy> <r>
```

## Stack

Python · OpenCV · NumPy · Matplotlib

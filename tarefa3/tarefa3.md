---
title: "Tarefa 3"
author: "Rafael Beserra Gomes"
institute: "UFRN"
fonttheme: "professionalfonts"
fontsize: 9pt
urlcolor: blue
linkstyle: bold
md_extensions: +fenced_divs
aspectratio: 169
output:
	beamer_presentation:
		keep_tex: true
header-includes:
	- \usepackage{amsfonts,amsmath,oldgerm,tikz}
	- \usetikzlibrary{calc,decorations.pathmorphing,patterns}
	- \usetikzlibrary{arrows,shapes}
	- \usetheme{ufrn}
	- \pgfdeclarelayer{background}
	- \pgfsetlayers{background,main}
---

# Tarefa 3

## Especificação da tarefa

- Pontuação: 1.2pts
- Em grupo de até 3 alunos
- Prazo: 14/09 23h59
- Apresentação: até dia 15/09

---

### Tarefa 3A

Dada uma imagem e três inteiro (**t**, **lt** low-threshold, **ht** high-threshold), o programa deve exibir na tela:

a) a imagem original
b) o resultado da laplaciana
c) o resultado do filtro de sobel em x (normalizado)
d) o resultado do filtro de sobel em y (normalizado)
e) o resultado do filtro de sobel (limiarização em **t** da magnitude do gradiente)
f) o resultado do filtro de Canny (limiares **lt** e **ht** da histerese com duplo limiar)

**observação:** pode utilizar as funções prontas Laplacian, Sobel e Canny

![Exemplo de resultado](filtros.jpg){width=30%}

---

### Tarefa 3B

dada uma imagem e um inteiro **t**, o programa deve informar a rotação do tabuleiro de xadrez como um ângulo no intervalo $[0, \frac{\pi}{2}[$. O parâmetro **t** deve ser utilizado como limiar para o algoritmo.

**observação:** pode utilizar a função pronta Sobel. Dica: utilize arctan2 de numpy ou atan2 de math para calcular o ângulo em função dos componentes do vetor, atentando-se para o sistema de coordenadas da imagem (onde é calculado o gradiente) e o sistema de coordenadas cartesiano (onde é calculado o arco tangente). A pasta contém vários arquivos chessboardxx.png para testes, onde xx é o ângulo do tabuleiro. Caso queira, você também pode criar mais testes modificando o script gerarImagensXadrez.sh para gerar novas imagens.

![Exemplo de imagem cujo ângulo é 48 graus](chessboard48.png){width=20%}
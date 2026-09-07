---
title: "Tarefa 2"
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
	- \newcommand{\graphlabel}[1]{\node[overlay,anchor=north east,font=\tiny\ttfamily,black!60] at (current bounding box.south east) {#1};}
	- \usepackage{grafos}
---

# Tarefa 2

## Especificação da tarefa

- Pontuação: 1.0pts
- Em grupo de até 3 alunos
- Prazo: 07/09 23h59
- Apresentação: até dia 08/09

---

### Tarefa 2A

- o programa deve exibir a imagem foto06.jpg e o resultado da limiarização dessa imagem
- o programa deve ter como parâmetro o limiar
- **não** deve usar função pronta para limiarização, **nem** operações matriciais (ou seja, deve percorrer a imagem para realizar o operador pontual da limiarização)

\centering	
![Exemplo de resultado](limiarGabarito.jpg){width=60%}

---

### Tarefa 2B

- o programa deve exibir a imagem foto06.jpg, o resultado da transformação logarítmica (clarear, para melhorar contraste da estátua à frente) e logarítmica inversa (escurecer, para melhorar contraste da estátua ao fundo). Pode usar operação matricial se disponível na linguagem.

\centering
![](logGabarito.jpg){width=60%}

---

### Tarefa 2C

- o programa deve exibir a imagem original e o resultado da equalização do histograma (pode, caso queira, utilizar cv2.equalizeHist)

---

### Tarefa 2D

- o programa deve exibir a reconstrução da imagem foto06.jpg a partir dos pedaços a.jpg (possui 10% do tamanho original), b.jpg (está rotacionada 90 graus), c.jpg e d.jpg
- utilize as funções do opencv, como resize, rotate e warpAffine para fazer a reconstrução

---

### Tarefa 2E

- o programa deve exibir a imagem livro.jpg e somente a área do livro em uma nova imagem
- deve utilizar getPerspectiveTransform e warpPerspective para esta tarefa
    - use um software de edição de imagens para obter as coordenadas dos 4 cantos do livro na imagem original

\centering
![](livroGabarito.jpg){width=40%}
---
title: "Tarefa 6"
author: "Visão computacional"
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

# Tarefa 6

## Especificação da tarefa

- Pontuação: 2.2 pts (0.2 pts/imagem 1-5 + 0.4 pts/imagem 6-8)
- Em grupo de até 3 alunos

---



Nesta tarefa você deverá contar o número de discos vermelhos, amarelos, verdes e azuis nas imagens numeradas de 1.jpg a 8.jpg. Note que cada disco tem um círculo interno e externo.

### Tarefa 6 - apresentação dos resultados

- Coloque na saída do terminal ou em texto na tela: para cada cor, o número de círculos encontrados / total de círculos daquela cor de acordo com o gabarito. Por exemplo:

    - Vermelho: 18/20
    - Amarelo: 23/20
    - Verde: 13/13
    - Azul: 8/12

- O programa deve exibir a imagem original na qual **deve** se sobrepor o desenho do círculo interno/externo relativo a cada disco com a mesma cor do círculo detectado e um ponto (de qualquer cor) para representar o centro do disco.
    - Use como cor do círculo a mesma cor do disco (vermelho, amarelo, verde, azul) mas em uma tonalidade que permita distinguir o que é círculo e o que é disco
    - A borda não pode ser grossa a ponto de atrapalhar muito a visualização do disco
    - Vocẽ pode escolher entre desenhar o círculo interno ou externo, mas deve ser consistente e adotar a mesma escolha para todos os discos
	- O resultado de cada imagem deve aparecer em uma única imagem e não em imagens separadas por cor (exemplo, uma imagem para os círculos vermelhos, outra para o amarelo, etc)


---

### Tarefa 6 - outras observações gerais

- As imagens de 1.jpg a 5.jpg são mais fáceis; as imagens de 6.jpg a 8.jpg são mais difíceis pois contém muitas sobreposições, mas tente o melhor possível!
- Pode utilizar quaisquer funções prontas do opencv ou numpy, caso ajudem na tarefa
- Para as imagens mais desafiantes, você pode implementar do zero caso queira aproveitar o fato que todos os discos contém um círculo interno e externo, com a razão entre os raios constante. Lembre-se também de que você pode separar em 4 detecções distintas, para que os os pontos pertencentes a um círculo de uma cor não interfira na detecção dos círculos de outras cores

---

### Tarefa 6 - avaliação

- Não há um gabarito em relação ao centro e raio do círculo, a avaliação será através de uma inspeção visual e para o resultado de cada imagem será atribuído um multiplicador conforme a seguir:
	- 0 pts: insuficiente
	- 0.25 pts: ruim
	- 0.5 pts: razoável
	- 0.75 pts: bom
	- 1 pt: excelente
- Será levada em conta a complexidade da imagem (espera-se mais acertos nas imagens mais fáceis)
- A existência de falsos positivos e detecções duplicadas também serão verificadas na avaliação
- Você deve ser capaz de explicar todos os passos para obtenção do resultado

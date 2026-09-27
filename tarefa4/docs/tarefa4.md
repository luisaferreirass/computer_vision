---
title: "Tarefa 4"
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

# Tarefa 4

## Especificação da tarefa

- Pontuação: 1.2pts
- Em grupo de até 3 alunos
- Prazo: 23/09 23h59
- Apresentação: até dia 24/09

---

### Tarefa 4

Na pasta há 6 arquivos de imagens com ruído (vide subseção abaixo sobre cada uma), além de uma imagem (cristo.jpg) que foi utilizada para gerá-las. O objetivo desta tarefa é atenuar o ruído de forma a obter um resultado visual satisfatório (o aumento do PSNR é um bom sinal). Fique livre para escolher o filtro e parâmetros que produzam os melhores resultados (pode se limitar aos que constam nos slides).

Dado o nome do arquivo de imagem de referência (o que servirá para calcular o PSNR) e um inteiro k (entre 0 e 5), o programa deve exibir na tela a imagem ruidok.png e a imagem com o ruído atenuado pelo melhor filtro que tenha encontrado com o PSNR na legenda (pode utilizar cv2.PSNR).
	
### Observações

- pode fazer testes com outras imagens, mas o professor utilizará a imagem cristo.jpg para avaliar a resolução.
- pode utilizar quaisquer funções prontas do opencv ou numpy, caso ajudem na tarefa. O programa deve estar programado para exibir somente uma das 6 imagens para facilitar a visualização.

---

### gerarRuido.py

arquivo que gera as imagens com ruído; não precisa alterar esse arquivo, a não ser que queira fazer mais testes; os argumentos de linha de comando são: (1) o nome do arquivo de imagem e (2) um inteiro entre 0 e 5 para gerar cada um dos 6 ruídos propostos.

## Caracterização das imagens com ruído

- ruido0.png: ruído sal e pimenta leve (32.52 dB)
- ruido1.png: ruído gaussiano leve (30.05 dB)
- ruido2.png: ruído sal moderado (22.16 dB)
- ruido3.png: ruído pimenta moderado (22.53 dB)
- ruido4.png: ruído gaussiano grave (18.78 dB)
- ruido5.png: ruído sal e pimenta grave (12.56 dB)

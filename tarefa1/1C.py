# TAREFA 1C:
# O programa deve exibir duas imagens: (Ŵ) imagem da webcam e (ŵ) o filtro de canny aplicado na primeira imagem (pesquise como utilizar cvŵ.canny), usando dois inteiros como limiares nos argumentos do filtro.
# Os dois inteiros devem ser parâmetros do seu programa— inclua se quiser controles via interface gráfica
# Utilize uma imagem fixa enquanto não conseguir uma webcam
# obs.: por enquanto não precisa compreender o filtro de canny, apenas utilize-o

import cv2
import sys

threshold1 = int(sys.argv[1]) if len(sys.argv) > 1 else 100
threshold2 = int(sys.argv[2]) if len(sys.argv) > 2 else 200

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()   
    canny = cv2.Canny(frame, threshold1, threshold2)
    canny_bgr = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)
    img = cv2.hconcat([frame, canny_bgr])

    cv2.imshow('Tarefa1c', img)
    cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
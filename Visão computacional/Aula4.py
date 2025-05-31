import cv2
import numpy as np

# Definir o caminho do vídeo (troque por 0 para usar a webcam)
video_path = "livro.mp4"
cap = cv2.VideoCapture(0)  # cv2.VideoCapture(0) para webcam

# Definir os intervalos de cor HSV para azul
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([140, 255, 255])

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # Se não conseguiu ler um quadro, encerra o loop

    # Redimensionar o frame para 500x500
    frame = cv2.resize(frame, (500, 500))

    # Converter para HSV
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Criar uma máscara para capturar tons de azul
    mask_blue = cv2.inRange(img_hsv, lower_blue, upper_blue)

    # Encontrar os contornos da máscara
    contornos, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Verificar se algum contorno foi encontrado
    if len(contornos) > 0:
        # Texto a ser exibido
        text = "Objeto Azul Detectado!"

        # Desenhar os contornos no quadro original
        cv2.drawContours(frame, contornos, -1, (0, 255, 0), 3)  # Contornos em verde com espessura 3
    else:
        text = "Nenhum Objeto Azul Detectado"

    # Colocar o texto no frame original
    cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Colocar o texto na máscara azul (cor branca para imagem binária)
    cv2.putText(mask_blue, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255), 2, cv2.LINE_AA)
    cv2.bitwise_and(frame, frame, mask=mask_blue)

    # Exibir os quadros originais e a máscara
    cv2.imshow("Video Original", frame)
    cv2.imshow("HSV", img_hsv)
    cv2.imshow("Mascara Azul", mask_blue)

    # Pressione 'q' para sair
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

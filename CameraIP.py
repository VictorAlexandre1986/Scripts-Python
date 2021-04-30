
#É preciso instalar o app "ip webcam" no smartphone
#É preciso instalar a biblioteca open cv : pip install opencv

import cv2

#Função para evitas paradas por erros
def nothing(x):
    pass

#Execução da camera, colocar o ip do servidor exibido no smartphone
cap = cv2.VideoCapture('http://192.168.15.2:8080/video')

while(True):

    #Leitura do frame
    ret, frame = cap.read()

    #Print dimensão da imagem capturada
    print(f'Dimensão original: {frame.shape}')

    #Rediomensionar o frame capturado
    scale_percent = 80 #%60 do tamanho original
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width,height)

    frameResized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)

    #Exibir o frame
    cv2.imshow('frameResized',frameResized)

    #waitkey
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break


#Finalização
cap.release()
cv2.destroyAllWindows()


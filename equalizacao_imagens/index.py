import cv2
import numpy as np

#Realize a equalização das imagens abaixo de forma a obter 
# o melhor resultado. Lembrando que a equalização produz uma imagem 
# cujos brilhos são mais distribuídos, reduzindo as regiões 
# muito escuras ou muito claras. Utilize o espaço de cor mais 
# adequado para cada imagem. 
# Considere os seguintes espaços de cores:
# RGB, HSV, HSL, YCrCb e Lab.

image_paths = [
    './src/images/family.jpg',
    './src/images/lenna.jpg',
    './src/images/mindland.png'
]

W_NAME_ORI  = 'Original'
W_NAME_GRAY = 'Niveis de Cinza'
W_NAME_Y    = 'Canal Y'
W_NAME_Cb   = 'Canal Cb'
W_NAME_Cr   = 'Canal Cr'
W_NAME_YEQ  = 'Canal Y Eq'
W_NAME_RGB  = 'Resultante RGB'
W_NAME_RES  = 'Resultante'
W_NAME_RE2S  = 'Resultante2'
BANDA_Y  = 0
BANDA_Cb = 2
BANDA_Cr = 1

for image_path in image_paths:
    print('leu aq')
    img_readed = cv2.imread(image_path)

    (w, h, c) = img_readed.shape
    imgRGBf = np.zeros((w,h,3), dtype=np.float32)
    imgRGBf += img_readed/255.0

    # rgb
    imgR = img_readed[:, :, 0].copy()
    imgG = img_readed[:, :, 1].copy()
    imgB = img_readed[:, :, 2].copy()
    
    # equalized
    imgReq = cv2.equalizeHist(imgR)
    imgGeq = cv2.equalizeHist(imgG)
    imgBeq = cv2.equalizeHist(imgB)

    imgEq = img_readed.copy()
    imgEq[:,:,0] = imgBeq
    imgEq[:,:,1] = imgGeq
    imgEq[:,:,2] = imgReq

    imgGray = cv2.cvtColor(imgRGBf, cv2.COLOR_RGB2GRAY)

    imgYCbCr = cv2.cvtColor(imgRGBf, cv2.COLOR_BGR2YCrCb)
    imgY   = imgYCbCr[:,:,BANDA_Y]
    imgCb  = imgYCbCr[:,:,BANDA_Cb]
    imgCr  = imgYCbCr[:,:,BANDA_Cr]

    # Equalizar a banda Y
    aux = 255*imgY
    imgY = cv2.equalizeHist(aux.astype(np.uint8))

    imgYCbCr[:,:,BANDA_Y] = imgY.astype(float)/255
    imgRGBf = cv2.cvtColor(imgYCbCr, cv2.COLOR_YCrCb2BGR)

    imgLab = cv2.cvtColor(imgRGBf, cv2.COLOR_BGR2LAB)
    imgHSL = cv2.cvtColor(imgRGBf, cv2.COLOR_BGR2HSV)
    imgHSV = cv2.cvtColor(imgRGBf, cv2.COLOR_BGR2HSV)

    # show img_readed and imgEq side by side
    cv2.namedWindow(W_NAME_ORI, cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow(W_NAME_RE2S, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(W_NAME_ORI, img_readed)
    cv2.imshow(W_NAME_RE2S, imgRGBf)



    cv2.waitKey(0)
    

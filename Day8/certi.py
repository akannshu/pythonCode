from PIL import Image,ImageDraw,ImageFont
img = Image.open("./CertificateTemplate.jpg")

import matplotlib.pyplot as plt
import numpy as np

def print_img(img):
    plt.imshow(np.array(img))
    plt.show()

import cv2
img = cv2.imread("./CertificateTemplate.jpg")    

cv2.imshow("certi", img)
cv2.waitKey()
cv2.destroyAllWindows() 
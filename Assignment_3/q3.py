import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

image = cv2.imread("forest.jpg")
gamma = [2, 2.3, 2.5, 2.7]


gamma_smooth = np.array(255*np.multiply(image, 1/255) ** 2.5, dtype = "uint8")

g_r = cv2.equalizeHist(image[:,:,0])
g_g = cv2.equalizeHist(image[:,:,1])
g_b = cv2.equalizeHist(image[:,:,2])
hist_smooth = cv2.merge((g_r,g_g,g_b))


fused1 = np.array(255*np.multiply(hist_smooth, 1/255) ** i, dtype = "uint8")

f_r = cv2.equalizeHist(gamma_smooth[:,:,0])
f_g = cv2.equalizeHist(gamma_smooth[:,:,1])
f_b = cv2.equalizeHist(gamma_smooth[:,:,2])
fused2 = cv2.merge((g_r,g_g,g_b)) #giving best
print(np.max(gamma_smooth))
average = (gamma_smooth + hist_smooth)/2

'''
cv2.imshow("original image",average)
cv2.imshow("gamma-smooth",gamma_smooth)
cv2.imshow("histo-smooth",hist_smooth)
cv2.imshow("gamma and histo fused1",fused1)
cv2.imshow("gamma and histo fused2",fused2)
cv2.waitKey(0)'''

cv2.imwrite('gamma.jpg',gamma_smooth)
cv2.imwrite('histo.jpg',hist_smooth)
'''Part 2'''
#FORMULAE 66E
#I = JT + A(1- T)
#I - A(1-T) / T = J
#(I - A + A*T)T = J
#T = (I - A) / (J - A)

A = [0.8159, 0.8186, 0.8272]
I = image
J = fused2
r,c,v  = image.shape

A_r = np.full((r,c), A[0])
A_g = np.full((r,c), A[1])
A_b = np.full((r,c), A[2])

A = cv2.merge((A_r, A_g, A_b))

T = np.divide((I-A),(J-A))

trans = cv2.imread("trans.jpg")

dist = np.sqrt(np.sum(T**2 - trans**2))
print("Distance : ",dist)

DH = (I - A + (A * trans)) / trans
cv2.imshow("dehazed", DH)

cv2.imshow("T", T)
cv2.waitKey(0)
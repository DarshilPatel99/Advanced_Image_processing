
import matplotlib.pyplot as plt
from skimage import exposure
import cv2

def show_histogram(img):    
    histr = cv2.calcHist(img,[0],None,[256],[0,256]) 
    plt.plot(histr) 
    plt.show()
   
src = cv2.imread('einstein.jpg')
ref = cv2.imread('Lena.jpg')

result_img = exposure.match_histograms(src, ref, multichannel=True)

plt.imshow(src)
plt.title('Source') 
plt.show()
show_histogram(src)

plt.imshow(ref)
plt.title('reference') 
plt.show()
show_histogram(ref)

plt.imshow(result_img)
plt.title('match_histogram image') 
plt.show()
show_histogram(result_img)


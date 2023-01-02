# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 00:38:12 2021

@author: Tarang
"""

from skimage import exposure
import cv2

def show_img(img, label='difault'):    
    cv2.imshow(label, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
source = cv2.imread('einstein.jpg')
reference = cv2.imread('Lena.jpg')

adjusted = exposure.match_histograms(source, reference, multichannel=True)

show_img(source, 'source')
show_img(reference, 'reference')
show_img(adjusted, 'adjusted')
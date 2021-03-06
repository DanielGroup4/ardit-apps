# Exercise: Batch Image Resizing
# Write a script that resizes all images in a directory to 100x100.

import cv2
import glob

from numpy import imag

images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image, 0)
    re = cv2.resize(img, (100, 100))
    cv2.imshow("Hey", re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_" + image , re)


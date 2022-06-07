import cv2

img = cv2.imread("galaxy.jpg", 0)

print(type(img))
print(img)
print(img.shape) # show the matrix´s shape
print(img.ndim) # show the dimension

 # resize the image because is to large, currently has 1485 pixels of heigh and 990 of weigh
resized_img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))  # divide and convert in integer 
cv2.imshow("Galaxy", resized_img)
cv2.imwrite("Galaxy_resized.jpg", resized_img) # this create a save the new resize image 
#cv2.waitKey(2000) # 2 seconds
cv2.waitKey(0) # close until press any button
cv2.destroyAllWindows() # close the windows

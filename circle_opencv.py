import cv2

path = r"C:\Users\USER\Pictures\Screenshots\Screenshot 2025-03-15 161038.png"
image = cv2.imread(path)
cv2.imshow('Original Image', image)

imageCircle = image.copy()
imageCircle  = cv2.circle(imageCircle, (570, 150), 50, (0, 0, 255), thickness = 10, lineType = cv2.LINE_8)

cv2.imshow('Circle Image', imageCircle )
cv2.waitKey(0)
cv2.destroyAllWindows()
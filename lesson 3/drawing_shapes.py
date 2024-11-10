import cv2

image = cv2.imread("bilateral.jpg")

#adding lines to image 
starting_point = (0,0)
ending_point = (230,489)
color = (249,239,230)
thickness = 5
image = cv2.line(image, starting_point, ending_point, color, thickness)

#adding rectanle to image
left_top = (100,100)
right_bottom = (300,300)
color = (200,200,200)
thickness = 30
image = cv2.rectangle(image, left_top, right_bottom, color, thickness)


cv2.imshow("original image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
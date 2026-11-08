import cv2 as cv

# Load images
dog = cv.imread("images/dog.jpeg")
cat = cv.imread("images/cat.png")

# Display images
cv.imshow("Dog image", dog)
cv.imshow("Cat image", cat)

cv.waitKey(0)
cv.destroyAllWindows()

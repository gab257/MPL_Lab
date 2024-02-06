import cv2

img = cv2.imread("C:\\Users\\STUDENT\\PycharmProjects\\TBA_SDL_Lab1\\Images\\Flower.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Flower", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
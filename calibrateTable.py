import cam
import cv2 as cv


result, image = cam.takePic()
if not result: print("No Picture")

# height, width, channels = image.shape
# print(height, width)

dealerImage = image[0:1080, 1200:1920]
player1Image = image[720:1080, 0:1200]
player2Image = image[360:720, 0:1200]
player3Image = image[0:360, 0:1200]


cv.imshow("Dealer1", dealerImage)
cv.imshow("Player1", player1Image)
cv.imshow("Player2", player2Image)
cv.imshow("Player3", player3Image)
cv.waitKey(9000) 
cv.destroyWindow("Dealer")
cv.destroyWindow("Dealer1")
cv.destroyWindow("Player1")
cv.destroyWindow("Player2")
cv.destroyWindow("Player3")
# import cv2 as cv
import playerAdvise as pa
count = 0
cardsInShoe = 312
dealerIndex = 0

advice, count, cardsInShoe = pa.playerRec(0,1080,1200,1920, count, cardsInShoe, dealerIndex)




# cam = cv.VideoCapture(0) 
# result, image = cam.read() 

# dealerImage = image[0:1080, 1200:1920]
# player1Image = image[720:1080, 0:1200]
# player2Image = image[360:720, 0:1200]
# player3Image = image[0:360, 0:1200]

# height, width, channels = image.shape
# print(height, width)

# cv.imshow("Dealer1", dealerImage)
# cv.imshow("Player1", player1Image)
# cv.imshow("Player2", player2Image) 
# cv.imshow("Player3", player3Image)
# cv.waitKey(10000) 
# cv.destroyWindow("Dealer1")
# cv.destroyWindow("Player1")
# cv.destroyWindow("Player2")
# cv.destroyWindow("Player3")

# thingy = ["9h","As","2d","Jc","Qs","Kh"]



# transformed_thingy = [card.replace('d', '').replace('s', '').replace('c', '').replace('h', '')
#                       .replace('A', '11').replace('J', '10').replace('Q', '10').replace('K', '10')
#                       for card in thingy]

# print(transformed_thingy)

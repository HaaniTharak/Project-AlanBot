import cv2 as cv
import cam
import initialCalcs as ic

#Run this to start program


#collect image================================================================
result, image = cam.takePic()
#Check if picture taken properly
if not result: print("Error with taking Picture")

#Split areas of picture================================================================
# height, width, channels = image.shape
# print(height, width)

dealerImage = image[0:360, 0:1280]
player1Image = image[360:720, 0:426]
player2Image = image[360:720, 426:852]
player3Image = image[360:720, 852:1280]

cv.imshow("Dealer", dealerImage)
cv.imshow("Player1", player1Image)
cv.imshow("Player2", player2Image)
cv.imshow("Player3", player3Image)
cv.waitKey(10000) 
cv.destroyWindow("Dealer")
cv.destroyWindow("Player1")
cv.destroyWindow("Player2")
cv.destroyWindow("Player3")

#Run card recognition on areas================================================================
testCardData = []

#send data to initial calcs================================================================
#ToDo Make sure it works with a diffrent number of players
count = 0
cardsInShoe = 312
dealerCards = [8]
player1Cards = [4,5]
player2Cards = [11,10]
player3Cards = [4,2]

dealerInfo, count, cardsInShoe = ic.playerUpdate(dealerCards, count, cardsInShoe)
player1Info, count, cardsInShoe = ic.playerUpdate(player1Cards, count, cardsInShoe)
player2Info, count, cardsInShoe = ic.playerUpdate(player2Cards, count, cardsInShoe)
player3Info, count, cardsInShoe = ic.playerUpdate(player3Cards, count, cardsInShoe)
trueCount = ic.calcTrueCount(count, cardsInShoe)

print("True count is " + str(trueCount) + "Numebr of cards left in shoe are " + str(cardsInShoe) + " dealers total is " + str(dealerInfo) + " Player ones total is " + str(player1Info) )


#Send data to micro================================================================
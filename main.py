import cv2 as cv
import cam
import initialCalcs as ic
import visionModel as vm
import cardFix as cf

#Run this to start program

#collect image================================================================
result, image = cam.takePic()
#Check if picture taken properly
if not result: print("Error with taking Picture")

#Split areas of picture================================================================
# height, width, channels = image.shape
# print(height, width)

dealerImage = image[0:1080, 1200:1920]
player1Image = image[720:1080, 0:1200]
player2Image = image[360:720, 0:1200]
player3Image = image[0:360, 0:1200]


#cv.imshow("Dealer1", dealerImage)
# cv.imshow("Player1", player1Image)
# cv.imshow("Player2", player2Image)
# cv.imshow("Player3", player3Image)
#cv.waitKey(3000) 
#cv.destroyWindow("Dealer")
# cv.destroyWindow("Dealer1")
# cv.destroyWindow("Player1")
# cv.destroyWindow("Player2")
# cv.destroyWindow("Player3")

#Run card recognition on areas================================================================

dealerCards = vm.doVision(dealerImage)
player1Cards = vm.doVision(player1Image)
player2Cards = vm.doVision(player2Image)
player3Cards = vm.doVision(player3Image)

#Remove Suits and convert to integers======================================================
finalDealer = cf.updateCards(dealerCards)
finalPlayer1 = cf.updateCards(player1Cards)
finalPlayer2 = cf.updateCards(player2Cards)
finalPlayer3 = cf.updateCards(player3Cards)


finalDealer = [eval(i) for i in finalDealer]
finalPlayer1 = [eval(i) for i in finalPlayer1]
finalPlayer2 = [eval(i) for i in finalPlayer2]
finalPlayer3 = [eval(i) for i in finalPlayer3]

print(finalDealer)
print(finalPlayer1)
print(finalPlayer2)
print(finalPlayer3)

#send data to initial calcs================================================================

#ToDo Make sure it works with a diffrent number of players
count = 0
cardsInShoe = 312

dealerInfo, count, cardsInShoe = ic.playerUpdate(finalDealer, count, cardsInShoe)
player1Info, count, cardsInShoe = ic.playerUpdate(finalPlayer1, count, cardsInShoe)
player2Info, count, cardsInShoe = ic.playerUpdate(finalPlayer2, count, cardsInShoe)
player3Info, count, cardsInShoe = ic.playerUpdate(finalPlayer3, count, cardsInShoe)
trueCount = ic.calcTrueCount(int(count), int(cardsInShoe))

print("True count is " + str(trueCount) + "Numebr of cards left in shoe are " + str(cardsInShoe) + " dealers total is " + str(dealerInfo) + " Player ones total is " + str(player1Info) )

#Send data to micro================================================================
uart.send(dealerInfo, player1Info, player2Info, player3Info, trueCount)

import visionModel as vm
import cam
import cardFix as cf
import finalDealerIndex
import initialCalcs as ic
import time
import dupRemove as dr

def startGame(count, cardsInShoe):
    numCards = 0
    while True:
        
        result, image = cam.takePic()
        if not result: return False

        dealerImage = image[0:1080, 1200:1920]

        dealerCards = vm.doVision(dealerImage)

        if dealerCards:
            numCards = numCards + 1
            finalDealer = cf.updateCards(dealerCards)
            finalDealer = [eval(i) for i in finalDealer]
            finalDealer = dr.removeDuplicates(finalDealer, numCards)
            dealerInfo, count, cardsInShoe = ic.playerUpdate(finalDealer, count, cardsInShoe)
            dealerIndex = finalDealerIndex.dealerConvertToIndex(dealerInfo)
            print("Dealer Card is " +  str(dealerInfo))
            return dealerIndex, count, cardsInShoe
        
        time.sleep(1)

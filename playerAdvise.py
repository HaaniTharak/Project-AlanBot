import visionModel as vm
import cam
import cardFix as cf
import initialCalcs as ic
import finalIndex
import uart
import time
import dupRemove as dr

def playerRec(x1,x2,y1,y2, count, cardsInShoe, dealerIndex):
    numCards = 1
    while True:
        result, image = cam.takePic()
        if not result: return False

        cards = vm.doVision(image[x1:x2,y1:y2])
        
        if not len(cards):
            print("No cards")
            return "NoPlayer",count, cardsInShoe
            
        
        lastCount = count
        lastNumCards = cardsInShoe
        # print("LastNumCards initial: " + str(lastNumCards))
        # print("CardsInShoe initial: " + str(cardsInShoe))
        numCards = numCards + 1
        finalPlayer = cf.updateCards(cards)
        finalPlayer = [eval(i) for i in finalPlayer]
        finalPlayer = dr.removeDuplicates(finalPlayer, numCards)
        print("Cards: " + str(finalPlayer))
        playerInfo, count, cardsInShoe = ic.playerUpdate(finalPlayer, count, cardsInShoe)
        countChange = count - lastCount
        cardNumChange = lastNumCards - cardsInShoe

        trueCount = int(ic.calcTrueCount(count, cardsInShoe))
        playerIndex = finalIndex.convertToIndex(playerInfo)

        if playerInfo > 21:
            return "Bust", count, cardsInShoe
        
        uart.send(trueCount, playerIndex, dealerIndex)
       
        stand = input("Press s to Stand or anything else to continue ")
        if stand == 's':
            return "Stand", count, cardsInShoe
        
        count = count - countChange

        cardsInShoe = cardsInShoe + cardNumChange
       

import visionModel as vm
import cam
import cardFix as cf
import finalDealerIndex
import initialCalcs as ic
import time
import dupRemove as dr

def scanDealer(count, cardsInShoe):  
    try:
        numCards =  int(input("Enter the number of cards the dealer has when hand is over ")) - 1
    except ValueError:
        print("Re-Input number of cards dealer has when  hand is over ")

    
      
    result, image = cam.takePic()
    if not result: return False

    dealerImage = image[0:1080, 1200:1920]

    dealerCards = vm.doVision(dealerImage)

    finalDealer = cf.updateCards(dealerCards)

    finalDealer = [eval(i) for i in finalDealer]
    
    finalDealer = dr.removeDuplicates(finalDealer, numCards)
    dealerInfo, count, cardsInShoe = ic.playerUpdate(finalDealer, count, cardsInShoe)
    dealerIndex = finalDealerIndex.dealerConvertToIndex(dealerInfo)

    return count, cardsInShoe
    
       
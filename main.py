import startHand
import playerAdvise
import finishDealer

#Run this to start program
count = 0
cardsInShoe = 312

while cardsInShoe > 40:
    dealerIndex, count, cardsInShoe = startHand.startGame(count, cardsInShoe)
    print(count)
    dealerUpCount = count
    print("Player 1: ")
    player1Status, count, cardsInShoe = playerAdvise.playerRec(720,1080,0,1200, count, cardsInShoe, dealerIndex)
    print(count)
    print("Player 2: ")
    player2Status, count, cardsInShoe = playerAdvise.playerRec(360,720,0,1200, count, cardsInShoe, dealerIndex)
    print(count)
    print("Player 3: ")
    player3Status, count, cardsInShoe = playerAdvise.playerRec(0,360,0,1200, count, cardsInShoe, dealerIndex)
    print(count)
    
    count, cardsInShoe = finishDealer.scanDealer(count, cardsInShoe)
    print("Count: "+ str(count))
    print("Cards left: "+ str(cardsInShoe))

    holdForDeal = input("Press any button once cards are cleared")
   
print("Reshuffle and restart program")
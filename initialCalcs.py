
#====================================================================================
# Calculates the player total and adds the cards to the count
def playerUpdate(playerCards, count, cardsInShoe):
    playerTotal = sum(playerCards)
    for i in playerCards:
        if(i == 10 or i == 11):
            count = count - 1
        if(i < 7):
            count = count + 1
        cardsInShoe = cardsInShoe - 1

    return(playerTotal,count, cardsInShoe)
#====================================================================================
#Calculates the true count
def calcTrueCount(count, cardsInShoe):
    return (count / (cardsInShoe / 52))

#====================================================================================


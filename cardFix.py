
def updateCards(inCards):
    final = [card.replace('d', '').replace('s', '').replace('c', '').replace('h', '')
                      .replace('A', '11').replace('J', '10').replace('Q', '10').replace('K', '10')
                      for card in inCards]
    return final

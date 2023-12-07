def convertToIndex(playerTotal):
    if playerTotal >= 4 and playerTotal <= 8:
        return 0
    elif playerTotal > 8 and playerTotal < 17:
        return playerTotal - 8
    elif playerTotal >= 17 and playerTotal <= 21:
        return 9
    else:
        return 24
    
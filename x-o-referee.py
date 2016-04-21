def checkio(game_result):
    for row in game_result:
        if row[0] == row[1] == row[2] and row[0] != '.':
            return row[0]
    rotated = zip(*game_result)
    for row in rotated:
        if row[0] == row[1] == row[2] and row[0] != '.':
            return row[0]
    if game_result[0][0] == game_result[1][1] == game_result[2][2] and game_result[0][0] != '.':
        return game_result[0][0]
    if game_result[0][2] == game_result[1][1] == game_result[2][0] and game_result[0][2] != '.':
        return game_result[0][2]
    return 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"

from operator import indexOf


def locate_card(cards, query):
    return indexOf(cards,query)
    

cards = [13, 11, 10, 7, 4, 3, 1, 0]
query = 7

print("Output: ",locate_card(cards,query))
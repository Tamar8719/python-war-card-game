import random

import Card as c

class Deck:
    sidra = ('❤️', '♦️','♠️', '♣️') #Why it was defined as Tuple???
    klaf_name = ('Two', 'Three', 'Four', 'Five','Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

    def __init__(self):
        self.all_cards = []
        for s in Deck.sidra:
            for r in Deck.klaf_name:
                self.all_cards.append(c.Card(s,r))

    #דורש להוסיף עוד פונקציונליות כגון : ערבוב חפיסה, הוצאת קלף מחפיסה

    def mix(self):
        random.shuffle(self.all_cards)

    def divide(self):
        mid = len(self.all_cards) // 2

        list1 = self.all_cards[:mid]
        list2 = self.all_cards[mid:]

        return list1, list2




if __name__ == '__main__':
    d = Deck()
    for c in d.all_cards:
        print(c)
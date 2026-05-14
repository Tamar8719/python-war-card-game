class Card:
    values = {'Two':2,
              'Three':3,
              'Four':4,
              'Five':5,
              'Six':6,
              'Seven':7,
              'Eight':8,
              'Nine':9,
              'Ten':10,
              'Jack':11,
              'Queen':12,
              'King':13,
              'Ace':14}


    def __init__(self, sidra1, name1):
        self.sidra = sidra1
        self.name = name1
        self.value = Card.values[self.name]

    def __str__(self):
        return self.name + " of " + self.sidra

    #לא לשכוח להוסיף פונקציות השוואה

    def compareTo (self, card):
        tmp =  self.value - card.value
        return tmp





if __name__ == '__main__':
    c1 = Card('Lev', 'Two')
    print(f'{c1} has value: {c1.value}')
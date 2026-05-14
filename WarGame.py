
import Card as c
import Deck as d
import Player as p

#אתחול המשחק
#יצירת החפיסה והשחקנים
print("Card War Game 🃏♣️♦️♥️♠️")
deck= d.Deck()
deck.mix()
list1, list2 = deck.divide()

p1 = p.Player(list1)
p2 = p.Player(list2)

def game(p1, p2):
    if len(p1.list1) == 0 or len(p2.list1) == 0:
        return print(f"The winner: {p1.win(p2.list1)} 🏆🏆")
    p1.take(p2.list1)
    game(p1, p2)
    return 0


game(p1, p2)
#מהלך המשחק עד הודעת הניצחון



#בכל טור הדפיסי הודעה בסגנון
#שחקן א שלף ... , שחקן ב שלף... , שחקן ... ניצח את הסיבוב

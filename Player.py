class Player:

    def __init__(self, list1):
        self.list1 = list1

    def take(self, list2):
        print(f"player 🐶 had card {self.list1[0].name} from the type: {self.list1[0].sidra}")
        print(f"playar 🐻 had card {list2[0].name} from the type: {list2[0].sidra}")
        tmp = self.list1[0].compareTo(list2[0])
        if tmp < 0:
            print("player 🐻 win in this turn!")
            list2.append(self.list1[0])
            list2.append(list2[0])
            self.list1.pop(0)
            list2.pop(0)
        if tmp > 0:
            print("player 🐶 win in this turn!")
            self.list1.append(list2[0])
            self.list1.append(self.list1[0])
            self.list1.pop(0)
            list2.pop(0)
        if tmp == 0:
            print("fight now")
            self.fight(list2)
        return 0


    def fight(self, list2):
        if not list2 or not self.list1:
            return self.win(list2)
        index1 = 3
        index2 = 3
        if len(list2) < 4 :
            index2 = len(list2) - 1
        if len(self.list1) < 4:#fix it because i need that this will be the minimum from  both
            index1 = len(self.list1) - 1
        print(f"index1: {index1} index2: {index2}")
        print(f"playar 🐶 had card {self.list1[index1].name} from the type: {self.list1[index1].sidra}")
        print(f"playar 🐻 had card {list2[index2].name} from the type: {list2[index2].sidra}")
        tmp = self.list1[index1].compareTo(list2[index2])
        if tmp < 0:
            print("player 🐻 win in this turn!")
            list2.extend(self.list1[:index1])
            list2.extend(list2[:index2])
        if tmp > 0:
            print("player 🐶 win in this turn!")
            self.list1.extend(list2[:index2])
            self.list1.extend(self.list1[:index1])
        del self.list1[:index1 + 1]
        del list2[:index2 + 1]
        if tmp == 0:
            print("fight now 🃏🃏🃏")
            self.fight(list2)
        return 0

    def win(self, list2):
        if len(self.list1) > len(list2):
            return  "player 🐶"
        return "player 🐻"





















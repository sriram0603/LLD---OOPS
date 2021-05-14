
class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    
    def getvalue(self):
        return self.rank.value
    
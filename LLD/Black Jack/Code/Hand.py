from .rank import Rank
from .card import card
class Hand:
    def __init__(self):
        self.handList = []
    
    def getVal(self):
        tempvalue = 0
        Aces = 0
        for card in self.handList:
            tempvalue+=card.getvalue()
            if card.rank==Rank.ACE:
                Aces+=1
        while Aces:
            if tempvalue>21:
                tempvalue-=10
            Aces-=1
        return tempvalue
    
        
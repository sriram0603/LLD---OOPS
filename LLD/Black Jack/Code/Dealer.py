from .Deck import Shoe
from .Hand import Hand
class Dealer:
    def __init__(self):
        self.hand = Hand()
    
    def printHand(self):
        return self.hand.handList[0].getvalue()
    
    def hit(self,shoe: Shoe):
        self.hand.handList.append(shoe.drawCard())
    
    def dealCards(self,player,shoe):
        for _ in range(2):
            player.hand.handList.append(shoe.drawCard())
            self.hand.handList.append(shoe.drawCard())
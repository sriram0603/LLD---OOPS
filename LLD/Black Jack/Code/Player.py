from .Hand import Hand
from .Deck import Deck,Shoe
class Player:
    def __init__(self,name: str,amount: int):
        self.name = name
        self.totalAmount = amount
        self.hand = Hand()
    
    def getAMount(self):
        return self.totalAmount
        
    def hit(self, shoe: Shoe):
        self.hand.handList.append(shoe.drawCard())
    
    def updateAmount(self,val):
        self.totalAmount+=val
    
    

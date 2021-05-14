from .suit import Suit
from .rank import Rank
from .card import Card
import random
class Shoe:
    def __init__(self,number_of_decks: int):
        self.decks = number_of_decks
        self.__cards = []
        self.createShoe()
        self.shuffle()
        self.nextCard = 0

    def createShoe(self):
        for _ in range(0,self.decks):
            self.__cards.extend(Deck().getCards())
    
    def shuffle(self):
        for i in range(0,len(self.__cards)):
            j = random.randint(0,len(self.__cards)-i-1)
            self.__cards[i],self.__cards[j]=self.__cards[j],self.__cards[i]

    def drawCard(self) -> Card:
        result = self.__cards[self.nextCard]
        self.nextCard+=1
        return result



class Deck:
    def __init__(self):
        self.cards = []
        self.createDeck()
        self.nextCard = 0
        
    
    def createDeck(self):
        for s in Suit.value:
            for r in Rank.value:
                c = Card(r,s)
                self.cards.append(c)
    
    def getCards(self):
        return self.cards
    
    

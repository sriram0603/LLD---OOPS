from.Deck import Shoe
from .Dealer import Dealer
from .Player import Player
from .hand import Hand
class BlackJack:
    def __init__(self,betAmount):
        self.player = Player("Bhargav",100)
        self.dealer = Dealer()
        self.shoe = Shoe()
        self.betAmount = betAmount
    
    def printHandsandScore(self):
        print(self.player.hand.getVal())
        print(self.dealer.printHand())


    def start(self):
        # ask player to place some bet
        # add 2 cards into player hand and 2 cards into dealer hand
        self.dealer.dealCards(self.player,self.shoe)
        playerScore = self.player.hand.getVal()
        dealerScore = self.dealer.hand.getVal()
        action = int(input("enter the action:"))
        while True:
            self.printHandsandScore()
            if playerScore==21:
                print("player wins")
                self.player.updateAmount(self.betAmount)
                return
            elif playerScore>21:
                print("Dealer wins")
                self.player.updateAmount(-self.betAmount)
                return
            else:
                print("enter 1 to hit and 0 to stand")
                if action ==1:
                    self.player.hit(self.shoe)
                    playerScore =self.player.hand.getVal()
                    print("You chose to hit")
                elif action==0:
                    return self.dealerPlay(playerScore,dealerScore)
                else:
                    print("Inavlid choice, please select 1 or 0")

    def dealerPlay(self,playerScore,dealerScore):
        while dealerScore<17:
            self.dealer.hit(self.shoe)
            dealerScore = self.dealer.hand.getvalue()
        if dealerScore>21:
            print("player Wins")
            self.player.updateAmount(self.betAmount)
            return 1
        elif dealerScore>=playerScore:
            print("Dealer wins")
            self.player.updateAmount(-self.betAmount)
            return 0
        else:
            print("player Wins")
            self.player.updateAmount(self.betAmount)
            return 1



import random


class Game:
    def __init__(self):
        self.deck = []
        for i in range(2, 15):
            self.deck.extend([Card(i, "♥"), Card(i, "♠"),
                             Card(i, "♦"), Card(i, "♣")])


class Card:
    cards = {11: "J", 12: "Q", 13: "K", 14: "A"}
    for low_cards in range(2, 11):
        cards[low_cards] = str(low_cards)

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return self.cards[self.value] + " " + self.suit


class Player:
    def __init__(self, deck, num_cards):
        self.hand = random.sample(deck, num_cards)
        for card in self.hand:
            deck.remove(card)
        self.in_play = []


    def play_card(self):
        return self.hand.pop(0)

    def add_card(self, card):
        self.hand.append(card)

    def compare_and_update(self, card1, card2, pot):
        print(card1, card2)
        if card1.value > card2.value:
            self.add_card(card1)
            self.add_card(card2)

        elif card2.value > card1.value:
            self.add_card(card2)

        else:
            pass
           # deal with a tie
    """we will be implementing most of the game play in player since we need to play a card, 
    add/subtract a card from our own deck."""
    
    """lets implement the compare and "pot" to the player as well to simplify but may be better to 
    add to the Card Class?"""


def main():
    game = Game()
    player1 = Player(game.deck, 26)
    player2 = Player(game.deck, 26)


    print("p1hand",player1.hand, "\np2hand",player2.hand)
    p1_card = player1.play_card()
    p2_card = player2.play_card() 

    player1.compare_and_update(p1_card, p2_card, None)
    print("p1hand",player1.hand, "\np2hand",player2.hand)
    # print("p1hand",player1.hand, "\np2hand",player2.hand)
    # if p1_card.value > p2_card.value:
    #     player1.add_cards(player2)
        
    # elif p1_card.value < p2_card.value:
    #     player2.add_cards(player1)
    # else:
    #     pass
    # print("\np1hand",player1.hand, "\np2hand",player2.hand)



    """not fully working but wanted to brainstorm the While Loop"""
    # while len(player1.hand) < 52 and len(player2.hand) < 52:
    #     card1 = player1.hand[0]
    #     card2= player2.hand[0]
    #     ...
    print()


if __name__ == "__main__":
    main()

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
    """we will be implementing most of the game play in player since we need to play a card, add/subtract a card from our own deck."""
    
    """lets implement the compare and "pot" to the player as well to simplify but may be better to add to the Card Class?"""


def main():
    game = Game()
    player1 = Player(game.deck, 26)
    player2 = Player(game.deck, 26)
    """not fully working but wanted to brainstorm the While Loop"""
    while len(player1.hand) < 52 and len(player2.hand) < 52:
        card1 = player1.hand[0]
        card2= player2.hand[0]
        ...
    print()


if __name__ == "__main__":
    main()

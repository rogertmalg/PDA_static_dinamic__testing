import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("spades", 1)
        self.card2 = Card("Clubs", 7)
        self.cards = [self.card1, self.card2]
        self.cardgame = CardGame()
    
    def test_check_for_ace(self):
        self.assertEqual(True, self.cardgame.check_for_ace(self.card1))
    
    def test_for_highest_card(self):
        self.assertEqual(self.card2, self.cardgame.highest_card(self.card2, self.card1))

    def test_cards_total(self):
        total = self.cardgame.cards_total(self.cards)
        self.assertEqual("You have a total of 8", total)
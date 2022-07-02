
import random


class PlayingCard:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value

    def get_num_value(self):
        if self.value == "ace":
            return 1
        elif self.value == "jack":
            return 10
        elif self.value == "queen":
            return 10
        elif self.value == "king":
            return 10
        else:
            return self.value


class Deck:
    def __init__(self):
        self.cards = []

    def draw_card(self):
        selected_card = random.choice(self.cards)
        removed = selected_card
        self.cards.remove(removed)
        return selected_card

    def init_deck(self):
        suits = ["hearts", "diamonds", "spades", "clubs"]
        values = ["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"]
        for suit in suits:
            for value in values:
                self.cards.append(PlayingCard(suit, value))


class Person:
    def __init__(self, deck):
        """set hand and get two initial cards from the deck"""
        self.hand = Hand()
        self.hand.get_cards(deck)

    def play_turn(self, deck):
        """add a card from the deck to hand"""
        self.hand.get_cards(deck)

    def report_score(self):
        """report total values of the hand"""
        self.hand.get_total_value()


class Dealer(Person):
    def __init__(self, deck):
        """inherit Person Class and set self.name as 'Dealer'"""
        super().__init__(deck)
        self.name = "Dealer"


class Player(Person):
    def __init__(self, deck, name):
        """inherit Person Class and set self.name as what a user typed in"""
        super().__init__(deck)
        self.name = name


class Hand:
    def __init__(self):
        """set self.cards as an empty list"""
        self.cards = []

    def get_cards(self, deck):
        """draw two initial cards from the deck and append them to self.cards"""
        self.cards.append(deck.draw_card())
        self.cards.append(deck.draw_card())

    def get_total_value(self):
        """get total value of cards in the hand"""
        # iterate over self.cards and get the total value from self.cards and return it
        sum = 0
        for card in self.cards:
            sum += card.get_num_value()
        return sum

    def add_card(self, deck):
        """draw one card from the deck and append them to self.cards"""
        self.cards.append(deck.draw_card())


class BlackjackGame:
    def __init__(self):
        """initialize deck and player"""
        self.deck = Deck()
        self.player = None
        self.dealer = None

    def play_game(self):
        # Prime the loop and start the first game.
        user_response = "Y"

        while user_response == "Y" or user_response == "y":
            # fill the deck with 52 cards
            self.deck.init_deck()
            # initialize a player and dealer and get two cards per player
            player_name = input("What's your name?: ")
            self.player = Player(self.deck, player_name)
            self.dealer = Dealer(self.deck)
            Person.__init__(self.player, self.deck)
            Person.__init__(self.dealer, self.deck)
            #"""All control should take a place here"""
            # show score then ask if player will take another card
            print(player_name, "has dealt a hand with a value of", self.player.hand.get_total_value())
            skip_or_play = input("Would you like to take another card? (Y/N): ")
            while skip_or_play == "y" or skip_or_play == "Y":
                if skip_or_play == "y" or skip_or_play == "Y":
                    Person.play_turn(self.player, self.deck)
                    Person.play_turn(self.dealer, self.deck)
                else:
                    print("Your hand now has a total value of:", self.player.hand.get_total_value())
                    take_card = input("Would you like to take another card? (Y/N): ")


                if self.dealer.hand.get_total_value() > 21:
                    break
                if self.player.hand.get_total_value() > 21:
                    break



            # player will be busted if their score is over 21
            if self.player.hand.get_total_value() > 21 and self.dealer.hand.get_total_value() < 21:
                print("You BUSTED with a total value of", self.player.hand.get_total_value())
                print("The dealer was dealt a hand with a value of:", self.dealer.hand.get_total_value())
                print('\n', "** ", player_name, "You Lose! **", '\n')
            elif self.player.hand.get_total_value() > 21 and self.dealer.hand.get_total_value() > 21 :
                print("The dealer BUSTED with a total value of", self.dealer.hand.get_total_value())
                print("You BUSTED with a total value of", self.player.hand.get_total_value())
                print('\n', "** ", player_name, "You Lose! **", '\n')
            # player will lose if the dealer has a higher score than him/her
            elif  self.dealer.hand.get_total_value() > self.player.hand.get_total_value():
                print("The dealer was dealt a hand with a value of:", self.dealer.hand.get_total_value())
                print("Your score:", self.player.hand.get_total_value())
                print('\n', "** ", player_name, "You Lose! **", '\n')
            # player will win if they have a higher score than the dealer
            else:
                print("The dealer was dealt a hand with a value of:", self.dealer.hand.get_total_value())
                print("Your score:", self.player.hand.get_total_value())
                print('\n', "** ", player_name, "You Win! **", '\n')
            user_response = input("Would you like to play again? (Y/N): ")


game = BlackjackGame()
game.play_game()

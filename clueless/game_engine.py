import random

from clueless import game_state


class CardDeck(object):
    """
    The CardDeck represents a deck of game cards
    """

    def __init__(self):

        #create a list of GameCard objects for the suspects
        self._suspects = [
            game_state.GameCard(item=item, item_type=game_state.SUSPECT)
            for item in game_state.SUSPECTS
        ]
        #create a list of GameCard objects for the weapons
        self._weapons = [
            game_state.GameCard(item=item, item_type=game_state.WEAPON)
            for item in game_state.WEAPONS
        ]
        #create a list of GameCard objects for the rooms
        self._rooms = [
            game_state.GameCard(item=item, item_type=game_state.ROOM)
            for item in game_state.ROOMS
        ]
        #create a full list of cards
        self._game_cards = self._suspects + self._weapons + self._rooms

        self._winning_cards = list()

    def draw_winning_cards(self):
        """
        randomly select winning suspect, weapon, and room and
        return a list of the winning cards
        """

        #select the winning cards by choosing a random integer for each index
        # in the list and selecting the game card at that index
        winning_suspect = self._suspects[
            random.choice(range(len(self._suspects)))]
        winning_weapon = self._weapons[
            random.choice(range(len(self._weapons)))]
        winning_room = self._rooms[
            random.choice(range(len(self._rooms)))]

        #assign the selected winners to a list
        self._winning_cards = [winning_suspect, winning_weapon, winning_room]

        #remove the winning cards from the deck
        self._game_cards = [
            game_card for game_card in self._game_cards
            if game_card not in self._winning_cards
        ]

        return self._winning_cards

    def shuffle_cards(self):
        """
        shuffles the game cards
        """
        random.shuffle(self._game_cards)

    def deal_cards(self, num_hands):
        """
        deals the cards by taking the number of hands and return a list
        of lists that contain each seperate hand
        """
        return [self._game_cards[x::num_hands] for x in range(num_hands)]


class GameEngine(object):

    def __init__(self, players):
        self.players = players
        self.game = None

    def start_new_game(self):
        self.game= game_state.GameState(self.players)

        card_deck = CardDeck()

        #poplate the case file with the winning cards
        self.case_file = card_deck.draw_winning_cards()

        #deal cards to the players
        num_players = len(self.players)
        hands = card_deck.deal_cards(num_players)
        for x in range(num_players):
            self.game.players[x].game_cards = hands[x]

    #Todo: Sgonzales complete player move operations
    def handle_move(self, player, space_name):
        pass

    def _move_suspect(self):
        pass

    def _move_weapon(self):
        pass

    def handle_suggestion(self, player, suspect, weapon, room):
        pass

    def handle_suggestion_response(self, player, game_card):
        pass

    def process_accusation(self, player, suspect, weapon, room):
        pass

    def end_player_turn(self, player):
        pass

    def _next_turn(self):
        turn_index = self.game.turn_list.index(self.game.current_player)
        if turn_index < (len(self.game.turn_list)-1):
            turn_index += 1
        else:
            turn_index = 0
        self.game.current_player = self.game.turn_list[turn_index]
        self.game.turn_status = game_state.AWAITING_MOVE

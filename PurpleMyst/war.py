#!/usr/bin/env python3
import collections
import random


def create_deck():
    return [n for n in range(13) for _ in range(4)]


class Player:
    def __init__(self, name, stack):
        self.name = name
        self.stack = collections.deque(stack)

    def draw(self):
        card = self.stack.pop()
        print(self.name, "drew a", card,
              "and now has", len(self.stack), "cards remaining")
        return card

    def _duel_step(self, other_player, current_stack=None):
        if current_stack is None:
            current_stack = []

        if not self.stack:
            other_player.stack.extendleft(current_stack)
            return
        elif not other_player.stack:
            self.stack.extendleft(current_stack)
            return

        my_card = self.draw()
        their_card = other_player.draw()
        current_stack.append(my_card)
        current_stack.append(their_card)

        if my_card > their_card:
            self.stack.extendleft(current_stack)
        elif my_card < their_card:
            other_player.stack.extendleft(current_stack)
        else:
            for _ in range(3):
                if self.stack:
                    current_stack.append(self.draw())
                if other_player.stack:
                    current_stack.append(other_player.draw())
            self._duel_step(other_player, current_stack)

    def duel(self, other_player):
        while self.stack and other_player.stack:
            self._duel_step(other_player)


def main():
    deck = create_deck()
    random.shuffle(deck)

    player1 = Player("Player one", deck[:26])
    player2 = Player("Player two", deck[26:])

    player1.duel(player2)

    if player1.stack:
        print("Player1 wins!")
    else:
        print("Player2 wins!")


if __name__ == "__main__":
    main()

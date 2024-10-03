import random

##########################
## GAME START FUNCTIONS ##
##########################
def generate_cards(size: int, type_card) -> tuple:
    return tuple(
        type_card
        for _ in range(size)
    )
  
def generate_interval_cards(for_each_one: int, interval: tuple) -> tuple[int]:
    return tuple(
        range(interval[0], interval[1] + 1)
    ) * for_each_one


def sort(deck: tuple) -> tuple:
    return tuple(random.sample(deck, len(deck)))


def deal_cards(deck: tuple) -> tuple:
    return (deck[0], deck[2]), (deck[1], deck[3]), deck[4:]
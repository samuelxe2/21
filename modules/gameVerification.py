from itertools import product

##########################
##  GAME VERIFICATIONS  ##
##########################
def check_results_game(player_deck: tuple, crupier_deck: tuple) -> int:
    return check_sum(crupier_deck, sum_cards(crupier_deck)), check_sum(player_deck, sum_cards(player_deck))

def sum_cards(deck: tuple) -> tuple[int]:
    
    def figure_check():
        return tuple(10 if card in ('J', 'Q', 'K') else card for card in deck)

    def as_check(eval_deck):
        if 'As' in eval_deck:
            def combinations_as():
                return product([1, 11], **{'repeat': len([card for card in eval_deck if card == 'As'])}) 

            def possible_sums():
                return frozenset(
                    sum([card for card in eval_deck if isinstance(card, int)]) +
                    sum(combination) for combination in combinations_as()
                )

            return tuple(possible_sums())
        else:
            return (sum(eval_deck),)
    
    return as_check(figure_check())


'''
NOTE: The meaning of the return values are:
No. 0 -> One has obtained a natural blackjack
No. 1 -> One has obtained a blackjack
No. 2 -> One has 16 or less in hand
No. n -> One has 17 or over in hand (And that number is n)
'''
def check_sum(deck: tuple, sums_deck: tuple) -> int:    
    if 21 in sums_deck:
        if len(deck) == 2:
            return 0
        else:
            return 1
        
    if all(sum_card > 21 for sum_card in sums_deck):
        return max(
            sum_card
            for sum_card in sums_deck
            if sum_card > 21
        )

    if any(17 <= sum_card < 21 for sum_card in sums_deck):
        return max(
            (sum_card 
            for sum_card in sums_deck 
            if 17 <= sum_card < 21)
        )
    else:
        return max(
            (sum_card
            for sum_card in sums_deck
            if 2 <= sum_card < 17)
        )

'''
The int status are defined on the docstring in function check_sum()
'''
def check_victory_game(crupier_status: int, player_status: int, user_bet: int):

    if player_status == 0 != crupier_status: return "Blackjack", user_bet + int(user_bet * 1.5) 
    if crupier_status == player_status:      return "Push", user_bet
    
    if crupier_status <= 1 or player_status <= 1:
        if crupier_status < player_status:   return "Lose", 0
        else:                                return "Win", user_bet + user_bet     

    if crupier_status < player_status:       return "Win", user_bet + user_bet
    else:                                    return "Lose", 0
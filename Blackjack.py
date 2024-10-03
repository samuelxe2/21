import random
from itertools import product

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


##########################
##       GAME INFO      ##
##########################
def get_statistics_blackjack(
        player_deck: tuple, 
        crupier_deck: tuple, 
        on: bool,
        player_count: int,
        crupier_count: int
) -> str:

    def count_cards(x):
        return x if x > 2 else 21

    def statistics(player_deck, count_cards, player_count):
        return f"""
    Your cards:             {player_deck}
    Card count:             {count_cards(player_count)}"""

    def yet_revealed_cards(crupier_deck):
        return f"""
    Crupier first card:     {crupier_deck[0]}
    Crupier second card:    ?
    """

    def revealed_cards(crupier_deck, crupier_count):
        return f"""
    Crupier cards:          {crupier_deck}
    Card count:             {count_cards(crupier_count)}
    """

    if on:  
        return statistics(player_deck, count_cards, player_count) + yet_revealed_cards(crupier_deck)
    else:   
        return statistics(player_deck, count_cards, player_count) + revealed_cards(crupier_deck, crupier_count)


def user_options() -> str:
    return """
    1. Hit
    2. Stand
    3. Double Down
    4. Split
    5. Surrender
    """


def get_user_option() -> int:
    return int(input(user_options() + "\nEnter the option: "))


def final_statistics(crupier_deck: tuple, result: str, user_bet: int, money_won: int) -> None:
    
    def verify_bet(x):
        return x * 2 if money_won == -1 or money_won == -2 else x
    
    def verify_money(x):
        return 0 if x == -1 else(user_bet * 2 if x == -2 else x)

    def total_won():
        return 0 if (verify_money(money_won) - verify_bet(user_bet)) < 0 else (verify_money(money_won) - verify_bet(user_bet))

    def total_lost():
        return 0 if (verify_bet(user_bet) - verify_money(money_won)) < 0 else (verify_bet(user_bet) - verify_money(money_won))

    print("Final crupier deck:  ", crupier_deck)
    print("Final result:        ", result)
    print("Original bet:        ", user_bet)
    print("Total won:           ", total_won())
    print("Total lost:          ", total_lost())
    print("Money returned:      ", verify_money(money_won))
    print(" ")


def sign_split_hand(selection: int) -> None:

    def order(x):
        return "1st" if x == 1 else ("2nd" if x == 2 else "")

    print(f"""
    **********************
    **  {order(selection)} split hand  **
    **********************""")


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

    
##########################
##       GAME FLOW      ##
##########################
def game_flow(
        player_deck: tuple, 
        crupier_deck: tuple, 
        game_deck: tuple, 
        user_bet: int,
        on: bool
    ):

    def game_flow_count():
        return check_results_game(player_deck, crupier_deck)

    if on: print(get_statistics_blackjack(player_deck, crupier_deck, on, game_flow_count()[1], game_flow_count()[0]))

    if game_flow_count()[1] > 21:
        if not on: print(get_statistics_blackjack(player_deck, crupier_deck, on, game_flow_count()[1], game_flow_count()[0]))
        return crupier_deck, game_deck, False, 0, "Lose"

    if game_flow_count()[0] > 21:
        print(get_statistics_blackjack(player_deck, crupier_deck, on, game_flow_count()[1], game_flow_count()[0]))
        return crupier_deck, game_deck, False, user_bet + user_bet, "Win"

    def user_option(x): 
        return get_user_option() if x == True else 2

    #print("CHECK: ",crupier_deck)

    match user_option(on):
        ###Player hits###
        case 1:
            return game_flow(
                player_deck + (game_deck[0],), 
                crupier_deck, 
                game_deck[1:], 
                user_bet, 
                on
            )

        ###Player stands###
        case 2:
            if 1 < game_flow_count()[0] < 17 and game_flow_count()[1] != 0:
                print(get_statistics_blackjack(player_deck, crupier_deck, False, game_flow_count()[1], game_flow_count()[0])) #CHECKING
                return game_flow(
                    player_deck, 
                    crupier_deck + (game_deck[0],), 
                    game_deck[1:], 
                    user_bet, 
                    False
                )
            else:
                print(get_statistics_blackjack(player_deck, crupier_deck, False, game_flow_count()[1], game_flow_count()[0]))

            def case_2(check_victory_game):
                return (crupier_deck, game_deck, False, check_victory_game[1], check_victory_game[0])

            return case_2(check_victory_game(game_flow_count()[0], game_flow_count()[1], user_bet))
        
        ###Player doubles down###
        case 3:
            def hof_game_flow():
                return game_flow(
                player_deck + (game_deck[0],),
                crupier_deck,
                game_deck[1:],
                user_bet * 2,
                False
            )

            print("The bet has been duplicated: ", user_bet * 2)

            def change_bet(x, dd_result):
                return -1 if dd_result == "Lose" else (-2 if dd_result == "Push" else x)

            def case_3(hof_game_flow):
                return (hof_game_flow[0], hof_game_flow[1], hof_game_flow[2], change_bet(hof_game_flow[3], hof_game_flow[4]), hof_game_flow[4])

            return case_3(hof_game_flow())
        
        ###Player splits###
        case 4:
            if(len(player_deck) == 2 and player_deck[0] == player_deck[1]):
                
                sign_split_hand(1)
                def left_split():
                    return game_flow(
                    (player_deck[0], game_deck[0]), 
                    crupier_deck, 
                    game_deck[2:], 
                    user_bet, 
                    on
                )

                def right_split(left_split):
                    #Stadistics form the left split
                    final_statistics(left_split[0], left_split[4], user_bet, left_split[3])

                    #Right split
                    sign_split_hand(2)
                    return game_flow(
                        (player_deck[1], game_deck[1]), 
                        left_split[0],
                        left_split[1],
                        left_split[2],
                        user_bet
                    )

                return right_split(left_split())
            
            else:
                print("You have entered a illegal move. You will be kicked out of the Casino")
                return None
        
        ###Player surrender###
        case 5:
            return crupier_deck, game_deck, False, user_bet / 2, "Surrender"
        
        case _:
            print("It seems you're drunk. Please, have a rest and come back next time!")
            return None
        

##########################
##     GAME ACTIONS     ##
##########################
def game_execution(deck_ready):
    '''
    Diagnostics:
    print(deck_ready[0])
    print(deck_ready[1])
    print(deck_ready[2])
    '''
    
    def input_bet(): return int(input("Enter the bet: "))

    def execute_flow(input_bet):
        game_results(game_flow(deck_ready[0], deck_ready[1], deck_ready[2], input_bet, True), input_bet)
    
    print(" ")
    execute_flow(input_bet())

def game_results(game_flow, input_bet):
    if game_flow == None:
        print("Game has ended!")
    else:
        final_statistics(game_flow[0], game_flow[4], input_bet, game_flow[3])

game_execution(deal_cards(sort((
    generate_interval_cards(4, (2, 9))  +
    generate_cards(4, 'J')              +
    generate_cards(4, 'Q')              +
    generate_cards(4, 'K')              +
    generate_cards(4, 10)               +
    generate_cards(4, 'As')
))))



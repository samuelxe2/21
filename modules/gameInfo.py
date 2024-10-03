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
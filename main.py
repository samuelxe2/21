from modules.gameInfo  import final_statistics
from modules.gameStart import *
from modules.gameFlow import game_flow

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
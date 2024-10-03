from modules.gameInfo import *
from modules.gameVerification import *

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
                    if left_split == None: return None

                    #Stadistics form the left split
                    final_statistics(left_split[0], left_split[4], user_bet, left_split[3])

                    #Right split
                    sign_split_hand(2)
                    return game_flow(
                        (player_deck[1], game_deck[1]), 
                        left_split[0],
                        left_split[1],
                        user_bet,
                        not left_split[2]
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
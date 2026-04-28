import time 
from GameState import GameState

class SearchTimeout(Exception):
    pass

def get_best_move(state: GameState, time_limit: float) -> int:
    pass



def minimax(state, depth, alpha, beta, maximizing_player, start_time, time_limit):
    if (time.time() - start_time) > time_limit:
        raise SearchTimeout()
    
    if depth == 0 or state.is_terminal():
        return state.evaluate_board()

    if maximizing_player:
        max_eval = float('-inf')
        for move in state.get_valid_locations():
            pass
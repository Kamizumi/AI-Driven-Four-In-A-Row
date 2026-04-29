import time
from GameState import GameState


class SearchTimeout(Exception):
    pass


def get_best_move(state: GameState, time_limit: float):
    start_time = time.time()
    valid_moves = ordered_moves(state)
    if not valid_moves:
        return None

    best_move = valid_moves[0]
    depth = 1

    while True:
        try:
            current_best_move = None
            current_best_score = float("-inf")

            for move in ordered_moves(state):
                next_state = state.copy()
                next_state.make_move(move[0], move[1], next_state.current_turn)
                score = minimax(
                    next_state,
                    depth - 1,
                    float("-inf"),
                    float("inf"),
                    False,
                    start_time,
                    time_limit,
                )

                if score > current_best_score:
                    current_best_score = score
                    current_best_move = move

            if current_best_move is not None:
                best_move = current_best_move

            depth += 1
        except SearchTimeout:
            break

    return best_move


def ordered_moves(state: GameState):
    moves = state.get_valid_locations()
    center = 3.5
    return sorted(moves, key=lambda move: abs(move[0] - center) + abs(move[1] - center))


def minimax(state, depth, alpha, beta, maximizing_player, start_time, time_limit):
    if (time.time() - start_time) >= time_limit:
        raise SearchTimeout()

    if depth == 0 or state.is_terminal():
        return state.evaluate()

    if maximizing_player:
        max_eval = float("-inf")
        for move in ordered_moves(state):
            next_state = state.copy()
            next_state.make_move(move[0], move[1], next_state.current_turn)
            eval_score = minimax(
                next_state,
                depth - 1,
                alpha,
                beta,
                False,
                start_time,
                time_limit,
            )
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval

    min_eval = float("inf")
    for move in ordered_moves(state):
        next_state = state.copy()
        next_state.make_move(move[0], move[1], next_state.current_turn)
        eval_score = minimax(
            next_state,
            depth - 1,
            alpha,
            beta,
            True,
            start_time,
            time_limit,
        )
        min_eval = min(min_eval, eval_score)
        beta = min(beta, eval_score)
        if beta <= alpha:
            break
    return min_eval

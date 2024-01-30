
from copy import deepcopy
import random
from math import exp

board_size = 5
population = []

def getQueens(board):
    queen_positions = []
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == "Q":
                temp = i,j
                queen_positions.append(temp)
    return queen_positions

def printBoard(board):
    print("printing board...")
    for i in range(board_size):
        for j in range(board_size):
            print(board[i][j], end=' ')
        print()

def isBoardComplete(board):
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == "Q":
                # check row and column
                for k in range(board_size):
                    if k != j and board[i][k] == "Q":
                        return False
                    if k != i and board[k][j] == "Q":
                        return False
                # check diagonals
                for k, l in zip(range(i-1, -1, -1), range(j-1, -1, -1)):
                    if board[k][l] == "Q":
                        return False
                for k, l in zip(range(i-1, -1, -1), range(j+1, board_size)):
                    if board[k][l] == "Q":
                        return False
    return True

def backtracking_search(current_state):
    # check if current state is a goal state
    if is_goal_state(current_state):
        return current_state

    # generate all possible successor states
    successor_states = generate_successors(current_state)

    # iterate over successor states and perform depth-first search
    for successor_state in successor_states:
        result = backtracking_search(successor_state)
        if result is not None:
            return result

    # if no solution found, backtrack
    return None


def main():
    print("N-Queens Problem using Backtracking")
    board = []
    
    # initialize board with empty cells
    for i in range(board_size):
        row = ["-1"] * board_size
        board.append(row)

    # define initial state with random queen placements
    initial_state = [random.randint(0, board_size-1) for i in range(board_size)]
    board = update_board(board, initial_state)

    # print initial state
    print("Initial state:")
    print_board(board)
    
    # solve the problem
    solution = backtracking_search(initial_state)
    
    # print the solution if found, otherwise print failure message
    if solution is not None:
        print("Solution found:")
        board = update_board(board, solution)
        print_board(board)
    else:
        print("No solution found.")

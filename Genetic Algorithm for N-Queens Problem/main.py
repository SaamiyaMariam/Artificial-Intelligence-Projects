
from copy import deepcopy                        
import random                                  
from math import exp                            
import numpy as np

board_size =0
population = []
chromosomePop =[]
fitnessF = []

def putQueens(board):                          
    i = 0
    while (i < board_size):
        row = random.randint(0, board_size - 1)
        if (board[row][i] != "Q"):
            board[row][i] = "Q"
            i+=1

def getQueens(board):                            # This will get the positions of queens palced in the maze
    queen_positions = []                         
    for i in range(board_size):
        for j in range (board_size):
            if board[i][j] == "Q":
                temp = i,j
                queen_positions.append(temp)
    return queen_positions

def printBoard(board):                          
    for i in range(board_size):
        for j in range(board_size):
            print(board[i][j], end=' ')
        print()

def Chromosomes(board):
    k=0
    chr = []
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 'Q':
                position = i
                chr.append(position)
            
    return chr



def objective_function(board):                   # This function will return the number of attacking queens
    positions = getQueens(board)
    attacking_queens = 0
    count = 0
    for i in range (0,len(positions)):
        current_queen = positions[i]
        
        for j in range (0,len(positions)):
            count+=1
            if i!=j:
                other_queen = positions[j]
                
                # Step 1: Seeing if two queens are in same rows
                
                if (other_queen[0] == current_queen[0]):
                    attacking_queens+=1

                # Step 2 : Now we will check diagonals
                
                # There are a total of 4 diagonals

                otherx = other_queen[0]
                othery = other_queen[1]
                x = deepcopy(current_queen[0])            # Copying indexes
                y = deepcopy(current_queen[1])

                # Top-Left Diagonal
                
                while x >=0 and y >= 0:
                    x-=1
                    y-=1

                    if x == otherx and y == othery:
                        attacking_queens+=1
                
                        
                x = deepcopy(current_queen[0])            # Copying indexes
                y = deepcopy(current_queen[1])

                # Bottom-Right Diagonal
                
                while x <board_size and y <board_size:
                    x+=1
                    y+=1

                    if (x == otherx and y == othery):
                        attacking_queens+=1
                
                
                x = deepcopy(current_queen[0])            # Copying indexes
                y = deepcopy(current_queen[1])

                # Bottom-Left Diagonal
                
                while x <board_size and y >=0:
                    x+=1
                    y-=1

                    if (x == otherx and y == othery):
                        attacking_queens+=1
                        
                        
                x = deepcopy(current_queen[0])            # Copying indexes
                y = deepcopy(current_queen[1])        
                
                # Top-Right Diagonal
                
                while x >=0 and y <board_size:
                    x-=1
                    y+=1

                    if x == otherx and y == othery:
                        attacking_queens+=1

    return (int)(attacking_queens/2)


def crossOver(p1, p2):
    
    childCh = []
    for i in range(board_size):
        siz = int(board_size /2)
        childCh[:siz] = p1[:siz]
        childCh[siz:] = p2[siz:]
    return childCh



def main():
    global board_size
    board_size = int(input("Input the board size:"))
    

    rows , cols = (board_size,board_size)
   
    board = []   
    population = []   
    for i in range(10):
        for k in range(rows):
            col = []
            for j in range(cols):
                col.append("*")
            board.append(col)
        putQueens(board)
        printBoard(board)
        population.append(board)

        print()
        #print("-------------------------")
        print()
        #creating chromosomes
        print(Chromosomes(board))
        chromosomePop.append(Chromosomes(board))
        print()
        print()
        print(objective_function(board))
        fitnessF.append(objective_function(board))
        print("-------------------------")
        board = []

    for y in range(9):
        print("CrossOver of Chromosome ", y, " and ", y+1)
        crossoverCh = crossOver(chromosomePop[y], chromosomePop[y+1])
        chromosomePop.append(crossoverCh) #appending new chromosomes to chromosomePop
        print(crossoverCh)

    fitnessVal = fitnessF.sort(reverse = True)
    
    for i in range(10):
        print("fitness: " ,fitnessF[i])
    
if __name__ == "__main__":
    main()


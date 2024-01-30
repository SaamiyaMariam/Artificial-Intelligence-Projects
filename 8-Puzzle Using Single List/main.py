
from collections import defaultdict
graph = defaultdict(list)
# Import random to pick random indexes
import random
# Define a goal state puzzle board representation


Start_State = [4,5,3,2,1,6,7,0,8]
Goal_State = [1,2,3,4,5,6,7,8,0]

def DisplayMatrix(mat):
    i=1
    for j in range(len(mat)):
        if(i%3):
            print(mat[j],end=" ")   
        else:
            print(mat[j])
        i+=1




# Define a function to perform DFS
def dfs(graph, node, visited):
    
    # If the node has not been visited, visit it and continue the DFS on its neighbors
    if node not in visited:
        
        print(node, end=' ') # You can replace this with any custom processing for the node
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited) # Recursively call the dfs function on each unvisited neighbor of the current node i+=1

# Create a set to store the nodes that have been visited
visited = set()



print("Goal State")
DisplayMatrix(Goal_State)
print("Start State")
DisplayMatrix(Start_State)
print()
print()

#to check if the puzzle is solved
def checkSolved(puzzle_board):
    solution = [1,2,3,4,5,6,7,8,0]
    return puzzle_board == solution
    

def solveThePuzzle(Start_State):
    
    while not checkSolved:
      
        moveLeft(Start_State)
        moveRight(Start_State)
        moveUp(Start_State)
        moveDown(Start_State)
        solveThePuzzle(Start_State)

def moveLeft(Start_State):
    print("move left:")
    newState = Start_State[:]
    index=newState.index(0)
    if index not in [0,3,6]:
        tempVar = newState[index-1]
        newState[index-1] = newState[index]
        newState[index]=tempVar
        Start_State=newState
        DisplayMatrix(newState)

def moveRight(Start_State):
    print("move right")
    newState = Start_State[:]
    index=newState.index(0)
    if index not in [2,5,8]:
        tempVar = newState[index+1]
        newState[index+1] = newState[index]
        newState[index]=tempVar
        Start_State=newState
        DisplayMatrix(newState)

def moveUp(Start_State):
    print("move up")
    newState = Start_State[:]
    index=newState.index(0)
    if index not in [0,1,2]:
        tempVar = newState[index-3]
        newState[index-3] = newState[index]
        newState[index]=tempVar
        Start_State=newState
        DisplayMatrix(newState)

def moveDown(Start_State):
    print("move down")
    newState = Start_State[:]
    index=newState.index(0)
    if index not in [6,7,8]:
        tempVar = newState[index+3]
        newState[index+3] = newState[index]
        newState[index]=tempVar
        Start_State=newState
        DisplayMatrix(newState)


Start_State = [0,1,3,4,2,5,7,8,6]
dest_Puzz = [1,2,3,4,5,6,7,8,0]

def DisplayPuzz(Start_State):
  j = 1
  for i in range(len(Start_State)):
    if(j%3):
      print(Start_State[i],end=" ")
    else:
      print(Start_State[i])
    j+=1


def move_left(state):
    new_state = state[:]
    index = new_state.index(0)
    if index not in [0, 3, 6]:
        temp = new_state[index - 1]
        new_state[index - 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None

def move_right(state):
    new_state = state[:]
    index = new_state.index(0)
    if index not in [2, 5, 8]:
        temp = new_state[index + 1]
        new_state[index + 1] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None


def move_up(state):
    new_state = state[:]
    index = new_state.index(0)
    #print("------ index-------", index)
    if index not in [0, 1, 2]:
        temp = new_state[index - 3]
        new_state[index - 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None


def move_down(state):
    new_state = state[:]
    index = new_state.index(0)
    # print(index)
    if index not in [6, 7, 8]:
        temp = new_state[index + 3]
        new_state[index + 3] = new_state[index]
        new_state[index] = temp
        return new_state
    else:
        return None 

def DFS(Start_State):
  no_of_iter = 0
  visited = [Start_State]
  queue = [Start_State]
  while(queue):
    s = queue.pop()
    no_of_iter += 1
    # print(s)  
    if(s == dest_Puzz):
      print("Reached Final State")
      DisplayPuzz(s)
      return no_of_iter
    new_array = []
    new_array.append(move_right(s))
    new_array.append(move_up(s))
    new_array.append(move_down(s))
    new_array.append(move_left(s))
    for i in new_array:
      if i not in visited and i != None:
        visited.append(i)
        queue.append(i)

def IDFS(Start_State,depth):
  nextDepth = 0
  no_of_iter = 0
  visited = [Start_State]
  queue = [Start_State]
  while(queue):
    s = queue.pop()
    no_of_iter += 1
    print("S",s)  
    if(s == dest_Puzz):
      print("Reached Final State")
      DisplayPuzz(s)
      return no_of_iter
    new_array = []
    new_array.append(move_right(s))
    print("new_array after move right",new_array)
    new_array.append(move_up(s))
    print("new_array after move up",new_array)
    new_array.append(move_down(s))
    print("new_array after move down",new_array)
    new_array.append(move_left(s))
    print("new_array after move left",new_array)
    if nextDepth <= depth:
      for i in new_array:
        print( "i",i )
        if i not in visited and i != None:
          print("visited before append",visited)
          visited.append(i)
          print("visited after append",visited)
          print("queue before append",queue)
          queue.append(i)
          print("queue after append",queue)
        print("nextDepth",nextDepth)
        nextDepth+=1
    else:
      print("nextDepth",nextDepth)
      nextDepth-=1

print("Initial State")
DisplayPuzz(Start_State)
iteration =DFS(Start_State)
print("No of iternations in DFS",iteration )


#moveDown(Start_State)
print("solving the Puzzle....")
solveThePuzzle(Start_State)
DisplayMatrix(Start_State)

import tkinter as tk
from tkinter import *
import time
import TestGrids
import heapq


globalGridCapture = 0 
class Cell():

    def __init__(self,x,y):
        self.value = 0
        self.parent = None
        self.x = x
        self.y = y
        self.g = 0
        self.h = 0
        self.f = 0
        self.visited = False


class AStarResources():
    def __init__(self,Grid,method):
        
        self.Values = Grid
        self.cellMatrix = self.Initiate_Maze()
        self.startingCell = self.Get_Cell(1,1)
        self.endingCell = None
        self.listOpen.append(self.startingCell)
        self.heuristicMethod = method

   
                           
    def Initiate_Maze(self):
        maze = []
        for y in range(len(self.Values)):
            row = []
            for x in range(len(self.Values[y])):
                newCell = Cell(x,y)#somebody check if I got the x and y the right way round
                newCell.value = self.Values[y][x]
                row.append(NewCell)
            maze.append(row)
        return maze
    
    def Get_Neigbours():
        pass

    def Get_Heuristics(self,cell):
        
        xDifference = abs(cell.x - self.startingCell.x)
        yDifference = abs(cell.y - self.startingCell.y)
        if self.heuristicMethod == 1:
            #euclidean distance
            distance = ((xDifference**2)+(yDifference)**2)**0.5
        if self.heuristicMethod == 2:
            #manhattan distance
            distance = xDifference + yDifference

        return distance 
            
        
       

    def Get_Cell(self, x, y):
        #returns a specified cell as its object
        #The reference to the cell memory is returned, remember in OOP
        #this means that after x = get_cell(x,y)changing x will change the cell
        return self.cellMatrix[y][x]
    def Update_Cell(self,Cell,Parent):
        # cell.g = origin.g + 10
        # cell.h = get heuristic (cell)
        # cell.f = sum of
        # cell.parent = parent
    
        pass
    def Get_Path(self):
        #get end path 
        pass

    def Select_New_Cell(self):
        #ngl i have no idea why i created this. i obviously had thought of something at the time
        #I think this is the function that gets a new cell with the lowest f from open 
        pass
        

    def Solve(self):
        Origin = self.startingCell
        while found == False:
            if Origin == self.endingCell:
                found = True
                self.Get_Path()
                break
            Origin.visited = True
            Origin.value = 3 #in order for the GUI to see a value is visited we must change its value to 3
            #0 = Unvisited open space
            #1 = Wall
            #2 = Finish
            #3 = Visited
            #4 = Edge
            #Since we actually have attributes for the finish and whether a cell is visited, these values mainly for the use of the GUI 
            neighbours = Get_Neighbours(Origin)
            for Cell in neighbours:
                print("Processed Cell: ", Cell.x , Cell.y)
                if Cell.value == 0 and Cell.visited == False: #No point processing cells that are walls since we cant move to them anyway.
                    #By doing this we increase efficiency
                    Update_Cell(Cell,Origin) #sends target 'neighbour' cell and also orgin cell to be set as its parent
                    self.listOpen.append(Cell)
                    print("Processed Cell: ", Cell.x ,",", Cell.y)
                    print("Appended Cell ", Cell.x, "," , Cell.y, "to the open list")
            print("Open List now contains objects", self.listOpen)
            
            #Now after calculating heuristic we must choose the cell with the lowest f value as the new origin
                    
                
            #Choose Cell lowest F from open list using select new cell function .already made look up 
            #origin = chosencell

            #RETURN THE FINISHED PATH AND THE GRID SO IT CAN BE DISPLAYED!!!!!
            

def Run_AStar_Tests():
    pass

        
def Move(Matrix,x,y):

    
    if Matrix[y][x] == 2:
        global globalGridCapture
        globalGridCapture = Matrix
        print ('found at %d,%d' % (x, y)) 
        return True
        
    elif Matrix[y][x] == 1: 
        print ('wall at %d,%d' % (x, y)) 
        return False 
    elif Matrix[y][x] == 3: 
        print ('visited at %d,%d' % (x, y)) 
        return False
    elif Matrix[y][x] == 4: 
        print ('edge at %d,%d' % (x, y)) 
        return False
    
    print ('visiting %d,%d' % (x, y)) 
    Matrix[y][x] = 3
    
    if ((x < len(Matrix)-1 and Move(Matrix,x+1, y)) 
 
        or (y > 0 and Move(Matrix,x, y-1)) 

        or (x > 0 and Move(Matrix,x-1, y)) 

        or (y < len(Matrix)-1 and Move(Matrix,x, y+1))): 
 
        return True 
 
    return False


           
def ValidateInteger(userInput , intMin , intMax):
    
    try:
        int(userInput)
    except:
        
        return True
    
    userinput = int(userInput)
    if userinput < intMin:
        print("input was not valid")
        return True
    elif userinput > intMax:
        print("input was not valid")
        return True
    else:
        return False
    
def Close_Window(root):
    root.destroy()
def Display_Result(Grid):
    root = Tk()
    wall = tk.PhotoImage(file = "MazePiece_Wall.gif")
    space = tk.PhotoImage(file = "MazePiece_Space.gif")
    edge = tk.PhotoImage(file = "MazePiece_Outer.gif")
    visited = tk.PhotoImage(file = "MazePiece_Visited.gif")
    finish = tk.PhotoImage(file = "MazePiece_Finish.gif")
        
    for y in range(len(Grid)):
        for x in range(len(Grid[y])):
            if Grid[y][x] == 0:
                label = Label(root, image=space, width = 30 , height = 30).grid(row = y , column = x)
            elif Grid[y][x] == 1:
                label = Label(root, image=wall , width = 30 , height = 30).grid(row = y , column = x)
            elif Grid[y][x] == 2:
                label = Label(root, image=finish , width = 30 , height = 30).grid(row = y , column = x)
            elif Grid[y][x] == 3:
                label = Label(root, image=visited , width = 30 , height = 30).grid(row = y , column = x)
            elif Grid[y][x] == 4:
                label = Label(root, image=edge , width = 30 , height = 30).grid(row = y , column = x)
                
    b = Button(root, text = "Next" , command = lambda: Close_Window(root)).grid(row = round((len(Grid[1])/2))  , column = (len(Grid)+1))
    root.lift()
    root.attributes('-topmost', True)
    root.attributes('-topmost', False)
    root.mainloop()
          

def main():
    print("Starting")
    gridStore = TestGrids.ImportMatrices()
    Grid = gridStore.TestMaze4
    userInput = None
    while ValidateInteger(userInput,1,2):
        print()
        print("Please choose an method")
        print("1 = A Star")
        print("2 = Depth First Search")
        print("3 = Breadth First Search")
        userInput = input()
    userInput = int(userInput)

        
    #---A Star---#
    if userInput == 1:


        method = None
        while ValidateInteger(method,1,2):
            print("Please choose heuristic method:")
            print("1 = Manhattan")
            print("2 = Euclidean")
            method = input()
        method = int(method)
            

       
        choice = None

        
        while ValidateInteger(choice,1,2):
            print("1 = Run Program")
            print("2 = Run Tests") 
            choice = input()
        choice = int(choice)
        
        if choice == 1:
            print("Initialising AStar")
            AStar = AStarResources(Grid,method)
            Path,Grid = Astar.Solve()

            
        elif choice == 2:
            Run_AStar_Tests()

            

        
    #---Recursive Depth First---#
    elif userInput == 2:
        
        
        Display_Result(Grid)
        StartPosx = 1
        StartPosy = 1
        Move(Grid , StartPosx , StartPosy)
        try:
            Display_Result(globalGridCapture)
        except:
            print("The finish could not be found or is inaccessible")
        
        
    
    #---Breadth First---#
    elif userInput == 3:
        pass
    




        
       
        
       






main()
    
    #starttime = time.time()
    #Maze = NewMaze()


##    for i in range(len(Maze.cellMatrix)):
##        print("")
##        for y in range(len(Maze.cellMatrix[i])):
##            print(Maze.cellMatrix[i][y].value, end = "")
##    print("")
##    elapsedtime = time.time() - starttime
##    print("Time Taken:",elapsedtime)
##   
##
##        






        
##        self.wall = tk.PhotoImage(file = "MazePiece_Wall.gif")
##        self.space = tk.PhotoImage(file = "MazePiece_Space.gif")
##        self.edge = tk.PhotoImage(file = "MazePiece_Outer.gif")
##        self.visited = tk.PhotoImage(file = "MazePiece_Visited.gif")
##        self.finish = tk.PhotoImage(file = "MazePiece_Finish.gif")
##        

##    def UpdateMaze(self):
##        for y in range(len(self.maze)):
##            for x in range(len(self.maze[y])):
##                if self.maze[y][x] == 0:
##                    label = Label(root, image=self.space, width = 30 , height = 30).grid(row = y , column = x)
##                elif self.maze[y][x] == 1:
##                    label = Label(root, image=self.wall , width = 30 , height = 30).grid(row = y , column = x)
##                elif self.maze[y][x] == 2:
##                    label = Label(root, image=self.finish , width = 30 , height = 30).grid(row = y , column = x)
##                elif self.maze[y][x] == 3:
##                    label = Label(root, image=self.visited , width = 30 , height = 30).grid(row = y , column = x)
##                elif self.maze[y][x] == 4:
##                    label = Label(root, image=self.edge , width = 30 , height = 30).grid(row = y , column = x)
##


                    



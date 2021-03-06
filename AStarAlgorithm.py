
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
    def Display_Details(self):
        print("Cell ", self.x ,",", self.y )
        print("Holds value - ", self.value)
        print("G Value - ", self.g)
        print("Heuristic Distance - ",self.h)
        print("F Value - " , self.f)
        if self.visited == True:
            print("This cell has been visited/processed")
        else:
            print("This cell has not been visited yet")
        print(self.parent)
class AStarResources():
    def __init__(self,Grid,method):
        self.listOpen = []
        self.Values = Grid
        self.cellMatrix = self.Initiate_Maze()
        validSelection = False
        while validSelection == False:
            print("Please enter a starting position")
            userStartx = int(input("X Value: "))
            userStarty = int(input("Y Value: "))
            if self.Validate_Cell(self.Get_Cell(userStartx , userStarty)) == True:
                validSelection = True
                self.startingCell = self.Get_Cell(userStartx,userStarty)
                self.startingCell.value = 10 
            else:   
                print("The chosen starting cell is a wall and is invalid as a starting point")
                print("Please choose another")
        validSelection = False
        while validSelection == False:
            print("Please enter an ending position")
            userEndx = int(input("X Value: "))
            userEndy = int(input("Y Value: "))
            if self.Validate_Cell(self.Get_Cell(userEndx,userEndy)) == True:
                validSelection = True
                self.endingCell = self.Get_Cell(userEndx,userEndy)
                self.endingCell.value = 2 
            else:
                print("The chosen starting cell is a wall and is invalid as a starting point")
                print("Please choose another") 
        self.listOpen.append(self.startingCell)
        self.heuristicMethod = method
        self.Values[self.endingCell.y][self.endingCell.x] = 2
        self.Values[self.startingCell.y][self.startingCell.x] = 10
        
        Display_Result(self.Values)            
    def Initiate_Maze(self):
        maze = []
        for y in range(len(self.Values)):
            row = []
            for x in range(len(self.Values[y])):
                newCell = Cell(x,y)#somebody check if I got the x and y the right way round
                newCell.value = self.Values[y][x]
                row.append(newCell)
            maze.append(row)
        return maze
    def Get_Neighbours(self,cell):
        neighbourNorth = self.Get_Cell(cell.x,((cell.y)-1))
        neighbourEast = self.Get_Cell(((cell.x)+1),cell.y)
        neighbourSouth = self.Get_Cell(cell.x,((cell.y)+1))
        neighbourWest = self.Get_Cell(((cell.x)-1),cell.y)
        Neighbours = [neighbourNorth,neighbourEast,neighbourWest,neighbourSouth]
        return Neighbours
    def Get_Heuristics(self,cell):
        xDifference = abs(cell.x - self.endingCell.x)
        yDifference = abs(cell.y - self.endingCell.y)
        if self.heuristicMethod == 2:
            #euclidean distance
            distance = (((xDifference**2)+(yDifference)**2)**0.5) #<-- made a multiplier to get it on track
        if self.heuristicMethod == 1:
            #manhattan distance
            distance = xDifference + yDifference

        return distance 
    def Get_Cell(self, x, y):
        #returns a specified cell as its object
        #The reference to the cell memory is returned, remember in OOP
        #this means that after x = get_cell(x,y)changing x will change the cell
        return self.cellMatrix[y][x]
    def Update_Cell(self,cell,Parent):
         cell.g = Parent.g + 0.6 #0.7
         cell.h = self.Get_Heuristics(cell)
         cell.f =  cell.g + cell.h
         cell.parent = Parent
    def Get_Path(self,rootCell):
        while rootCell.parent != None:
            if rootCell.value == 2:
                print("Starting at root cell ", rootCell.x ,"," , rootCell.y)
            else:
                if rootCell.x > rootCell.parent.x and rootCell.y == rootCell.parent.y:
                    rootCell.value = 6
                elif rootCell.x == rootCell.parent.x and rootCell.y > rootCell.parent.y:
                    rootCell.value = 7
                elif rootCell.x < rootCell.parent.x and rootCell.y == rootCell.parent.y:
                    rootCell.value = 8
                elif rootCell.x == rootCell.parent.x and rootCell.y < rootCell.parent.y:
                    rootCell.value = 9
                    
            prevCell = rootCell
            rootCell = rootCell.parent



            
        #get end path
    def Find_Minimum(self,List):
      #include the design for this recursive function
        if len(List)==1:
            return List[0]
        elif len(List)==2:
            if List[0].f < List[1].f:
                return List[0]
            else:
                return List[1]
        else:
            testvalue = self.Find_Minimum(List[1:])
            if List[0].f < testvalue.f:
                return List[0]
            else:
                return testvalue
    def Validate_Cell(self,cell): # WHEN A STARTING POSITION IS ENTERED ABOVE THE LIMIT IT IS NOT PICKING IT UP TO BE FIXED !!!
        if cell.x > len(self.cellMatrix[1]):
            return False
        elif cell.y > len(self.cellMatrix):
            return False
        elif cell.value != 0:
            return False
        elif cell.visited == True:
            return False
        else:
            return True 
    def Select_New_Cell(self):
        minimumCell = self.Find_Minimum(self.listOpen)
        return minimumCell
    def Solve(self):
        Origin = self.startingCell
        found = False
        while found == False:          
            if Origin == self.endingCell:
                found = True
                self.Update_Cell(Origin,Previous)
                self.Get_Path(Origin)
                return self.cellMatrix
                break
                print("End was found")
            neighbours = self.Get_Neighbours(Origin)
            for Cell in neighbours:
                if Cell == self.endingCell:
                    Cell.f = 0
                    self.listOpen.append(Cell)
                else:
                    
                    if self.Validate_Cell(Cell) == True: #No point processing cells that are walls since we cant move to them anyway.
                        #By doing this we increase efficiency
                        self.Update_Cell(Cell,Origin) #sends target 'neighbour' cell and also origin cell to be set as its parent
                        self.listOpen.append(Cell)
                        Cell.value = 5
                    else:
                        pass
            #issue to talk about - the program kept selecting the starting cell as the new origin every time becuase we forgot to remove it from the open
            #list. Since the cost function did not have any biases towards weight over cost. It chose the same cell every time           
            Origin.visited = True
            self.listOpen.remove(Origin)
            Origin.value = 3 #in order for the GUI to see a value is visited we must change its value to 3
            Previous = Origin
            Origin = self.Select_New_Cell()
            #RETURN THE FINISHED PATH AND THE GRID SO IT CAN BE DISPLAYED!!!!!
        
def Cell_Convert(cellMatrix):
        grid = []
        for cell in cellMatrix:
            row = []
            for inner in cell:
                row.append(inner.value)
            grid.append(row) 
        return grid           
def Run_AStar_Tests(): #DELETE THIS AND THE OPTION IN MAIN TO USE IT 
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
    imageheight = 11
    imagewidth = 11
    root = Tk()
    wall = tk.PhotoImage(file = "GUI_Image_Wall.gif")
    space = tk.PhotoImage(file = "GUI_Image_Space.gif")
    edge = tk.PhotoImage(file = "GUI_Image_Outer.gif")
    visited = tk.PhotoImage(file = "GUI_Image_Visited.gif")
    finish = tk.PhotoImage(file = "GUI_Image_Finish.gif")
    processed = tk.PhotoImage(file = "GUI_Image_Processed.gif")
    pathLeft = tk.PhotoImage(file = "GUI_Image_Path_Left.gif")
    pathRight = tk.PhotoImage(file = "GUI_Image_Path_Right.gif")
    pathUp = tk.PhotoImage(file = "GUI_Image_Path_Up.gif")
    pathDown = tk.PhotoImage(file = "GUI_Image_Path_Down.gif")
    Start = tk.PhotoImage(file = "Untitled-3.PSD")
    for y in range(len(Grid)):
        for x in range(len(Grid[y])):
            if Grid[y][x] == 0:
                label = Label(root, image=space, width = imagewidth , height = imageheight).grid(row = y , column = x)
            elif Grid[y][x] == 1:
                label = Label(root, image=wall , width = imagewidth , height = imageheight).grid(row = y , column = x)
            elif Grid[y][x] == 2:
                label = Label(root, image=finish , width = imagewidth , height = imageheight).grid(row = y , column = x)
            elif Grid[y][x] == 3:
                label = Label(root, image=visited , width = imagewidth , height = imageheight).grid(row = y , column = x)
            elif Grid[y][x] == 4:
                label = Label(root, image=edge , width = imagewidth , height = imageheight).grid(row = y , column = x)
            elif Grid[y][x] == 5:
                label = Label(root, image=processed , width = imagewidth , height = imageheight).grid(row = y , column = x)
            elif Grid[y][x] == 6:
                label = Label(root, image=pathRight , width = imagewidth , height = imageheight).grid(row = y , column = x)
            elif Grid[y][x] == 7:
                label = Label(root, image=pathDown , width = imagewidth , height = imageheight).grid(row = y , column = x)
            elif Grid[y][x] == 8:
                label = Label(root, image=pathLeft , width = imagewidth , height = imageheight).grid(row = y , column = x)
            elif Grid[y][x] == 9:
                label = Label(root, image=pathUp , width = imagewidth , height = imageheight).grid(row = y , column = x)
            elif Grid[y][x] == 10:
                label = Label(root, image=Start, width = imagewidth , height = imageheight).grid(row = y , column = x)
                
                
    b = Button(root, text = "Next" , command = lambda: Close_Window(root),height= 1 ,width = 1).grid(row = round((len(Grid)+1))  , column = (len(Grid)+1))
    root.lift()
    root.attributes('-topmost', True)
    root.attributes('-topmost', False)
    root.mainloop()
    
def main():
    print("Starting")
    gridStore = TestGrids.ImportMatrices()
    Grid = gridStore.TestMaze3
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
           # Path,Grid = Astar.Solve()
            Grid = AStar.Solve()
            Display_Result(Cell_Convert(Grid))
        elif choice == 2:
            Run_AStar_Tests()  
    #---Recursive Depth First---#
    elif userInput == 2:       
        StartPosx = int(input("Input Start Position X:"))
        StartPosy = int(input("Input Start Position Y:"))
        EndPosx = int(input("Input End Position X:"))
        EndPosy = int(input("Input End Position Y:"))
        Grid[EndPosy][EndPosx] = 2
        Display_Result(Grid)
        
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
##                    label = Label(root, image=self.space, width = imageheight , height = imageheight).grid(row = y , column = x)
##                elif self.maze[y][x] == 1:
##                    label = Label(root, image=self.wall , width = imageheight , height = imageheight).grid(row = y , column = x)
##                elif self.maze[y][x] == 2:
##                    label = Label(root, image=self.finish , width = imageheight , height = imageheight).grid(row = y , column = x)
##                elif self.maze[y][x] == 3:
##                    label = Label(root, image=self.visited , width = imageheight , height = imageheight).grid(row = y , column = x)
##                elif self.maze[y][x] == 4:
##                    label = Label(root, image=self.edge , width = imageheight , height = imageheight).grid(row = y , column = x)
##


                    

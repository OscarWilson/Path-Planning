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
            else:
                
                print("The chosen starting cell was not valid")
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
                print("The chosen starting cell was not valid")
                print("Please choose another")
                
        
        self.listOpen.append(self.startingCell)
        self.heuristicMethod = method

   
                           
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
         cell.g = Parent.g + 0.7
         cell.h = self.Get_Heuristics(cell)
         cell.f =  cell.g + cell.h
         cell.parent = Parent
    
    def Get_Path(self):
        #get end path
        print("GETTING PATH")
        #mark all pathpoints as cell.value = GUI_Image_Path
        pass
    
    def Find_Minimum(self,List):
      #include the design for this recursive function
        if len(List)==2:
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
    def Validate_Cell(self,cell):
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
            print("Start Origin =", Origin)
            print("With an f value of " , Origin.f)
            print("And a g value of ", Origin.g)
            print("And an h value of " , Origin.h) 
            print()
                            
            if Origin == self.endingCell:
                found = True
                self.Get_Path()
                return self.cellMatrix
                break
                print("End was found")
           
            #0 = Unvisited open space
            #1 = Wall
            #2 = Finish
            #3 = Visited
            #4 = Edge
            #5 = Open List
            #Since we actually have attributes for the finish and whether a cell is visited, these values mainly for the use of the GUI

            neighbours = self.Get_Neighbours(Origin)
            #APPENDING VALID NEIGHBOURS TO OPEN LIST
            print()
            print()
            print()
            print("Evaluating Origins Neighbours")
            for Cell in neighbours:
                if Cell == self.endingCell:
                    Cell.f = 0
                    self.listOpen.append(Cell)
                else:
                    
                    if self.Validate_Cell(Cell) == True: #No point processing cells that are walls since we cant move to them anyway.
                        #By doing this we increase efficiency
                        print("Updating neighbours")
                        self.Update_Cell(Cell,Origin) #sends target 'neighbour' cell and also origin cell to be set as its parent
                        self.listOpen.append(Cell)
                        Cell.value = 5
                        print("Appended Cell ", Cell.x, "," , Cell.y, "to the open list")
                    else:
                        print("Cell ", Cell.x, "," , Cell.y, "was not valid")
           
           

            #issue to talk about - the program kept selecting the starting cell as the new origin every time becuase we forgot to remove it from the open
            #list. Since the cost function did not have any biases towards weight over cost. It chose the same cell every time 

                    
            Origin.visited = True
            self.listOpen.remove(Origin)
            Origin.value = 3 #in order for the GUI to see a value is visited we must change its value to 3

            Origin = self.Select_New_Cell()
            
            print("The open list is",self.listOpen )
            print("F VALUES")
            for Cell in self.listOpen:
                print("Cell ", Cell , " Has H Value " , Cell.h ,"Has G Value" , Cell.g , "Has F Value " , Cell.f)
        


            
            #  Display_Result(self.Cell_Convert(self.cellMatrix))  
                
            #Now after calculating heuristic we must choose the cell with the lowest f value as the new origin
                    
                
            #Choose Cell lowest F from open list using select new cell function .already made look up 
            #origin = chosencell

            #RETURN THE FINISHED PATH AND THE GRID SO IT CAN BE DISPLAYED!!!!!


            
def Cell_Convert(cellMatrix):
        grid = []
        for cell in cellMatrix:
            row = []
            for inner in cell:
                row.append(inner.value)
            grid.append(row) 
        return grid           

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
    wall = tk.PhotoImage(file = "GUI_Image_Wall.gif")
    space = tk.PhotoImage(file = "GUI_Image_Space.gif")
    edge = tk.PhotoImage(file = "GUI_Image_Outer.gif")
    visited = tk.PhotoImage(file = "GUI_Image_Visited.gif")
    finish = tk.PhotoImage(file = "GUI_Image_Finish.gif")
    processed = tk.PhotoImage(file = "GUI_Image_Processed.gif")
    path = tk.PhotoImage(file = "GUI_Image_Path.gif")
                           
    
        
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
            elif Grid[y][x] == 5:
                label = Label(root, image=processed , width = 30 , height = 30).grid(row = y , column = x)
                
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
           # Path,Grid = Astar.Solve()
            Grid = AStar.Solve()
            Display_Result(Cell_Convert(Grid))

            
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


                    

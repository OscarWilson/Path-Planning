import tkinter as tk
from tkinter import *
import time




class MazeGUI():
    def __init__(self):
        
        self.maze = [
        [4,  4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,  4],
        [4,  0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,  4], 
        [4,  0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0,  4],
        [4,  0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,  4],  
        [4,  0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,  4],
        [4,  0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,  4], 
        [4,  0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,  4],
        [4,  0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,  4],  
        [4,  0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0,  4],
        [4,  0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0,  4], 
        [4,  0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0,  4],
        [4,  0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0,  4],  
        [4,  0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,  4],        
        [4,  0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0,  4], 
        [4,  0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,  4],
        [4,  1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1,  4],  
        [4,  2, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0,  4],
        [4,  0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1,  4], 
        [4,  0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0,  4],
        [4,  0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0,  4],  
        [4,  0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  4],
        [4,  4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,  4],
        ]


        
        self.wall = tk.PhotoImage(file = "MazePiece_Wall.gif")
        self.space = tk.PhotoImage(file = "MazePiece_Space.gif")
        self.edge = tk.PhotoImage(file = "MazePiece_Outer.gif")
        self.visited = tk.PhotoImage(file = "MazePiece_Visited.gif")
        self.finish = tk.PhotoImage(file = "MazePiece_Finish.gif")
        

    def UpdateMaze(self):
        for y in range(len(self.maze)):
            for x in range(len(self.maze[y])):
                if self.maze[y][x] == 0:
                    label = Label(root, image=self.space, width = 30 , height = 30).grid(row = y , column = x)
                elif self.maze[y][x] == 1:
                    label = Label(root, image=self.wall , width = 30 , height = 30).grid(row = y , column = x)
                elif self.maze[y][x] == 2:
                    label = Label(root, image=self.finish , width = 30 , height = 30).grid(row = y , column = x)
                elif self.maze[y][x] == 3:
                    label = Label(root, image=self.visited , width = 30 , height = 30).grid(row = y , column = x)
                elif self.maze[y][x] == 4:
                    label = Label(root, image=self.edge , width = 30 , height = 30).grid(row = y , column = x)
 
def Move(Maze,x,y):

    
    if Maze.maze[y][x] == 2: 
        print ('found at %d,%d' % (x, y)) 
        return True 
    elif Maze.maze[y][x] == 1: 
        print ('wall at %d,%d' % (x, y)) 
        return False 
    elif Maze.maze[y][x] == 3: 
        print ('visited at %d,%d' % (x, y)) 
        return False
    elif Maze.maze[y][x] == 4: 
        print ('edge at %d,%d' % (x, y)) 
        return False
    
    print ('visiting %d,%d' % (x, y)) 
    Maze.maze[y][x] = 3
    
    if ((x < len(Maze.maze)-1 and Move(Maze,x+1, y)) 
 
        or (y > 0 and Move(Maze,x, y-1)) 

        or (x > 0 and Move(Maze,x-1, y)) 

        or (y < len(Maze.maze)-1 and Move(Maze,x, y+1))): 
 
        return True 
 
    return False


root = Tk()
Maze = MazeGUI()
Maze.UpdateMaze()
StartPosX = 1
StartPosY = 1
Move(Maze,StartPosX,StartPosY)
Maze.UpdateMaze()
print()
for i in range(len(Maze.maze)):
    print(Maze.maze[i])
    
root.mainloop()

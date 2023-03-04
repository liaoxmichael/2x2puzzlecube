# Michael Liao
# CSC 372 Artificial Intelligence
# A1
''' Description: 
    This file contains a the Node class, which will be used to keep track of the state of the cube
    (purely the action taken and the previous action, parent). Each time a node is generated, it
    references the parent node's depth value to calculate its own (+1). fscore is purely depth;
    this node is used for comparison against my heuristic search.
'''
from cube import Cube

class Node:
    action = int # 0: F/B, 5: F'/B', 1: R/L, 4: R'/L', 2: U/D, 3: U'/D'
    parent = None # root if no parent, check with "is" keyword
    depth = int
    cube = Cube
    fscore = float

    def __init__(self, action, parent, depth, cube=Cube):
        self.action = action
        self.parent = parent
        self.depth = depth
        self.cube = cube.deepCopy()
        self.act()
        self.fscore = self.depth

    def act(self): # performs the chosen action on the cube
        if self.action != -1:
            action_map = {0: self.cube.frontCW, 5: self.cube.frontCCW, 1: self.cube.rightCW, 4: self.cube.rightCCW, 2: self.cube.topCW, 3: self.cube.topCCW}
            action_map[self.action]()
    
    def __repr__(self): # adding a string representation that will make printing out solutions easier
        return self.action
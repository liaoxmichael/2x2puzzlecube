# Michael Liao
# CSC 372 Artificial Intelligence
# A1
''' Description: 
    This file contains a the Node class, which will be used to keep track of the state of the cube
    (purely the action taken and the previous action, parent). Each time a node is generated, it
    references the parent node's depth value to calculate its own (+1). The heuristic we will use
    is the total Manhattan distance displacement of each cube from solved divided by 4, which will
    factor into our fscore that we use to perform IDA*.
'''
from cube import Cube

class Node:
    action = int # 1: F/B, 2: F'/B', 3: R/L, 4: R'/L', 5: U/D, 6: U'/D'
    parent = None # root if no parent, check with "is" keyword
    depth = int
    heuristic = float
    fscore = float

    def __init__(self, action, parent, depth, cube=Cube):
        self.action = action
        self.parent = parent
        self.depth = depth
        # will have code here to calculate the heuristic score of this state so can compare in solver.py IDA*
        # found when the node is generated
        self.fscore = self.depth + self.heuristic

    def act(self, cube=Cube): # performs the chosen action on the cube
        action_map = {1: cube.frontCW, 2: cube.frontCCW, 3: cube.rightCW, 4: cube.rightCCW, 5: cube.topCW, 6: cube.topCCW}
        action_map[self.action]()
    
    def __repr__(self): # adding a string representation that will make printing out solutions easier
        return self.action
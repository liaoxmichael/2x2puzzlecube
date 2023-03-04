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
    action = int # 0: F/B, 5: F'/B', 1: R/L, 4: R'/L', 2: U/D, 3: U'/D'
    parent = None # root if no parent, check with "is" keyword
    depth = int
    cube = Cube
    heuristic = float
    fscore = float

    def __init__(self, action, parent, depth, cube=Cube):
        self.action = action
        self.parent = parent
        self.depth = depth
        self.cube = cube.deepCopy()
        self.act()
        self.heuristic = self.getHeuristic()
        self.fscore = self.depth + self.heuristic

    def getHeuristic(self):
        ''' example: U' from default (solved)
            RYB 000: PYB 100 (+0), RWB 110 (+1), RYG 001 (+0)
            PWG 011 (+1) target corner 111: RWG 010 (+1), PYG 101 (+0), PWB 111 (+1) 
            total: 4/4, 1 turn away, admissible!
        '''
        total_taxicab = -6.0 # -6 to account for neighbors needing to be 1 coordinate away from target (each absolute difference overcounts by 1 turn)
        for i in range(3): # RYB's (000) neighbors: PYB (100), RWB (010), RYG (001); only 1 coordinate should be different
            total_taxicab += abs(self.cube.blocks_tuple[0].coords[i]-self.cube.blocks_tuple[4].coords[i])
            total_taxicab += abs(self.cube.blocks_tuple[0].coords[i]-self.cube.blocks_tuple[2].coords[i])
            total_taxicab += abs(self.cube.blocks_tuple[0].coords[i]-self.cube.blocks_tuple[1].coords[i])
        target_corner_coords = []
        for coord in self.cube.blocks_tuple[7].coords: # deep copy of coords to avoid changing coordinates
            target_corner_coords.append(coord)
        for i in range(3): # need to move PWG into opposite corner
            if self.cube.blocks_tuple[7].coords[i] == self.cube.blocks_tuple[0].coords[i]:
                total_taxicab += 1
                target_corner_coords[i] = (target_corner_coords[i] + 1)%2 # flip to get destination coords
        for i in range(3): # PWG's (111) neighbors: RWG (011), PYG (101), PWB (110); only 1 coordinate should be different
            total_taxicab += abs(target_corner_coords[i]-self.cube.blocks_tuple[3].coords[i])
            total_taxicab += abs(target_corner_coords[i]-self.cube.blocks_tuple[5].coords[i])
            total_taxicab += abs(target_corner_coords[i]-self.cube.blocks_tuple[6].coords[i])
        return total_taxicab/4.0

    def act(self): # performs the chosen action on the cube
        if self.action != -1:
            action_map = {0: self.cube.frontCW, 5: self.cube.frontCCW, 1: self.cube.rightCW, 4: self.cube.rightCCW, 2: self.cube.topCW, 3: self.cube.topCCW}
            action_map[self.action]()
    
    def __repr__(self): # adding a string representation that will make printing out solutions easier
        return self.action
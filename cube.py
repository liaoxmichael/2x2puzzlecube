# Michael Liao
# CSC 372 Artificial Intelligence
# A1
''' Description:
    This file contains the Cube class which keeps track of all 8 distinct blocks
    as a list. It also handles the rotation moves on the cube (for each face) and
    other methods concerning the state of the cube, like whether it's solved,
    displaying the cube, scrambling it, and resetting it.
'''

import random # for scrambling
from block import Block # other class

class Cube:
    blocks = [] # stores 8 blocks

    def __init__(self): # creating 8 blocks and storing them
        self.reset()

    def reset(): # returning the cube to a solved state
        RWB = Block(0, 1, 0, 'R', 'W', 'B') # i 100% need to triple check this later
        RWB.setNeighbor(PWB, 'x')
        RWB.setNeighbor(RYB, 'y')
        RWB.setNeighbor(RWG, 'z')

        PWB = Block(1, 1, 0, 'P', 'W', 'B')
        PWB.setNeighbor(RWB, 'x')
        PWB.setNeighbor(PYB, 'y')
        PWB.setNeighbor(PWG, 'z')

        PWG = Block(1, 1, 1, 'P', 'W', 'G')
        PWG.setNeighbor(RWG, 'x')
        PWG.setNeighbor(PYG, 'y')
        PWG.setNeighbor(PWB, 'z')

        RWG = Block(0, 1, 1, 'R', 'W', 'G')
        RWG.setNeighbor(PWG, 'x')
        RWG.setNeighbor(RYG, 'y')
        RWG.setNeighbor(RWB, 'z')

        RYG = Block(0, 0, 1, 'R', 'Y', 'G')
        RYG.setNeighbor(PYG, 'x')
        RYG.setNeighbor(RWG, 'y')
        RYG.setNeighbor(RYB, 'z')

        PYG = Block(1, 0, 1, 'P', 'Y', 'G')
        PYG.setNeighbor(RYG, 'x')
        PYG.setNeighbor(PWG, 'y')
        PYG.setNeighbor(PYB, 'z')

        PYB = Block(1, 0, 0, 'P', 'Y', 'B')
        PYB.setNeighbor(RYB, 'x')
        PYB.setNeighbor(PWB, 'y')
        PYB.setNeighbor(PYG, 'z')

        RYB = Block(0, 0, 0, 'R', 'Y', 'B')
        RYB.setNeighbor(PYB, 'x')
        RYB.setNeighbor(RWB, 'y')
        RYB.setNeighbor(RYG, 'z')

        blocks = [RWB, PWB, PWG, RWG, RYG, PYG, PYB, RYB]

    def check(): # returns a boolean value determining if the cube is solved/not
        # might be able to do so by checking adjacent pieces? will need to test
        # otherwise a deep check where every attribute is compared & adjusted for
        # potential orientation shifts (cube that is solved but rotated along XY
        # plane should pass test!)
        return True or False 

    def scramble(k): # performs k quarter-turn moves on the cube to randomize it
        pass # remember to ensure that subsequent random moves don't directly undo prev move

    def display(): # possibly will use graphics library from CS1:
        # plan to add interactable buttons that will call methods here
        # essentially the GUI for a user to solve on
        pass

    '''
    The following 8 functions are rotations, concerning the face and whether it is
    clockwise (CW) or counter-clockwise (CCW). These are all quarter-turns. Implementation
    will be tricky, but as long as I check my math and assignments of neighbors/orientations
    /coordinates, it should turn out fine. There may be a formula I can follow to rotate points
    in 3D space – bears looking into to minimize human error.
    '''
    def frontCW():
        pass
    
    def frontCCW():
        pass

    def backCW():
        pass

    def backCCW():
        pass

    def rightCW():
        pass

    def rightCCW():
        pass

    def leftCW():
        pass

    def leftCCW():
        pass

    def topCW():
        pass

    def topCCW():
        pass

    def bottomCW():
        pass

    def bottomCCW():
        pass
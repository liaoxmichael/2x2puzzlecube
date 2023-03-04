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
from collections import Counter # allows for fast list equality checking, which I need to determine if solved
from block import Block # other class
#from sty import fg, rs # external module, to color console output (affects face characters)

class Cube:
    blocks = [] # stores 8 blocks
    actions = [] # stores all 12 action functions so can map integers 0-11
    blocks_tuple =(Block,)

    def __init__(self): # creating 8 blocks and storing them
        self.reset()

    def reset(self): # returning the cube to a solved state
        '''
        RWB = Block(0, 1, 0, 'R4', 'W3', 'B1') # used this to make sure stickers are aligned in display
        PWB = Block(1, 1, 0, 'P3', 'W4', 'B2')
        PWG = Block(1, 1, 1, 'P1', 'W2', 'G4')
        RWG = Block(0, 1, 1, 'R2', 'W1', 'G3')
        RYG = Block(0, 0, 1, 'R1', 'Y3', 'G1')
        PYG = Block(1, 0, 1, 'P2', 'Y4', 'G2')
        PYB = Block(1, 0, 0, 'P4', 'Y2', 'B4')
        RYB = Block(0, 0, 0, 'R3', 'Y1', 'B3')
        
        RWB = Block(0, 1, 0, fg.red + 'R' + fg.rs, fg.white + 'W' + fg.rs, fg.blue + 'B' + fg.rs)
        PWB = Block(1, 1, 0, fg.magenta + 'P' + fg.rs, fg.white + 'W' + fg.rs, fg.blue + 'B' + fg.rs)
        PWG = Block(1, 1, 1, fg.magenta + 'P' + fg.rs, fg.white + 'W' + fg.rs, fg.green + 'G' + fg.rs)
        RWG = Block(0, 1, 1, fg.red + 'R' + fg.rs, fg.white + 'W' + fg.rs, fg.green + 'G' + fg.rs)
        RYG = Block(0, 0, 1, fg.red + 'R' + fg.rs, fg.yellow + 'Y' + fg.rs, fg.green + 'G' + fg.rs)
        PYG = Block(1, 0, 1, fg.magenta + 'P' + fg.rs, fg.yellow + 'Y' + fg.rs, fg.green + 'G' + fg.rs)
        PYB = Block(1, 0, 0, fg.magenta + 'P' + fg.rs, fg.yellow + 'Y' + fg.rs, fg.blue + 'B' + fg.rs)
        RYB = Block(0, 0, 0, fg.red + 'R' + fg.rs, fg.yellow + 'Y' + fg.rs, fg.blue + 'B' + fg.rs)
        '''
        RWB = Block(0, 1, 0, 'R', 'W', 'B') # used this to make sure stickers are aligned in display
        PWB = Block(1, 1, 0, 'P', 'W', 'B')
        PWG = Block(1, 1, 1, 'P', 'W', 'G')
        RWG = Block(0, 1, 1, 'R', 'W', 'G')
        RYG = Block(0, 0, 1, 'R', 'Y', 'G')
        PYG = Block(1, 0, 1, 'P', 'Y', 'G')
        PYB = Block(1, 0, 0, 'P', 'Y', 'B')
        RYB = Block(0, 0, 0, 'R', 'Y', 'B')

        RWB.setNeighbors(PWB, RYB, RWG)
        PWB.setNeighbors(RWB, PYB, PWG)
        PWG.setNeighbors(RWG, PYG, PWB)
        RWG.setNeighbors(PWG, RYG, RWB)
        RYG.setNeighbors(PYG, RWG, RYB)
        PYG.setNeighbors(RYG, PWG, PYB)
        PYB.setNeighbors(RYB, PWB, PYG)
        RYB.setNeighbors(PYB, RWB, RYG)

        self.blocks = [RYB, RYG, RWB, RWG, PYB, PYG, PWB, PWG] # 000 001 010 011 100 101 110 111
        self.blocks_tuple = (RYB, RYG, RWB, RWG, PYB, PYG, PWB, PWG) # saving as tuple for checking
        # binary representation can also encode xyz coords

    '''
    check returns a boolean value determining if the cube is solved/not
    might be able to do so by checking adjacent pieces? will need to test
    otherwise a deep check where every attribute is compared & adjusted for
    potential orientation shifts (cube that is solved but rotated along XY
    plane should pass test!)
    '''
    def check(self): # NEW 03/04/23: need to check ALL cubelet's neighbors, so creating a dict and iterating thru it to ensure that neighbors are valid
        proper_neighbors = {
            self.blocks_tuple[0]: [self.blocks_tuple[4], self.blocks_tuple[2], self.blocks_tuple[1]],
            self.blocks_tuple[1]: [self.blocks_tuple[5], self.blocks_tuple[3], self.blocks_tuple[0]],
            self.blocks_tuple[2]: [self.blocks_tuple[6], self.blocks_tuple[0], self.blocks_tuple[3]],
            self.blocks_tuple[3]: [self.blocks_tuple[7], self.blocks_tuple[1], self.blocks_tuple[2]],
            self.blocks_tuple[4]: [self.blocks_tuple[0], self.blocks_tuple[6], self.blocks_tuple[5]],
            self.blocks_tuple[5]: [self.blocks_tuple[1], self.blocks_tuple[7], self.blocks_tuple[4]],
            self.blocks_tuple[6]: [self.blocks_tuple[2], self.blocks_tuple[4], self.blocks_tuple[7]],
            self.blocks_tuple[7]: [self.blocks_tuple[3], self.blocks_tuple[5], self.blocks_tuple[6]]
        }
        for block in self.blocks_tuple: # checks if neighbors are correct
            if Counter(block.neighbors) != Counter(proper_neighbors[block]):
                return False
            if block.faces[0] != block.neighbors[1].faces[0] or block.faces[0] != block.neighbors[2].faces[0]: # x faces should be same for yz neighbors
                #print(block.faces, " vs. y neighbor ", block.neighbors[1].faces, " and z neighbor ", block.neighbors[2].faces) # debug
                return False
            if block.faces[1] != block.neighbors[0].faces[1] or block.faces[1] != block.neighbors[2].faces[1]: # y faces should be same for xz neighbors
                #print(block.faces, " vs. x neighbor ", block.neighbors[0].faces, " and z neighbor ", block.neighbors[2].faces) # debug
                return False
            if block.faces[2] != block.neighbors[0].faces[2] or block.faces[2] != block.neighbors[1].faces[2]: # z faces should be same for xy neighbors
                #print(block.faces, " vs. x neighbor ", block.neighbors[0].faces, " and y neighbor ", block.neighbors[1].faces) # debug
                return False
        return True

    def scramble(self, k): # performs k quarter-turn moves on the cube to randomize it
        random_action = random.randint(0,11)
        for i in range(k):
            prev_action = random_action
            random_action = random.randint(0,11)
            while random_action == (prev_action + 6) % 12: # +6 % 12 is the u-turn move so we must avoid it
                random_action = random.randint(0,11)
            self.actions[random_action](self)
            #print(self.actions[random_action]) # debug code to make sure we're not getting u-turns

    def display(self): # for some reason graphics library won't run in vscode so: instead,
        # we should have a running menu in console that takes in data to run commands
        Bface = [['',''],['','']]
        Lface = [['',''],['','']]
        Uface = [['',''],['','']]
        Rface = [['',''],['','']]
        Fface = [['',''],['','']]
        Dface = [['',''],['','']]
        middle_faces = [Lface, Uface, Rface]
        for block in self.blocks:
            if block.coords[2] == 1: # face B
                Bface[block.coords[1]][block.coords[0]] = block.faces[2]
            if block.coords[0] == 0: # face L
                Lface[(block.coords[2]+1)%2][block.coords[1]] = block.faces[0]
            if block.coords[1] == 1: # face U
                Uface[(block.coords[2]+1)%2][block.coords[0]] = block.faces[1]
            if block.coords[0] == 1: # face R
                Rface[(block.coords[2]+1)%2][(block.coords[1]+1)%2] = block.faces[0]
            if block.coords[2] == 0: # face F
                Fface[(block.coords[1]+1)%2][block.coords[0]] = block.faces[2]
            if block.coords[1] == 0: # face D
                Dface[block.coords[2]][block.coords[0]] = block.faces[1]
        top = "    " + Bface[0][0] + ' ' + Bface[0][1] + '\n    ' + Bface[1][0] + ' ' + Bface[1][1] + '\n' 
        middle_top = ""
        middle_bottom = ""
        for face in middle_faces:
            for i in range(2):
                if i == 0:
                    middle_top += face[i][0] + ' ' + face[i][1] + ' '
                else:
                    middle_bottom += face[i][0] + ' ' + face[i][1] + ' '
        bottom = "    " + Fface[0][0] + ' ' + Fface[0][1] + '\n    ' + Fface[1][0] + ' ' + Fface[1][1] + '\n    ' + Dface[0][0] + ' ' + Dface[0][1] + '\n    ' + Dface[1][0] + ' ' + Dface[1][1] + '\n-----------' 
        print(top + middle_top + '\n' + middle_bottom + '\n' + bottom)
    
    def swapBlocks(self, pos1, pos2, pos3, pos4): # moves all the blocks around in the list by 4, takes in strings of binary representing positions in blocks and the cube
        temp = self.blocks[int(pos4,2)]
        self.blocks[int(pos4,2)] = self.blocks[int(pos3,2)]
        self.blocks[int(pos3,2)] = self.blocks[int(pos2,2)]
        self.blocks[int(pos2,2)] = self.blocks[int(pos1,2)]
        self.blocks[int(pos1,2)] = temp

    def updateNeighbors(self): # whenever a rotation is made, all cubelets must update adjacent blocks
        for block in self.blocks:
            newX = "{}{}{}".format((block.coords[0] + 1)%2, block.coords[1], block.coords[2])
            newY = "{}{}{}".format(block.coords[0], (block.coords[1] + 1)%2, block.coords[2])
            newZ = "{}{}{}".format(block.coords[0], block.coords[1], (block.coords[2] + 1)%2)
            block.setNeighbors(self.blocks[int(newX,2)], self.blocks[int(newY,2)], self.blocks[int(newZ,2)])
    '''
    The following 8 functions are rotations, concerning the face and whether it is
    clockwise (CW) or counter-clockwise (CCW). These are all quarter-turns.
    The comments indicate the order of coordinates being changed (and the standard puzzle cube notation for that turn).
    '''
    def frontCW(self): # 010 -> 110 -> 100 -> 000 -> 010 , F
        self.swapBlocks("010","110","100","000")
        for block in self.blocks:
            if block.coords[2] == 0: # face F
                if block.coords[0] == 0 and block.coords[1] == 1: # all neighbors are flipped bit!
                    block.setCoords(1,1,0)
                elif block.coords[0] == 1 and block.coords[1] == 1:
                    block.setCoords(1,0,0)
                elif block.coords[0] == 1 and block.coords[1] == 0:
                    block.setCoords(0,0,0)
                elif block.coords[0] == 0 and block.coords[1] == 0:
                    block.setCoords(0,1,0)
                block.swapFaces('x', 'y') # due to 90 deg rotation, xy swap on all cubelets moved
        self.updateNeighbors()
        
    def frontCCW(self): # 010 <- 110 <- 100 <- 000 <- 010, F'
        self.swapBlocks("000","100","110","010")
        for block in self.blocks:
            if block.coords[2] == 0: # face F
                if block.coords[0] == 0 and block.coords[1] == 1:
                    block.setCoords(0,0,0)
                elif block.coords[0] == 1 and block.coords[1] == 1:
                    block.setCoords(0,1,0)
                elif block.coords[0] == 1 and block.coords[1] == 0:
                    block.setCoords(1,1,0)
                elif block.coords[0] == 0 and block.coords[1] == 0:
                    block.setCoords(1,0,0)
                block.swapFaces('x', 'y') # due to 90 deg rotation, xy swap on all cubelets moved
        self.updateNeighbors()

    def backCW(self): # 011 -> 001 -> 101 -> 111 -> 011, B
        self.swapBlocks("011","001","101","111")
        for block in self.blocks:
            if block.coords[2] == 1: # face B
                if block.coords[0] == 0 and block.coords[1] == 1:
                    block.setCoords(0,0,1)
                elif block.coords[0] == 0 and block.coords[1] == 0:
                    block.setCoords(1,0,1)
                elif block.coords[0] == 1 and block.coords[1] == 0:
                    block.setCoords(1,1,1)
                elif block.coords[0] == 1 and block.coords[1] == 1:
                    block.setCoords(0,1,1)
                block.swapFaces('x', 'y') # due to 90 deg rotation, xy swap on all cubelets moved
        self.updateNeighbors()

    def backCCW(self): # 011 <- 001 <- 101 <- 111 <- 011, B'
        self.swapBlocks("111","101","001","011")
        for block in self.blocks:
            if block.coords[2] == 1: # face B
                if block.coords[0] == 0 and block.coords[1] == 1:
                    block.setCoords(1,1,1)
                elif block.coords[0] == 0 and block.coords[1] == 0:
                    block.setCoords(0,1,1)
                elif block.coords[0] == 1 and block.coords[1] == 0:
                    block.setCoords(0,0,1)
                elif block.coords[0] == 1 and block.coords[1] == 1:
                    block.setCoords(1,0,1)
                block.swapFaces('x', 'y') # due to 90 deg rotation, xy swap on all cubelets moved
        self.updateNeighbors()

    def rightCW(self): # 110 -> 111 -> 101 -> 100 -> 110, R
        self.swapBlocks("110","111","101","100")
        for block in self.blocks:
            if block.coords[0] == 1: # face R
                if block.coords[1] == 1 and block.coords[2] == 0:
                    block.setCoords(1,1,1)
                elif block.coords[1] == 1 and block.coords[2] == 1:
                    block.setCoords(1,0,1)
                elif block.coords[1] == 0 and block.coords[2] == 1:
                    block.setCoords(1,0,0)
                elif block.coords[1] == 0 and block.coords[2] == 0:
                    block.setCoords(1,1,0)
                block.swapFaces('y', 'z') # due to 90 deg rotation, yz swap on all cubelets moved
        self.updateNeighbors()

    def rightCCW(self): # 110 <- 111 <- 101 <- 100 <- 110, R'
        self.swapBlocks("100","101","111","110")
        for block in self.blocks:
            if block.coords[0] == 1: # face R
                if block.coords[1] == 1 and block.coords[2] == 0:
                    block.setCoords(1,0,0)
                elif block.coords[1] == 1 and block.coords[2] == 1:
                    block.setCoords(1,1,0)
                elif block.coords[1] == 0 and block.coords[2] == 1:
                    block.setCoords(1,1,1)
                elif block.coords[1] == 0 and block.coords[2] == 0:
                    block.setCoords(1,0,1)
                block.swapFaces('y', 'z') # due to 90 deg rotation, yz swap on all cubelets moved
        self.updateNeighbors()

    def leftCW(self): # 010 -> 000 -> 001 -> 011 -> 010, L
        self.swapBlocks("010","000","001","011")
        for block in self.blocks:
            if block.coords[0] == 0: # face L
                if block.coords[1] == 1 and block.coords[2] == 0:
                    block.setCoords(0,0,0)
                elif block.coords[1] == 0 and block.coords[2] == 0:
                    block.setCoords(0,0,1)
                elif block.coords[1] == 0 and block.coords[2] == 1:
                    block.setCoords(0,1,1)
                elif block.coords[1] == 1 and block.coords[2] == 1:
                    block.setCoords(0,1,0)
                block.swapFaces('y', 'z') # due to 90 deg rotation, yz swap on all cubelets moved
        self.updateNeighbors()

    def leftCCW(self): # 010 <- 000 <- 001 <- 011 <- 010, L'
        self.swapBlocks("011","001","000","010")
        for block in self.blocks:
            if block.coords[0] == 0: # face L
                if block.coords[1] == 1 and block.coords[2] == 0:
                    block.setCoords(0,1,1)
                elif block.coords[1] == 0 and block.coords[2] == 0:
                    block.setCoords(0,1,0)
                elif block.coords[1] == 0 and block.coords[2] == 1:
                    block.setCoords(0,0,0)
                elif block.coords[1] == 1 and block.coords[2] == 1:
                    block.setCoords(0,0,1)
                block.swapFaces('y', 'z') # due to 90 deg rotation, yz swap on all cubelets moved
        self.updateNeighbors()

    def topCW(self): # 010 -> 011 -> 111 -> 110 -> 010, U
        self.swapBlocks("010","011","111","110")
        for block in self.blocks:
            if block.coords[1] == 1: # face U
                if block.coords[0] == 0 and block.coords[2] == 0:
                    block.setCoords(0,1,1)
                elif block.coords[0] == 0 and block.coords[2] == 1:
                    block.setCoords(1,1,1)
                elif block.coords[0] == 1 and block.coords[2] == 1:
                    block.setCoords(1,1,0)
                elif block.coords[0] == 1 and block.coords[2] == 0:
                    block.setCoords(0,1,0)
                block.swapFaces('x', 'z') # due to 90 deg rotation, yz swap on all cubelets moved
        self.updateNeighbors()

    def topCCW(self): # 010 <- 011 <- 111 <- 110 <- 010, U'
        self.swapBlocks("110","111","011","010")
        for block in self.blocks:
            if block.coords[1] == 1: # face U
                if block.coords[0] == 0 and block.coords[2] == 0:
                    block.setCoords(1,1,0)
                elif block.coords[0] == 0 and block.coords[2] == 1:
                    block.setCoords(0,1,0)
                elif block.coords[0] == 1 and block.coords[2] == 1:
                    block.setCoords(0,1,1)
                elif block.coords[0] == 1 and block.coords[2] == 0:
                    block.setCoords(1,1,1)
                block.swapFaces('x', 'z') # due to 90 deg rotation, yz swap on all cubelets moved
        self.updateNeighbors()

    def bottomCW(self): # 000 -> 100 -> 101 -> 001 -> 000, D
        self.swapBlocks("000","100","101","001")
        for block in self.blocks:
            if block.coords[1] == 0: # face D
                if block.coords[0] == 0 and block.coords[2] == 0:
                    block.setCoords(1,0,0)
                elif block.coords[0] == 1 and block.coords[2] == 0:
                    block.setCoords(1,0,1)
                elif block.coords[0] == 1 and block.coords[2] == 1:
                    block.setCoords(0,0,1)
                elif block.coords[0] == 0 and block.coords[2] == 1:
                    block.setCoords(0,0,0)
                block.swapFaces('x', 'z') # due to 90 deg rotation, yz swap on all cubelets moved
        self.updateNeighbors()

    def bottomCCW(self): # 000 <- 100 <- 101 <- 001 <- 000, D'
        self.swapBlocks("001","101","100","000")
        for block in self.blocks:
            if block.coords[1] == 0: # face D
                if block.coords[0] == 0 and block.coords[2] == 0:
                    block.setCoords(0,0,1)
                elif block.coords[0] == 1 and block.coords[2] == 0:
                    block.setCoords(0,0,0)
                elif block.coords[0] == 1 and block.coords[2] == 1:
                    block.setCoords(1,0,0)
                elif block.coords[0] == 0 and block.coords[2] == 1:
                    block.setCoords(1,0,1)
                block.swapFaces('x', 'z') # due to 90 deg rotation, yz swap on all cubelets moved
        self.updateNeighbors()

    actions = [frontCW, backCW, rightCW, leftCW, topCW, bottomCW, frontCCW,  backCCW, rightCCW,  leftCCW, topCCW, bottomCCW] # list created to facilitate random scrambling

    def deepCopy(self):
        copy = Cube()
        copy.blocks_tuple = (self.blocks_tuple[0].deepCopy(), self.blocks_tuple[1].deepCopy(), self.blocks_tuple[2].deepCopy(), self.blocks_tuple[3].deepCopy(), self.blocks_tuple[4].deepCopy(), self.blocks_tuple[5].deepCopy(), self.blocks_tuple[6].deepCopy(), self.blocks_tuple[7].deepCopy())
        for block in copy.blocks_tuple:
            binary = ""
            for coord in block.coords:
                binary += str(coord)
            copy.blocks[int(binary,2)] = block
        copy.blocks[0].setNeighbors(copy.blocks[4], copy.blocks[2], copy.blocks[1])
        copy.blocks[1].setNeighbors(copy.blocks[5], copy.blocks[3], copy.blocks[0])
        copy.blocks[2].setNeighbors(copy.blocks[6], copy.blocks[0], copy.blocks[3])
        copy.blocks[3].setNeighbors(copy.blocks[7], copy.blocks[1], copy.blocks[2])
        copy.blocks[4].setNeighbors(copy.blocks[0], copy.blocks[6], copy.blocks[5])
        copy.blocks[5].setNeighbors(copy.blocks[1], copy.blocks[7], copy.blocks[4])
        copy.blocks[6].setNeighbors(copy.blocks[2], copy.blocks[4], copy.blocks[7])
        copy.blocks[7].setNeighbors(copy.blocks[3], copy.blocks[5], copy.blocks[6])
        
        return copy

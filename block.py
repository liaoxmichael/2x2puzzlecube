# Michael Liao
# CSC 372 Artificial Intelligence
# A1
''' Description:
    This file contains the Block class which keeps track of a single piece's
    attributes: its neighbors (adjacent pieces), coordinates (in an XYZ system, 
    ranging from (0,0,0) to (1,1,1)), and faces (always the same 3, but
    maintaining different orientations as the piece is rotated). It contains
    methods for setting those attributes.
'''
#####

class Block:
    neighbors = [-1, -1, -1] # default values so setNeighbor() does not have index OOB error
    coords = [] # possible values: 0 and 1, limit length 3
    faces = [] # represented by characters, first letter of color; can rearrange in list
               # but will always remain the same 3

    def __init__(self, x, y, z, faceX, faceY, faceZ): # instantiates with:
        coords = [x, y, z] # known position
        faces = [faceX, faceY, faceZ] # known orientation

    def setNeighbor(self, block, direction): # possible issues: this has no checks; i have to
        if direction == 'x':                 # make sure to check valid neighbor when calling
            direction = 0                    # rotation move
        elif direction == 'y':
            direction = 1
        elif direction == 'z':
            direction = 2
        self.neighbors[direction] = block

    def setCoords(self, x, y, z):
        coords = [x, y, z]
    
    def swapFaces(self, direction1, direction2): # when changing faces, swaps to maintain
        if direction1 == 'x':                   # the faces. per rotation only 2 will change
            direction1 = 0                      # orientation anyways (ex: perform frontCW() from
        elif direction1 == 'y':                 # solved. say our block is RWB: faces are ['R', 'W', 'B']
            direction1 = 1                      # after move, faces should now be ['W', 'R', 'B'].
        elif direction1 == 'z':
            direction1 = 2
        if direction2 == 'x':
            direction2 = 0
        elif direction2 == 'y': # there must be a better way to do this besides passing nums
            direction2 = 1      # note to self: try using ascii mapping, since xyz consecutive
        elif direction2 == 'z':
            direction2 = 2

        temp = self.coords[direction1] # the actual swap happens here
        self.coords[direction1] = self.coords[direction2]
        self.coords[direction2] = temp

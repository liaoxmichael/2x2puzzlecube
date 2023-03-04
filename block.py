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

class Block:
    neighbors = [] # default values so setNeighbor() does not have index OOB error
    coords = [] # possible values: 0 and 1, limit length 3
    faces = [] # represented by characters, first letter of color; can rearrange in list
               # but will always remain the same 3

    def __init__(self, x, y, z, faceX, faceY, faceZ): # instantiates with:
        self.coords = [x, y, z] # known position
        self.faces = [faceX, faceY, faceZ] # known orientation

    def setNeighbors(self, blockX, blockY, blockZ): 
        self.neighbors = [blockX, blockY, blockZ]

    def setCoords(self, x, y, z):
        self.coords = [x, y, z]

    '''
    swapFaces exists to align faces post-rotation. Each rotation will only change 2 faces on the cubelet.
    ex: perform frontCW() from solved. say our block is RWB: faces are ['R', 'W', 'B']
    after move, faces should now be ['W', 'R', 'B']. Directions are 'x', 'y', or 'z'.
    (a character, and since xyz are consecutive ASCII characters, we can use ord())
    This allows us to change adjacent cubelets.
    '''
    def swapFaces(self, direction1, direction2):
        direction1 = ord(direction1) - 120
        direction2 = ord(direction2) - 120
        temp = self.faces[direction1] # the actual swap happens here
        self.faces[direction1] = self.faces[direction2]
        self.faces[direction2] = temp                                  

    def deepCopy(self):
        copy = Block(self.coords[0], self.coords[1], self.coords[2], self.faces[0], self.faces[1], self.faces[2])
        # setNeighbors when outside?
        copy.setCoords(self.coords[0], self.coords[1], self.coords[2])
        return copy
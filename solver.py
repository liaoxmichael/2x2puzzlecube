# Michael Liao
# CSC 372 Artificial Intelligence
# A1
''' Description: 
    This file holds the IDA* solver of the cube, repeating 10 times on cubes
    scrambled with an increasing amount of moves (until the program fails to
    find a solution!). It relies on creating a Solver object, which takes in
    an instance of a Cube, and a file to write to. These are all specified
    for the trials ahead in main().
'''
from cube import Cube
from nodes import Node
import time # to assist in calculating time taken of algorithm in lab trials
class Solver:
    cube = Cube
    root = Node
    output_file = __file__

    def __init__(self, cube, output_file):
        self.output_file = output_file
        self.cube = cube
        self.root = Node(-1,None,0,cube) # instantiates with a root node in the tree
    
    def DLS(self, limit): # depth-limited search; should unfold until all children have f-scores greater than limit (float)
        i=0
        prev_best=1
        frontier = [self.root]
        while(i<prev_best):
            current = frontier.pop()
            if self.cube.check():
                self.output_file.write() # should write nodes visited 
                return current
            else:
                for j in range(6):
                    frontier.append(Node(j,current,current.depth+1,self.cube))

    def IDA(self): # IDA*, will call DLS repeatedly and increase limit to the best f-score of the previous iteration
        # should return a node with solved cube that can be traced along its parent-chain to find solution
        nodesVisited = 0 # will print this out before the function finishes
        pass
    
def main():
    result_file = open("results.txt", "w")
    start_states = [] # should store all the start states of cubes as we scramble them
    solutions = [] # should store all solution nodes found
    for i in range(100): # increasing complexity of scrambled cubes
        for j in range(10): # repeating 10 trials
            result_file.write() # indicate what complexity + trial # this is
            start = time.time_ns()
            newCube = Cube().scramble(i)
            start_states.append(newCube)
            solutions.append(Solver(newCube,result_file).IDA())
            end = time.time_ns() # time taken for a given trial will be end-start
            result_file.write() # print out time taken
    
    result_file.close()
    ''' # Earlier interactive menu code. Now unneccesary
    cube = Cube()
    print("Use standard cube notation to rotate cube clockwise (F, B, R, L, U, D).")
    print("Add a ' symbol (read: prime) to indicate counter-clockwise, and 2 to rotate twice.")
    print("Ex: F rotates the front face clockwise. F' rotates it counter-clockwise. F2 rotates it twice.")
    print("------")
    cube.display()
    print("Scrambling!")
    cube.scramble(10)
    choice = 0
    done = False
    while (choice != "-1" and done != True):
        cube.display()
        choice = input("-1 to exit.\n> ")
        print(menu(choice, cube))
        if(cube.check()):
            done = True
            print("Solved! Nicely done.")
        elif(choice != "-1"): 
            print("Still unsolved...")

def menu(choice, cube):
    match choice:
        case "-1":
            return "Bye!"
        case "F":
            cube.frontCW()
            return "Rotating F."
        case "F'":
            cube.frontCCW()
            return "Rotating F'."
        case "F2":
            cube.frontCW()
            cube.frontCW()
            return "Rotating F2."
        case "B":
            cube.backCW()
            return "Rotating B."
        case "B'":
            cube.backCCW()
            return "Rotating B'."
        case "B2":
            cube.backCW()
            cube.backCW()
            return "Rotating B2."
        case "L":
            cube.leftCW()
            return "Rotating L."
        case "L'":
            cube.leftCCW()
            return "Rotating L'."
        case "L2":
            cube.leftCW()
            cube.leftCW()
            return "Rotating L2."
        case "U":
            cube.topCW()
            return "Rotating U."
        case "U'":
            cube.topCCW()
            return "Rotating U'."
        case "U2":
            cube.topCW()
            cube.topCW()
            return "Rotating U2."
        case "D":
            cube.bottomCW()
            return "Rotating D."
        case "D'":
            cube.bottomCCW()
            return "Rotating D'."
        case "D2":
            cube.bottomCW()
            cube.bottomCW()
            return "Rotating D2."
        case _:
            return "I didn't understand that."
#main()
'''
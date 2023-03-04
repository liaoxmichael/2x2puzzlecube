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
from nodesNoHeuristic import Node
import time # to assist in calculating time taken of algorithm in lab trials
import math # to help in finding min_fscore
class Solver:
    cube = Cube
    output_file = __file__

    def __init__(self, cube, output_file):
        self.output_file = output_file
        self.cube = cube
    
    def DLS(self, limit): # depth-limited search; should unfold until all children have f-scores greater than limit (float)
        frontier = [Node(-1,None,0,self.cube)] # root node
        overflow = []
        nodes_expanded = 0
        while frontier != []:
            current = frontier.pop()
            if current.cube.check():
                return current, nodes_expanded, -1
            elif current.depth < limit:
                for j in range(6):
                    if current.action != 5-j: # because of symmetry in action_map, we can use 5-j to find the u-turn move
                        frontier.append(Node(j,current,current.depth+1,current.cube))
            else: # depth exceeds limit, want to generate children
                for j in range(6):
                    if current.action != 5-j: # because of symmetry in action_map, we can use 5-j to find the u-turn move
                        overflow.append(Node(j,current,current.depth+1,current.cube))
            nodes_expanded += 1
        min_fscore = math.inf
        for node in overflow:
            if node.fscore < min_fscore and node.fscore > limit:
                min_fscore = node.fscore
        return None, nodes_expanded, min_fscore # returning the best f-score that surpassed limit to use as new limit

    def IDA(self): # IDA* will call DLS repeatedly and increase limit to the best f-score of the previous iteration
        # should return a node with solved cube that can be traced along its parent-chain to find solution
        total_nodes_expanded = 0
        result = None
        new_limit = 1
        while result is None:
            result, nodes_expanded, new_limit = self.DLS(new_limit)
            total_nodes_expanded += nodes_expanded
        self.output_file.write(str(total_nodes_expanded) + ",")
        return result

def getSolution(solution=Node):
        solution = []
        action_map = {1: "frontCW", 2: "frontCCW", 3: "rightCW", 4: "rightCCW", 5: "topCW", 6: "topCCW"}
        traveler = solution
        while traveler.parent is not None:
            solution.append(action_map[traveler.action])
        result_string = ""
        for string in solution:
            result_string += string + " "

def main():
    result_file = open("resultsNoHeuristic.csv", "w")
    result_file.write("depth,nodes,time (ns)\n") # format as csv
    start_states = [] # should store all the start states of cubes as we scramble them
    solutions = [] # should store all solution nodes found
    # remember to set back to size 0
    for i in range(1,32): # increasing complexity of scrambled cubes; should be max depth 14, so this might be overkill, but just to be safe
        for j in range(10): # repeating 10 trials
            result_file.write(str(i) + ",")
            start = time.time_ns()
            newCube = Cube()
            newCube.scramble(i)
            start_states.append(newCube)
            result = Solver(newCube,result_file).IDA()
            solutions.append(result)
            end = time.time_ns() # time taken for a given trial will be end-start
            result_file.write(str(end-start) + "\n") # print out time taken
        result_file.write(",,\n") # add additional row for averaging w/ spreadsheet later
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
'''
main()
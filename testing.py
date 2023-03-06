from cube import Cube
from solver import Solver
import time
def main():
    result_file = open("test.csv", "a")
    result_file.write("depth,nodes,time (ns)\n") # format as csv
    result_file.close()
    start_states = [] # should store all the start states of cubes as we scramble them
    solutions = [] # should store all solution nodes found
    result_file = open("test.csv", "a")
    start = time.time_ns()
    newCube = Cube()
    newCube.scramble(10)
    start_states.append(newCube)
    solver = Solver(newCube,result_file)
    result = solver.IDA()
    solver.getSolution(result)
    solutions.append(result)
    end = time.time_ns() # time taken for a given trial will be end-start
    result_file.write(str(end-start) + "\n") # print out time taken
    result_file.close()
    result_file = open("test.csv", "a")
    result_file.write(",,\n") # add additional row for averaging w/ spreadsheet later
    result_file.close()
    
def printNeighbors(cube):
    for block in cube.blocks:
        for face in block.faces:
            print(face, end='')
        print(':', end=' ')
        for adj in block.neighbors:
            for face in adj.faces:
                print(face, end='')
            print(' ', end='')
        print()

def printBlocks(cube):
     for block in cube.blocks:
            for face in block.faces:
                print(face, end='')
            print()

main()
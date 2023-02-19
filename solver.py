# Michael Liao
# CSC 372 Artificial Intelligence
# A1
''' Description: 
    This file will eventually hold the IDA* algorithm we'll use to search
    through possible cube solves and find an optimal solution. For now, it holds
    a main function that enables user interaction through the terminal.
'''
import queue
from cube import Cube
class Solver:
    pass
    
def main():
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
main()
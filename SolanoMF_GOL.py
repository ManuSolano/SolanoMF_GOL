"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

ON = 255
OFF = 0
vals = [ON, OFF]
generations=0


def randomGrid(Nx, Ny):
    """returns a grid of Nx by Ny random values"""
    return np.random.choice(vals, Nx*Ny, p=[0.2, 0.8]).reshape(Nx, Ny)

def update(frameNum, img, grid, Nx, Ny):

    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    newGrid = grid.copy()


    # iterate over each cell in the grid
    for i in range(Nx):
        for j in range(Ny):
            # count the number of live neighbors
            neighbors = 0
            for ii in range(max(0, i-1), min(Nx, i+2)):
                for jj in range(max(0, j-1), min(Ny, j+2)):
                    if (ii, jj) != (i, j) and grid[ii, jj] == ON:
                        neighbors += 1
            
            # apply the rules of the game
            if grid[i, j] == ON and (neighbors < 2 or neighbors > 3):
                newGrid[i, j] = OFF
            elif grid[i, j] == OFF and neighbors == 3:
                newGrid[i, j] = ON


    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    global generations
    generations=generations-1
    if (generations==0):
        sys.exit()
    return img,


# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments
    global generations
    chose = False
    choice = input("Do you want to use a config file? (y/n): ")
    while chose !=True:
        if choice == "y" or choice == "Y":
            choice2 = int(input("Choose a number from 1 to 5: "))
            if choice2==1:
                with open('config1.csv', 'r') as f:
                    Ny, Nx = [int(x) for x in f.readline().split()]
                    generations = int(f.readline())
            if choice2==2:
                with open('config2.csv', 'r') as f:
                    Ny, Nx = [int(x) for x in f.readline().split()]
                    generations = int(f.readline())
            if choice2==3:
                with open('config3.csv', 'r') as f:
                    Ny, Nx = [int(x) for x in f.readline().split()]
                    generations = int(f.readline())
            if choice2==4:
                with open('config4.csv', 'r') as f:
                    Ny, Nx = [int(x) for x in f.readline().split()]
                    generations = int(f.readline())
            if choice2==5:
                with open('config5.csv', 'r') as f:
                    Ny, Nx = [int(x) for x in f.readline().split()]
                    generations = int(f.readline())

            chose=True
        elif choice == "n" or choice == "N":
            Nx = int(input("Set the value of the universe width: "))
            Ny = int(input("Set the value of the universe height: "))
            generations = int(input("Set number of generations: "))
            chose=True
        else:
            print("Invalid input")
        
        
    # set animation update interval
    updateInterval = 50

    # declare grid
    grid = np.array([])
    # populate grid with random on/off - more off than on
    grid = randomGrid(Nx, Ny)
    # Uncomment lines to see the "glider" demo
    #grid = np.zeros(Nx*Ny).reshape(Nx, Ny)
    #addGlider(1, 1, grid)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, Nx, Ny),
                              frames=10,
                              interval=updateInterval,
                              save_count=50)

    plt.show()

# call main
if __name__ == '__main__':
    main()
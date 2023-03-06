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

block = np.array ([ [0, 0, 0, 0],
                    [0, ON, ON, 0],
                    [0, ON, ON, 0],
                    [0, 0, 0, 0]])

boat1 = np.array ([ [0, 0, 0, 0, 0],
                    [0, ON, ON, 0, 0],
                    [0, ON, 0, ON, 0],
                    [0, 0, ON, 0, 0],
                    [0, 0, 0, 0, 0]])

boat2 = np.rot90(boat1)
boat3 = np.rot90(boat2)
boat4 = np.rot90(boat3)

tub = np.array ([   [0, 0, 0, 0, 0],
                    [0, 0, ON, 0, 0],
                    [0, ON, 0, ON, 0],
                    [0, 0, ON, 0, 0],
                    [0, 0, 0, 0, 0]])

blinkerV = np.array ([ [0, 0, 0, 0, 0],
                       [0, 0, ON, 0, 0],
                       [0, 0, ON, 0, 0],
                       [0, 0, ON, 0, 0],
                       [0, 0, 0, 0, 0]])

blinkerH = np.rot90(blinkerV)

glider1 = np.array ([ [0, 0, 0, 0, 0],
                      [0, 0, 0, ON, 0],
                      [0, ON, 0, ON, 0],
                      [0, 0, ON, ON, 0],
                      [0, 0, 0, 0, 0]])

glider2 = np.array ([ [0, 0, 0, 0, 0],
                      [0, ON, 0, 0, 0],
                      [0, 0, ON, ON, 0],
                      [0, ON, ON, 0, 0],
                      [0, 0, 0, 0, 0]])

glider3 = np.array ([ [0, 0, 0, 0, 0],
                      [0, 0, ON, 0, 0],
                      [0, 0, 0, ON, 0],
                      [0, ON, ON, ON, 0],
                      [0, 0, 0, 0, 0]])

glider4 = np.array ([ [0, 0, 0, 0, 0],
                      [0, ON, 0, ON, 0],
                      [0, 0, ON, ON, 0],
                      [0, 0, ON, 0, 0],
                      [0, 0, 0, 0, 0]])

glider5=np.rot90(glider1)
glider6=np.rot90(glider2)
glider7=np.rot90(glider3)
glider8=np.rot90(glider4)

glider9=np.rot90(glider5)
glider10=np.rot90(glider6)
glider11=np.rot90(glider7)
glider12=np.rot90(glider8)

glider13=np.rot90(glider9)
glider14=np.rot90(glider10)
glider15=np.rot90(glider11)
glider16=np.rot90(glider12)

spaceship1 = np.array([[0, 0, 0, 0, 0, 0, 0],
                       [0, ON, 0, 0, ON, 0, 0],
                       [0, 0, 0, 0, 0, ON, 0],
                       [0, ON, 0, 0, 0, ON, 0], 
                       [0, 0, ON, ON, ON, ON, 0], 
                       [0, 0, 0, 0, 0, 0, 0]])
                       
spaceship2 = np.array([[0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, ON, ON, 0, 0], 
                       [0, ON, ON, 0, ON, ON, 0], 
                       [0, ON, ON, ON, ON, 0, 0], 
                       [0, 0, ON, ON, 0, 0, 0], 
                       [0, 0, 0, 0, 0, 0, 0]])

spaceship3 = np.array([[0, 0, 0, 0, 0, 0, 0],
                       [0, 0, ON, ON, ON, ON, 0], 
                       [0, ON, 0, 0, 0, ON, 0],
                       [0, 0, 0, 0, 0, ON, 0], 
                       [0, ON, 0, 0, ON, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0]])

spaceship4 = np.array([[0, 0, 0, 0, 0, 0, 0],
                       [0, 0, ON, ON, 0, 0, 0], 
                       [0, ON, ON, ON, ON, 0, 0], 
                       [0, ON, ON, 0, ON, ON, 0], 
                       [0, 0, 0, ON, ON, 0, 0], 
                       [0, 0, 0, 0, 0, 0, 0]])

spaceship5=np.rot90(spaceship1)
spaceship6=np.rot90(spaceship2)
spaceship7=np.rot90(spaceship3)
spaceship8=np.rot90(spaceship4)

spaceship9=np.rot90(spaceship5)
spaceship10=np.rot90(spaceship6)
spaceship11=np.rot90(spaceship7)
spaceship12=np.rot90(spaceship8)

spaceship13=np.rot90(spaceship9)
spaceship14=np.rot90(spaceship10)
spaceship15=np.rot90(spaceship11)
spaceship16=np.rot90(spaceship12)

loaf1 = np.array([[0, 0, 0, 0, 0, 0],
                  [0, 0, ON, ON, 0, 0], 
                  [0, ON, 0, 0, ON, 0], 
                  [0, ON, 0, ON, 0, 0], 
                  [0, 0, ON, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0]])

loaf2 = np.rot90(loaf1)
loaf3 = np.rot90(loaf2)
loaf4 = np.rot90(loaf3)

beacon1 = np.array([[0, 0, 0, 0, 0, 0],
                   [0, ON, ON, 0, 0, 0], 
                   [0, ON, ON, 0, 0, 0], 
                   [0, 0, 0, ON, ON, 0], 
                   [0, 0, 0, ON, ON, 0], 
                   [0, 0, 0, 0, 0, 0]])

beacon2 = np.array([[0, 0, 0, 0, 0, 0],
                   [0, ON, ON, 0, 0, 0], 
                   [0, ON, 0, 0, 0, 0], 
                   [0, 0, 0, 0, ON, 0], 
                   [0, 0, 0, ON, ON, 0], 
                   [0, 0, 0, 0, 0, 0]])

beacon3 = np.rot90(beacon1)
beacon4 = np.rot90(beacon2)

toad1 = np.array([[0, 0, 0, 0, 0, 0],
                  [0, 0, 0, ON, 0, 0], 
                  [0, ON, 0, 0, ON, 0], 
                  [0, ON, 0, 0, ON, 0], 
                  [0, 0, ON, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0]])

toad2 = np.array([[0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0], 
                  [0, 0, ON, ON, ON, 0], 
                  [0, ON, ON, ON, 0, 0], 
                  [0, 0, 0, 0, 0, 0], 
                  [0, 0, 0, 0, 0, 0]])

toad3 = np.rot90(toad1)
toad4 = np.rot90(toad2)
toad5 = np.flip(toad1)
toad6 = np.flip(toad2)
toad7 = np.rot90(toad5)
toad8 = np.rot90(toad6)

beehive1 = np.array([[0, 0, 0, 0, 0, 0],
                     [0, 0, ON, ON, 0, 0], 
                     [0, ON, 0, 0, ON, 0], 
                     [0, 0, ON, ON, 0, 0], 
                     [0, 0, 0, 0, 0, 0]])

beehive2 = np.rot90(beehive1)

num_blocks = 0
num_boats = 0
num_blinkers = 0
num_beehives = 0
num_loafs = 0
num_toads = 0
num_tubs = 0
num_beacons = 0
num_gliders = 0
num_spaceships = 0

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
    ynInput = input("Do you want to use the values from 'map.csv'? (y/n): ")
    if ynInput == "y" or ynInput == "Y":
       with open('map.csv', 'r') as f:
            Ny, Nx = [int(x) for x in f.readline().split()]
            generations = int(f.readline())
    elif ynInput == "n" or ynInput == "N":
        Nx = int(input("Set the value of the universe width: "))
        Ny = int(input("Set the value of the universe height: "))
        generations = int(input("Set number of generations: "))
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
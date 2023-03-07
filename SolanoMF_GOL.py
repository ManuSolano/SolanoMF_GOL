"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from datetime import datetime
import time

ON = 255
OFF = 0
vals = [ON, OFF]
generations=0
currentGen=0
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

def setGrid(Ny, Nx, LiveCoords):
    tempGrid = np.random.choice([OFF, OFF], Ny*Nx, p=[0.2, 0.8]).reshape(Ny, Nx)
    for pair in LiveCoords:
        i, j = pair
        if i >= 0 and i < Ny and j >= 0 and j < Nx:
            tempGrid[i, j] = ON
    return tempGrid

def count_pattern(grid, pattern):
    count = 0
    for i in range(grid.shape[0] - pattern.shape[0] + 1):
        for j in range(grid.shape[1] - pattern.shape[1] + 1):
            if (grid[i:i+pattern.shape[0], j:j+pattern.shape[1]] == pattern).all():
                count += 1
                grid[i:i+pattern.shape[0], j:j+pattern.shape[1]] = -1
    return count

def count_blocks(grid):
    pattern = np.array([[ON, ON], [ON, ON]])
    return count_pattern(grid, pattern)

def count_beehives(grid):
    pattern1 = np.array([[OFF, ON, ON], [ON, OFF, ON]])
    pattern2 = np.array([[ON, OFF], [ON, ON], [OFF, ON]])
    count = count_pattern(grid, pattern1) + count_pattern(grid, pattern2)
    return count

def count_loafs(grid):
    pattern1 = np.array([[OFF, ON, ON], [ON, OFF, ON]])
    pattern2 = np.array([[ON, ON], [OFF, ON], [ON, OFF]])
    pattern3 = np.array([[ON, OFF], [ON, ON]])
    pattern4 = np.array([[ON, OFF], [ON, ON]])
    count = count_pattern(grid, pattern1) + count_pattern(grid, pattern2) + \
            count_pattern(grid, pattern3) + count_pattern(grid, pattern4)
    return count

def count_boats(grid):
    pattern = np.array([[ON, ON, OFF], [ON, OFF, ON], [OFF, ON, OFF]])
    return count_pattern(grid, pattern)

def count_tubs(grid):
    pattern = np.array([[OFF, ON, OFF], [ON, OFF, ON], [OFF, ON, OFF]])
    return count_pattern(grid, pattern)

def count_blinkers(grid):
    pattern1 = np.array([[OFF, ON, OFF], [OFF, ON, OFF], [OFF, ON, OFF]])
    pattern2 = np.array([[OFF, OFF, OFF], [ON, ON, ON], [OFF, OFF, OFF]])
    count = count_pattern(grid, pattern1) + count_pattern(grid, pattern2)
    return count

def count_toads(grid):
    pattern1 = np.array([[OFF, OFF, OFF, OFF], [OFF, ON, ON, ON], [ON, ON, ON, OFF], [OFF, OFF, OFF, OFF]])
    pattern2 = np.array([[OFF, OFF, ON, OFF], [ON, OFF, OFF, ON], [ON, OFF, OFF, ON], [OFF, ON, OFF, OFF]])
    count = count_pattern(grid, pattern1) + count_pattern(grid, pattern2)
    return count

def count_beacons(grid):
    pattern1 = np.array([[ON, ON, OFF, OFF], [ON, ON, OFF, OFF], [OFF, OFF, ON, ON], [OFF, OFF, ON, ON]])
    pattern2 = np.array([[ON, ON, OFF, OFF], [ON, OFF, OFF, OFF], [OFF, OFF, OFF, ON], [OFF, OFF, ON, ON]])
    count = count_pattern(grid, pattern1) + count_pattern(grid, pattern2)
    return count

def count_gliders(grid):
    pattern1 = np.array([[OFF, ON, OFF], [OFF, OFF, ON], [ON, ON, ON]])
    pattern2 = np.array([[ON, OFF, ON], [OFF, ON, ON], [OFF, ON, OFF]])
    pattern3 = np.array([[OFF, OFF, ON], [ON, OFF, ON], [OFF, ON, ON]])
    pattern4 = np.array([[ON, OFF, OFF], [OFF, ON, ON], [ON, ON, OFF]])
    count = count_pattern(grid, pattern1) + count_pattern(grid, pattern2) + \
            count_pattern(grid, pattern3) + count_pattern(grid, pattern4)
    return count

def count_spaceships(grid):
    pattern1 = np.array([[ON, OFF, OFF, ON, OFF], [OFF, OFF, OFF, OFF, ON], [ON, OFF, OFF, OFF, ON], [OFF, ON, ON, ON, ON], [OFF, OFF, OFF, OFF, OFF] ])
    pattern2 = np.array([[OFF, OFF, OFF, OFF, OFF], [OFF, OFF, ON, ON, OFF], [ON, ON, OFF, ON, ON], [ON, ON, ON, ON, OFF], [OFF, ON, ON, OFF, OFF] ])
    pattern3 = np.array([[OFF, OFF, OFF, OFF, OFF], [OFF, ON, ON, ON, ON], [ON, OFF, OFF, OFF, ON], [OFF, OFF, OFF, OFF, ON], [ON, OFF, OFF, ON, OFF] ])
    pattern4 = np.array([[OFF, ON, ON, OFF, OFF], [ON, ON, ON, ON, OFF], [ON, ON, OFF, ON, ON], [OFF, OFF, ON, ON, OFF], [OFF, OFF, OFF, OFF, OFF] ])
    count = count_pattern(grid, pattern1) + count_pattern(grid, pattern2) + \
            count_pattern(grid, pattern3) + count_pattern(grid, pattern4)
    return count

def update(frameNum, img, grid, Nx, Ny,choice2):

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
    global num_blocks
    global num_boats
    global num_blinkers 
    global num_beehives 
    global num_loafs 
    global num_toads 
    global num_tubs 
    global num_beacons 
    global num_gliders 
    global num_spaceships

    num_blocks=num_blocks+count_blocks(grid)
    num_beehives=num_beehives+count_beehives(grid)
    num_loafs = num_loafs + count_loafs(grid)
    num_boats = num_boats + count_boats(grid)
    num_tubs = num_tubs + count_tubs(grid)
    num_blinkers = num_blinkers + count_blinkers(grid)
    num_toads=num_toads+count_toads(grid)
    num_beacons=num_beacons+count_beacons(grid)
    num_gliders=num_gliders+count_gliders(grid)
    num_spaceships=num_spaceships+count_spaceships(grid)
    total = num_blocks + num_boats + num_blinkers + num_beehives + num_loafs + num_toads + num_tubs + num_beacons + num_gliders + num_spaceships
    if total==0:
        total=1
    # update data
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    global currentGen
    currentGen=currentGen+1

    if choice2==0:
        num="MANUAL"
    elif choice2>0:
        num=choice2
    with open(f"output{num}.txt", "a") as file:
        
        file.write(f"..........Iteration {currentGen} ...........\n") 
        file.write(f"......................................\n") 
        file.write(f"Structure       Count       Percentage\n") 
        file.write(f"......................................\n") 
        file.write("{:<12}{:>10}{:>10}\n".format("Blocks", num_blocks, "{:.1f}".format((num_blocks*100)/total)))
        file.write("{:<12}{:>10}{:>10}\n".format("Beehives", num_beehives, "{:.1f}".format((num_beehives*100)/total)))
        file.write("{:<12}{:>10}{:>10}\n".format("Loafs", num_loafs, "{:.1f}".format((num_loafs*100)/total)))
        file.write("{:<12}{:>10}{:>10}\n".format("Boats", num_boats, "{:.1f}".format((num_boats*100)/total)))
        file.write("{:<12}{:>10}{:>10}\n".format("Tubs", num_tubs, "{:.1f}".format((num_tubs*100)/total)))
        file.write("{:<12}{:>10}{:>10}\n".format("Blinkers", num_blinkers, "{:.1f}".format((num_blinkers*100)/total)))
        file.write("{:<12}{:>10}{:>10}\n".format("Toads", num_toads, "{:.1f}".format((num_toads*100)/total)))
        file.write("{:<12}{:>10}{:>10}\n".format("Beacons", num_beacons, "{:.1f}".format((num_beacons*100)/total)))
        file.write("{:<12}{:>10}{:>10}\n".format("Gliders", num_gliders, "{:.1f}".format((num_gliders*100)/total)))
        file.write("{:<12}{:>10}{:>10}\n".format("Spaceships", num_spaceships, "{:.1f}".format((num_spaceships*100)/total)))
        file.write(f"......................................\n")
        file.write(f"Total              {total}\n") 
        file.write(f"......................................\n")
        file.write("\n")
    file.close()
    print(currentGen)
    if (currentGen==generations):
        time.sleep(1)
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
    
    while True:
        choice = input("Do you want to use a config file? (y/n): ")
        if choice == "y" or choice == "Y":
            while True:
                try:
                    choice2 = int(input("Choose a number from 1 to 5: "))
                    if choice2 < 1 or choice2 > 5:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter a number from 1 to 5.")

            with open(f'config{choice2}.csv', 'r') as f:
                    Ny, Nx = [int(x) for x in f.readline().split()]
                    generations = int(f.readline())
                    lines = f.readlines()[2:]  # slice the list to start from the third line
                    LiveCoords = [[int(x) for x in line.split()] for line in lines]
            grid=np.array([])
            grid=setGrid(Nx,Ny, LiveCoords)
            file = open(f"output{choice2}.txt", "w", encoding='utf-8')
            file.write(f"simulation at {datetime.today().strftime('%Y-%m-%d')}\n") 
            file.write(f"Universe size {Ny} x {Nx}\n")
            file.write("\n") 
            file.write(f"......................................\n") 
            break
        elif choice == "n" or choice == "N":
            Nx = int(input("Set the value of the universe width: "))
            Ny = int(input("Set the value of the universe height: "))
            generations = int(input("Set number of generations: "))
            grid = np.array([])
            grid = randomGrid(Nx, Ny)
            choice2=0
            file = open(f"outputMANUAL.txt", "w", encoding='utf-8')
            file.write(f"simulation at {datetime.today().strftime('%Y-%m-%d')}\n") 
            file.write(f"Universe size {Ny} x {Nx}\n")
            file.write(f"Total Generations: {generations}\n")
            file.write("\n") 
            file.write(f"......................................\n") 
            break
        else:
            print("Invalid input")
        
        
    # set animation update interval
    updateInterval = 5

    # declare grid
    
    # populate grid with random on/off - more off than on
    
    # Uncomment lines to see the "glider" demo
    #grid = np.zeros(Nx*Ny).reshape(Nx, Ny)
    #addGlider(1, 1, grid)

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, Nx, Ny,choice2),
                              frames=10,
                              interval=updateInterval,
                              save_count=50)

    plt.show()

# call main
if __name__ == '__main__':
    main()
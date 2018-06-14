import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

## This code was adapted from the book Python Playground.
## by Mahesh Venkitachalam
## nostarch.com

## The code has been drasticly shortened for a summer camp.

ON = 255
OFF = 0

def update(frameNum, img, grid, N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = (  grid[(i-1)%N,(j-1)%N]
                    + grid[(i-1)%N,j]
                    + grid[(i-1)%N,(j+1)%N]
                    + grid[i,(j-1)%N]
                    + grid[i,(j+1)%N]
                    + grid[(i+1)%N,(j-1)%N]
                    + grid[(i+1)%N,j]
                    + grid[(i+1)%N,(j+1)%N])/255

            if grid[i,j] == ON and (total < 2 or total > 3):
                newGrid[i,j] = OFF
            elif grid[i,j] == OFF and total == 3:
                newGrid[i,j] = ON

    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,

def main():
    N = 100
    grid = np.random.choice([OFF,ON], (N, N))

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig, update,
                                  fargs=(img, grid, N, ),
                                  frames=1000,
                                  save_count=50)
    plt.show()

main()

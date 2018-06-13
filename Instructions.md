% Conway's Game Of Life

## Preparing for Conway

You will need to install some special software for today's lesson.

1. Find the search bar on your computer.
2. Type "cmd".
3. At the command prompt, run "py -m pip install matplotlib".
4. If you get any error messages, please raise your hand for us to help.

## 2D Lists

In this lecture, you will need to understand two-dimensional list.

## 1D Lists

- A list is considered one-dimensional.
    - It represents a sequence of elements.
    - There's a first element.
    - There's a last element.
    - The list has a number of elements.
    - You can index those elements using square brackets.

## 2D Lists

    8 6 7
    5 3 0
    9 4 6

This is a grid of elements. Like 1D lists, you can index into the list but now we need two indices. The first index is always the row. The second index is the column.

## 2D Lists

    8 6 7
    5 3 0
    9 4 6

The number 8 appears in the first row and the first column, so we say that its location is at "0,0". The row comes first and the column comes second. Computer scientists begin counting with 0!

## 2D Lists

    8 6 7
    5 3 0
    9 4 6

The number 6 appears in the first row and the second column, so we say that its location is at "0,1".

## 2D Lists

    8 6 7
    5 3 0
    9 4 6

The number 5 appears in the second row and the first column, so we say that its location is at "1,0".

## 2D Lists

    8 6 7
    5 3 0
    9 4 6

- What is the location of 3?
- What is the location of 0?
- What is the location of 4?
- What is the location of 6?

## 2D Lists

    8 6 7
    5 3 0
    9 4 6

- What is the location of 3? (1,1)
- What is the location of 0? (1,2)
- What is the location of 9? (2,0)
- What is the location of 6? (2,2)

## 2D Lists

- A 2D list is considered two-dimensional.
    - It represents a grid of elements.
    - It has both rows and columns.
    - The number of elements in the list is the rows times the columns.
    - You need two indices to index into the list.

## Numpy

We use a special library for two dimensional lists named "numpy". Start up Idle and type this:

    import numpy as np

"np" is the common shorthand for "numpy". "numpy" is used by scientists for manipulating large datasets.

## Creating a 2D list

This is the grid that we used in our examples. Type this line. Here, we define an array with 3 rows and 3 columns. We define them one **row** at a time.

    x = np.array([[8, 6, 7], [5, 3, 0], [9, 4, 6]])

## Check our work.

Now we can check our work from earlier.

    x[1,1]
    x[1,2]
    x[2,0]
    x[2,2]

## Overwriting values.

We can overwrite values in a 2D list using this approach.

    x[2,2] = 42
    x

## Let's visualize.

Numbers are fun, but visualizations are more fun. Make sure that you have all of the following libraries imported. You should already have the first one.

    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation

## Let's visualize.

In this example, the elements equal to 255 represent "ON" elements and the ones with 0 represent "OFF".

    x = np.array([[0, 0, 255], [255, 255, 0], [0, 255, 0]])
    plt.imshow(x, interpolation='nearest')
    plot.show()

What colors does python assign to "ON" and "OFF" using this approach?

## Let's make more!

This will make a 400 by 400 grid with a randomly chosen value (0 or 255) for each element. How many elements are in the grid?

    width = 400
    height = 400
    x = np.random.choice([0,255], (width, height))
    plt.imshow(x, interpolation='nearest')
    plt.show()

## Conway's Game of Life

Conway's Game of Life simulates the people in your life.

- A typical person needs friends.
- If you have too few friends, you get lonely.
- If you have too many friends, you get overcrowded.

In this program, each element in a 2D list represents either a living person or an empty cell. RED means living. BLUE means empty.

## Conway's Game of Life

A man by the name of John Conway wanted to simulate life using a simple set of rules. Here are all four rules which we will program.

- If a cell is living but has fewer than two friends, it dies of loneliness.
- If a cell is living and has two or three friends, it continues to live.
- If a cell is living but has more than three friends, it dies of being overcrowded.
- If a cell is empty and has exactly three friends, a person is born at that location.

In this simulation, 255 means living and 0 means empty.

## How many friends do you have?

In order to determine how many friends an element has, we count the neighbors.

    (i-1, j-1)    (i-1, j)    (i-1, j+1)
    (i, j-1)      (i, j)      (i, j+1)
    (i+1, j-1)    (i+1, j)    (i+1, j+1)

In order to count the neighbors of an element, we count how many of the 8 cells surrounding a cell that are equal to 255. In a 3 by 3 grid, a cell has up to 8 neighbors.

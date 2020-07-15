import numpy as np
import random as rndm
import state


DIMX = 25
DIMY = 25


def create_ord_list(wlist):
    retlist = []
    temp_list = []
    for words in wlist:
        for letters in words:
            temp_list.append(ord(letters))
        retlist.append(temp_list)
        temp_list.clear()
    return retlist


def check_coords(grid_state, entry_list, ords):
    for i in range(0, entry_list):
        x_coord = entry_list[i][0]
        y_coord = entry_list[i][1]
        if grid_state[x_coord][y_coord] != 0 and ords[i] != grid_state[x_coord][y_coord]:
            return False
    return True

# word: number value list attruibuted to word.
# grid: the grid
# cross_coord: the starting coordinate where the letter at the "start_indice" of "word", will first be placed
# orientation (tuple): (x,y) +/- 1 in x/y defines the direction ex: (1,1) start to stop of the word heads in the
# positive increment of the matrix

def place_word(word, grid, cross_coord, start_indice, orientation):

    grid[cross_coord[0]][cross_coord[1]] = word[start_indice]
    wordlen = len(word)

    xinc_r = 1
    yinc_r = 1
    for i in range(start_indice, wordlen):
        grid[cross_coord[0] + xinc_r * orientation[0]][cross_coord[1] + yinc_r * orientation[1]] = word[i]
        xinc_r = xinc_r + 1
        yinc_r = yinc_r + 1

    xinc_l = 1
    yinc_l = 1
    for i in range(start_indice, 0, -1):
        grid[cross_coord[0] + xinc_l * -orientation[0]][cross_coord[1] + yinc_l * -orientation[1]] = word[i]

    return grid


def solve(numnum_list, grid):
    """
    IDEA 1: (iterative with comparision?)
    make a number of random states of the board where we initially place a random word in a random spot on the board.

    generate a state for all possible ways to cross a random word with the word placed.

    for each of those states, keep doing that until there are no more words or the solution becomes impossible.

    choose the best

    IDEA 2: (Bi-Directional Linked list)
    Change the words into objects in which every letter has a link to another word's
    letter where they cross.

    Bi-Directional Linked list cross-word (seems like a nightmare to maintain)?
    Caveat: We dont have to worry about storing them in a matrix.

    Argument against it: Its still good to worry about the overal dimension of the
    crossword (using a matrix to store them inherently makes you worry bout that)
     + doing it this way, would make it a nightmare to print this information
    so that I could actually understand what it generated.

    IDEA 3:

    Idea 2 but where all letters start as being linked to every other letter that is the same.
    We trim the links down to a 2-D space, where the solution with the most connections is the best solution.
    !!!!!!!!!!!!!!!!! THIS WONT WORK AS IT DOESNT CONSIDER 3D SPACE !!!!!!!!!!!!!!!!!!!!!!!!!!

    """
    # idea 1:

    numnum_list
    rand_dimx = rndm.randint(0, DIMX)
    rand_dimy = rndm.randint(0, DIMY)
    rand_start_coords = [rand_dimx, rand_dimy]
    rand_word

    for



    for

    binChoice = rndm.randint(0, 1)





binary = open("..\crosswords.txt")
text = binary.read()
word_list = text.split(",")
ord_list = create_ord_list(word_list)

grid = np.zeros((DIMX, DIMY))

output_matrix = solve(ord_list, grid)
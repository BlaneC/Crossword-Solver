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


def solve(numnum_list):
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

    """

    binChoice = rndm.randint(0, 1)





binary = open("..\crosswords.txt")
text = binary.read()
word_list = text.split(",")
ord_list = create_ord_list(word_list)

grid = np.zeros((DIMX, DIMY))


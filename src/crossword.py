import numpy as np


class State:
    grid = -1
    score = 0
    word_coordinates = -1

    def __init__(self, grid):
        self.grid = grid
        score = gridScorer(grid)

    def update_score(self):
        self.score = gridScorer(self.grid)


# best cross word will use the least tiles. Tiles used will have a value > 0 in them
def gridScorer(grid):
    score = 0
    for xlist in grid:
        for y in xlist:
            if y > 0:
                score = score + 1
    return score


def create_ord_list(wlist):
    retlist = []
    temp_list = []
    for words in wlist:
        for letters in words:
            temp_list.append(ord(letters))
        retlist.append(temp_list)
        temp_list.clear()
    return retlist


def solve(numnum_list):
    
    for




binary = open("..\crosswords.txt")
text = binary.read()
word_list = text.split(",")
ord_list = create_ord_list(word_list)



np.zeros((25, 25))


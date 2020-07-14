

class State:
    grid = -1
    score = 0
    word_coordinates = -1

    def __init__(self, grid):
        self.grid = grid
        score = grid_scorer(grid)

    def update_score(self):
        self.score = grid_scorer(self.grid)


# best cross word will use the least tiles. Tiles used will have a value > 0 in them
def grid_scorer(grid):
    score = 0
    for xlist in grid:
        for y in xlist:
            if y > 0:
                score = score + 1
    return score
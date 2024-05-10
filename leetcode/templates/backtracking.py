def is_valid_state(state):
    # is this a valid solution?
    return True


def get_candidates(state):
    res = []
    # get list of candidates off state/paramaters
    return res


def search(state, solutions):
    pass


def solve():
    solutions = []
    state = set()
    search(state, solutions)
    return solutions


class Backtracking:
    def __init__(self):
        self.solutions = []
        self.state = set()

    def is_valid_state(self):
        self.state
        return True

    def get_candidates(self):
        res = []
        self.state
        return res

    def search(self):
        if self.is_valid_state():
            self.solutions.append(self.state.copy())
            return

        for c in get_candidates:
            self.state.add(c)
            self.search()
            self.state.remove(c)

    def solve(self):
        self.search()
        return self.solutions

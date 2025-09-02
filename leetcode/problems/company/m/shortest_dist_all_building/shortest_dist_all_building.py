"""


BFS:
    We store the MIN distance to point (i,j) from target (ti,tj)
    We find the point which has the min sum of all points.


"""

SPACE = 0
HOUSE = 1
ROCK = 2


class Solution:
    def __init__(self):
        pass

    def shortest_distance(self, grid: list):
        target_list = self._get_target_list(grid)
        space_memo = self._get_memo(grid)

        for target in target_list:
            ti, tj = target
            # target coord, distance so far from target coord.
            que = [((ti, tj), 0)]
            self.bfs(que, space_memo)

    def bfs(self, que, memo):
        while que:
            i, j = que.pop()

    def _get_memo(self, grid, target_list):
        memo = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == SPACE:
                    memo[(i, j)] = {target: 0 for target in target_list}
        return memo

    def _get_target_list(self, grid):
        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == HOUSE:
                    res += [(i, j)]
        return res

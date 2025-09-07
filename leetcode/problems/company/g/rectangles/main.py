"""
List of rectangles

[
    [width, length],
     [width, length],
      [width, length],
       [width, length],
        [width, length],
]

Return the rectangles that make the maximum number of rectangles stacked,
If a rectangle below is greater in both LENGTH AND WIDTH.

TC: O(2**n * nlog(n) -> bt O(n * n logn) -> O(n**2)
SC: O(Acceptable rectangle list)
"""

from dataclasses import dataclass
import unittest


@dataclass
class State:
    rectangle_list: list
    solution: list
    res: list


class Solution:
    def is_valid_sol(self, state):
        # Only consider updating when current solution is longer than best
        if len(state.solution) <= len(state.res):
            return False
        prev = [float("-inf"), float("-inf")]
        for el in state.solution:
            if not (prev[0] < el[0] and prev[1] < el[1]):
                return False
            prev = el
        return True

    def get_candidates(self, state, i):
        # Not used in the fixed backtracking, kept for compatibility
        return state.rectangle_list[i:]

    def solve(self, state, i):
        # At the end of the array, consider updating best
        if i >= len(state.rectangle_list):
            if self.is_valid_sol(state):
                state.res = state.solution[::]
            return

        # Option 1: skip current rectangle
        self.solve(state, i + 1)

        # Option 2: include current rectangle if it keeps strict increase
        cur = state.rectangle_list[i]
        if not state.solution or (state.solution[-1][0] < cur[0] and state.solution[-1][1] < cur[1]):
            state.solution.append(cur)
            self.solve(state, i + 1)
            state.solution.pop()

    def rectangle_thing(self, rectangle_list):
        # Sort to allow reordering for stacking consideration
        sorted_rects = sorted(rectangle_list, key=lambda x: (x[0], x[1]))
        solution = []
        res = []
        state = State(sorted_rects, solution, res)
        self.solve(state, 0)
        return state.res


class TestRectangle(unittest.TestCase):
    def test_empty_input(self):
        s = Solution()
        rectangle_list = []
        expected = []
        actual = s.rectangle_thing(rectangle_list)
        self.assertEqual(expected, actual)

    def test_simple_increasing_chain(self):
        # All rectangles can stack: strictly increasing width and length
        s = Solution()
        rectangle_list = [
            [1, 1],
            [2, 2],
            [3, 3],
        ]
        expected = [
            [1, 1],
            [2, 2],
            [3, 3],
        ]
        actual = s.rectangle_thing(rectangle_list)
        self.assertEqual(expected, actual)

    def test_mixed_requires_selection(self):
        # Choose a maximal chain from an unsorted set
        s = Solution()
        rectangle_list = [
            [5, 4],
            [6, 4],  # cannot go above [5,4] because length equal (4)
            [6, 7],
            [2, 3],
        ]
        # Max stack (strictly increasing both dims): [2,3] -> [5,4] -> [6,7]
        expected = [
            [2, 3],
            [5, 4],
            [6, 7],
        ]
        actual = s.rectangle_thing(rectangle_list)
        self.assertEqual(expected, actual)

    def test_equal_dimension_blocks_stack(self):
        # Equal width or length should not count as stackable (strictly greater required)
        s = Solution()
        rectangle_list = [
            [3, 3],
            [3, 4],  # width equal to 3, length greater - cannot be stacked on [3,3] since width not greater
            [4, 5],
        ]
        # Max chain length is 2. Either [3,3]->[4,5] or [3,4]->[4,5]
        expected_options = [
            [[3, 3], [4, 5]],
            [[3, 4], [4, 5]],
        ]
        actual = s.rectangle_thing(rectangle_list)
        self.assertIn(actual, expected_options)

    def test_with_duplicates(self):
        # Duplicates should not artificially increase chain length
        s = Solution()
        rectangle_list = [
            [2, 3],
            [2, 3],
            [3, 4],
        ]
        expected = [
            [2, 3],
            [3, 4],
        ]
        actual = s.rectangle_thing(rectangle_list)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()

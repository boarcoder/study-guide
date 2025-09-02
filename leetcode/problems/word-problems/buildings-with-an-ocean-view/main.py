'''
https://foolishhungry.com/buildings-with-an-ocean-view/

- There are n buildings in a line. You are given an integer array heights of size n that represents the heights of the buildings in the line.
- The ocean is to the right of the buildings. A building has an ocean view if the building can see the ocean without obstructions. 
- Formally, a building has an ocean view if all the buildings to its right have a smaller height.
- Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.
[M] 15m Time limit: Pass
TC: O(N)
SC: O(h)
'''

def buildings_ocean_view(heights: list[int]) -> list[int]:
    res = []
    max_h = 0
    for i in range(len(heights) - 1, -1, -1):
        height = heights[i]
        if height > max_h:
            max_h = height
            res += [i]
    res.reverse()
    return res




import unittest

class TestBuildingsOceanView(unittest.TestCase):
    
    def test_mixed_heights(self):
        """Test case with mixed building heights"""
        heights = [4, 2, 3, 1]
        expected = [0, 2, 3]
        self.assertEqual(buildings_ocean_view(heights), expected)
    
    def test_decreasing_heights(self):
        """Test case where all buildings have ocean view (decreasing heights)"""
        heights = [4, 3, 2, 1]
        expected = [0, 1, 2, 3]
        self.assertEqual(buildings_ocean_view(heights), expected)
    
    def test_increasing_heights(self):
        """Test case where only the rightmost building has ocean view (increasing heights)"""
        heights = [1, 2, 3, 4]
        expected = [3]
        self.assertEqual(buildings_ocean_view(heights), expected)
    
    def test_single_building(self):
        """Test case with a single building"""
        heights = [5]
        expected = [0]
        self.assertEqual(buildings_ocean_view(heights), expected)
    
    def test_empty_input(self):
        """Test case with empty input"""
        heights = []
        expected = []
        self.assertEqual(buildings_ocean_view(heights), expected)
    
    def test_same_height_buildings(self):
        """Test case where some buildings have the same height"""
        heights = [1, 3, 2, 4, 2, 2]
        expected = [3, 5]
        self.assertEqual(buildings_ocean_view(heights), expected)


if __name__ == "__main__":
    unittest.main()
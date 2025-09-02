"""
Unit tests for the min_cost_trip function.
Tests various scenarios including edge cases, normal cases, and error conditions.
"""

import os
import sys
import unittest

# Add the current directory to sys.path to import main.py
# This is necessary because the folder name contains a hyphen
sys.path.insert(0, os.path.dirname(__file__))
from main import Solution


class TestMinCostTrip(unittest.TestCase):
    """Test cases for the min_cost_trip function."""
    
    def setUp(self):
        """Initialize a Solution instance for each test."""
        self.solver = Solution()
    
    def test_basic_example(self):
        """Test the basic example from the problem description."""
        D = [1, 4, 2, 3, 5]
        R = [3, 2, 4, 5, 6]
        # Optimal: depart on day 0 (cost 1), return on day 1 (cost 2) = 3
        self.assertEqual(self.solver.min_cost_trip(D, R), 3)
    
    def test_same_day_depart_and_return(self):
        """Test when departing and returning on the same day is optimal."""
        D = [10, 2, 100]
        R = [100, 2, 100]
        # Optimal: depart and return on day 1 (cost 2 + 2 = 4)
        self.assertEqual(self.solver.min_cost_trip(D, R), 4)
    
    def test_all_same_values(self):
        """Test when all departure and return costs are the same."""
        D = [5, 5, 5]
        R = [5, 5, 5]
        # Any valid combination gives 10
        self.assertEqual(self.solver.min_cost_trip(D, R), 10)
    
    def test_first_departure_last_return_optimal(self):
        """Test when first departure and last return is optimal."""
        D = [1, 100, 100]
        R = [100, 100, 1]
        # Optimal: depart on day 0 (cost 1), return on day 2 (cost 1) = 2
        self.assertEqual(self.solver.min_cost_trip(D, R), 2)
    
    def test_last_departure_last_return_optimal(self):
        """Test when last departure and last return is optimal."""
        D = [100, 100, 1]
        R = [100, 100, 1]
        # Optimal: depart on day 2 (cost 1), return on day 2 (cost 1) = 2
        self.assertEqual(self.solver.min_cost_trip(D, R), 2)
    
    def test_negative_values(self):
        """Test with negative cost values."""
        D = [-5, -2, 3]
        R = [4, -1, -3]
        # Optimal: depart on day 0 (cost -5), return on day 2 (cost -3) = -8
        self.assertEqual(self.solver.min_cost_trip(D, R), -8)
    
    def test_very_large_values(self):
        """Test with very large values to check for overflow issues."""
        D = [10**12, 10**15]
        R = [10**18, 10**12]
        # Optimal: depart on day 0 (cost 10^12), return on day 1 (cost 10^12) = 2*10^12
        self.assertEqual(self.solver.min_cost_trip(D, R), 2000000000000)
    
    def test_single_element_arrays(self):
        """Test with single-element arrays."""
        D = [7]
        R = [3]
        # Only option: depart and return on day 0 (cost 7 + 3 = 10)
        self.assertEqual(self.solver.min_cost_trip(D, R), 10)
    
    def test_different_lengths_raises(self):
        """Test that different length arrays raise ValueError."""
        D = [1, 2, 3]
        R = [1, 2]
        with self.assertRaises(ValueError):
            self.solver.min_cost_trip(D, R)
    
    def test_empty_arrays_raises(self):
        """Test that empty arrays raise ValueError."""
        D = []
        R = []
        with self.assertRaises(ValueError):
            self.solver.min_cost_trip(D, R)
    
    def test_arrays_with_zeros(self):
        """Test with arrays containing zero values."""
        D = [0, 2, 0]
        R = [0, 0, 0]
        # Optimal: depart on day 0 (cost 0), return on day 0 (cost 0) = 0
        self.assertEqual(self.solver.min_cost_trip(D, R), 0)
    
    def test_constraint_return_not_before_departure(self):
        """Test that the algorithm respects the constraint j >= i."""
        D = [50, 1]
        R = [0, 100]
        # Valid pairs: (0,0)=50, (0,1)=150, (1,1)=101
        # Invalid but tempting: (1,0)=1 (can't return before departure!)
        # Optimal valid: (0,0)=50
        self.assertEqual(self.solver.min_cost_trip(D, R), 50)
    
    def test_large_array_with_pattern(self):
        """Test with a larger array to verify performance."""
        D = [100, 50, 30, 20, 10, 5, 1]
        R = [1, 5, 10, 20, 30, 50, 100]
        # Optimal: depart on day 6 (cost 1), return on day 6 (cost 100) = 101
        # But wait, we can do better: depart on day 5 (cost 5), return on day 5 (cost 50) = 55
        # Actually best: depart on day 6 (cost 1), return on day 6 (cost 100) = 101
        # No wait, let me recalculate: min would be departing late and returning early (if possible)
        # Best valid: depart on day 0 (cost 100), return on day 0 (cost 1) = 101? No...
        # Actually: depart day 6 (cost 1), return day 6 (cost 100) = 101, but
        # depart day 0 (cost 100), return day 0 (cost 1) = 101, or
        # depart day 4 (cost 10), return day 4 (cost 30) = 40, or
        # depart day 3 (cost 20), return day 3 (cost 20) = 40, or
        # depart day 2 (cost 30), return day 2 (cost 10) = 40, or
        # depart day 1 (cost 50), return day 1 (cost 5) = 55, or
        # depart day 0 (cost 100), return day 0 (cost 1) = 101
        # Best is 40
        self.assertEqual(self.solver.min_cost_trip(D, R), 40)
    
    def test_monotonic_increasing_costs(self):
        """Test with monotonically increasing costs."""
        D = [1, 2, 3, 4, 5]
        R = [1, 2, 3, 4, 5]
        # Optimal: depart on day 0 (cost 1), return on day 0 (cost 1) = 2
        self.assertEqual(self.solver.min_cost_trip(D, R), 2)
    
    def test_monotonic_decreasing_costs(self):
        """Test with monotonically decreasing costs."""
        D = [5, 4, 3, 2, 1]
        R = [5, 4, 3, 2, 1]
        # Optimal: depart on day 4 (cost 1), return on day 4 (cost 1) = 2
        self.assertEqual(self.solver.min_cost_trip(D, R), 2)
    
    def test_alternating_high_low_pattern(self):
        """Test with alternating high and low costs."""
        D = [100, 1, 100, 1, 100]
        R = [1, 100, 1, 100, 1]
        # Optimal: depart on day 1 (cost 1), return on day 2 (cost 1) = 2
        self.assertEqual(self.solver.min_cost_trip(D, R), 2)
    
    def test_edge_case_two_days(self):
        """Test with exactly two days."""
        D = [10, 5]
        R = [3, 8]
        # Valid pairs: (0,0)=13, (0,1)=18, (1,1)=13
        # Optimal: 13 (either day 0,0 or day 1,1)
        self.assertEqual(self.solver.min_cost_trip(D, R), 13)
    
    def test_all_negative_values(self):
        """Test with all negative values."""
        D = [-10, -20, -15]
        R = [-5, -25, -30]
        # Optimal: depart on day 1 (cost -20), return on day 2 (cost -30) = -50
        self.assertEqual(self.solver.min_cost_trip(D, R), -50)
    
    def test_mixed_positive_negative_zero(self):
        """Test with a mix of positive, negative, and zero values."""
        D = [-5, 0, 10, -2]
        R = [8, -3, 0, -10]
        # Optimal: depart on day 0 (cost -5), return on day 3 (cost -10) = -15
        self.assertEqual(self.solver.min_cost_trip(D, R), -15)


if __name__ == "__main__":

    unittest.main()

import unittest
from main import Solution

# Define constants for readability
W = 'W'  # Workday
H = 'H'  # Holiday


class TestMaxVacationDays(unittest.TestCase):
    """Test suite for the max_vacation_days function."""
    
    def setUp(self):
        """Initialize the Solution instance for each test."""
        self.s = Solution()

    def test_docstring_example(self):
        """Test the example provided in the docstring.
        
        calendar = [W, W, H, W, W, H, W], PTO = 3
        Expected: 5 consecutive vacation days
        """
        calendar = [W, W, H, W, W, H, W]
        self.assertEqual(self.s.max_vacation_days(calendar, 3), 5)

    def test_empty_calendar(self):
        """Test with an empty calendar."""
        self.assertEqual(self.s.max_vacation_days([], 0), 0)
        self.assertEqual(self.s.max_vacation_days([], 3), 0)
        self.assertEqual(self.s.max_vacation_days([], 100), 0)

    def test_no_pto_only_holidays_count(self):
        """Test with 0 PTO - should return longest consecutive holiday streak."""
        calendar = [W, H, H, W, H, H, H]
        self.assertEqual(self.s.max_vacation_days(calendar, 0), 3)
        
        calendar = [H, H, H, H, W, H, H]
        self.assertEqual(self.s.max_vacation_days(calendar, 0), 4)

    def test_all_holidays(self):
        """Test calendar with all holidays."""
        calendar = [H] * 10
        self.assertEqual(self.s.max_vacation_days(calendar, 0), 10)
        self.assertEqual(self.s.max_vacation_days(calendar, 5), 10)
        self.assertEqual(self.s.max_vacation_days(calendar, 100), 10)

    def test_all_workdays(self):
        """Test calendar with all workdays."""
        calendar = [W] * 4
        
        # No PTO = no vacation
        self.assertEqual(self.s.max_vacation_days(calendar, 0), 0)
        
        # Some PTO = that many vacation days
        self.assertEqual(self.s.max_vacation_days(calendar, 2), 2)
        
        # PTO exceeds calendar length = entire calendar
        self.assertEqual(self.s.max_vacation_days(calendar, 10), 4)

    def test_single_day_calendars(self):
        """Test single-day calendars."""
        # Single holiday
        self.assertEqual(self.s.max_vacation_days([H], 0), 1)
        self.assertEqual(self.s.max_vacation_days([H], 5), 1)
        
        # Single workday with PTO
        self.assertEqual(self.s.max_vacation_days([W], 1), 1)
        self.assertEqual(self.s.max_vacation_days([W], 10), 1)
        
        # Single workday without PTO
        self.assertEqual(self.s.max_vacation_days([W], 0), 0)

    def test_bridge_single_workday(self):
        """Test bridging holidays with a single workday."""
        calendar = [H, W, H]
        
        # With 1 PTO, can bridge the gap
        self.assertEqual(self.s.max_vacation_days(calendar, 1), 3)
        
        # Without PTO, only get one holiday
        self.assertEqual(self.s.max_vacation_days(calendar, 0), 1)

    def test_bridge_multiple_workdays(self):
        """Test bridging holidays with multiple workdays."""
        calendar = [H, W, W, H]
        
        # With 2 PTOs, can bridge the gap
        self.assertEqual(self.s.max_vacation_days(calendar, 2), 4)
        
        # With 1 PTO, can only get partial bridge
        self.assertEqual(self.s.max_vacation_days(calendar, 1), 2)
        
        # Without PTO, only get one holiday
        self.assertEqual(self.s.max_vacation_days(calendar, 0), 1)

    def test_pto_exceeds_workdays(self):
        """Test when PTO exceeds total workdays in calendar."""
        calendar = [W, H, W, H]
        # With excess PTO, can convert all workdays
        self.assertEqual(self.s.max_vacation_days(calendar, 10), 4)
        
        calendar = [W, W, H, H, W]
        self.assertEqual(self.s.max_vacation_days(calendar, 5), 5)

    def test_complex_mixed_calendar(self):
        """Test complex mixed calendars with strategic PTO placement."""
        # Test case where optimal PTO placement matters
        calendar = [W, H, H, W, W, H, H, H, W, W, W, H]
        self.assertEqual(self.s.max_vacation_days(calendar, 2), 7)
        
        calendar = [H, H, W, W, W, H, H, W, H]
        self.assertEqual(self.s.max_vacation_days(calendar, 2), 5)
        self.assertEqual(self.s.max_vacation_days(calendar, 1), 4)
        self.assertEqual(self.s.max_vacation_days(calendar, 3), 7)
        self.assertEqual(self.s.max_vacation_days(calendar, 4), 9)

    def test_alternating_pattern(self):
        """Test alternating W-H patterns."""
        calendar = [W, H, W, H, W, H]
        
        # With 0 PTO, only individual holidays
        self.assertEqual(self.s.max_vacation_days(calendar, 0), 1)
        
        # With 1 PTO, can connect two holidays
        self.assertEqual(self.s.max_vacation_days(calendar, 1), 3)
        
        # With 2 PTOs, can connect more
        self.assertEqual(self.s.max_vacation_days(calendar, 2), 5)
        
        # With 3 PTOs, can take entire calendar
        self.assertEqual(self.s.max_vacation_days(calendar, 3), 6)

    def test_long_workday_stretches(self):
        """Test calendars with long stretches of workdays."""
        calendar = [H, H, W, W, W, W, W, H, H]
        
        # Need 5 PTOs to bridge the gap
        self.assertEqual(self.s.max_vacation_days(calendar, 5), 9)
        self.assertEqual(self.s.max_vacation_days(calendar, 4), 6)
        self.assertEqual(self.s.max_vacation_days(calendar, 3), 5)
        self.assertEqual(self.s.max_vacation_days(calendar, 2), 4)
        self.assertEqual(self.s.max_vacation_days(calendar, 1), 3)
        self.assertEqual(self.s.max_vacation_days(calendar, 0), 2)

    def test_edge_holidays(self):
        """Test calendars starting or ending with holidays."""
        # Starting with holidays
        calendar = [H, H, H, W, W]
        self.assertEqual(self.s.max_vacation_days(calendar, 0), 3)
        self.assertEqual(self.s.max_vacation_days(calendar, 1), 4)
        self.assertEqual(self.s.max_vacation_days(calendar, 2), 5)
        
        # Ending with holidays
        calendar = [W, W, H, H, H]
        self.assertEqual(self.s.max_vacation_days(calendar, 0), 3)
        self.assertEqual(self.s.max_vacation_days(calendar, 1), 4)
        self.assertEqual(self.s.max_vacation_days(calendar, 2), 5)

    def test_monotonicity_property(self):
        """Test that increasing PTO never decreases max vacation days."""
        test_calendars = [
            [W, W, H, W, W, H, W],
            [H, W, H, W, H, W, H, W],
            [H, H, H, H],
            [W, W, W, W, W],
            [W, H, W, H, W, H],
            [H, W, W, W, H, H, W, H],
        ]
        
        for calendar in test_calendars:
            previous_result = -1
            for pto in range(0, len(calendar) + 3):
                result = self.s.max_vacation_days(calendar, pto)
                
                # Result should be non-decreasing
                self.assertGreaterEqual(
                    result, 
                    previous_result,
                    f"Monotonicity violated: calendar={calendar}, pto={pto}, "
                    f"result={result}, previous={previous_result}"
                )
                
                # Result should not exceed calendar length
                self.assertLessEqual(
                    result,
                    len(calendar),
                    f"Result exceeds calendar length: calendar={calendar}, "
                    f"pto={pto}, result={result}"
                )
                
                previous_result = result

    def test_optimal_pto_placement(self):
        """Test that the solution finds optimal PTO placement."""
        # Case where greedy left-to-right doesn't work
        calendar = [W, W, H, H, H, W, W, W, H, H]
        
        # With 2 PTOs, better to use on first 2 W's to get 5 consecutive
        # rather than spreading them out
        self.assertEqual(self.s.max_vacation_days(calendar, 2), 5)
        
        # Another case where placement matters
        calendar = [H, W, W, H, H, H, W, H]
        # With 1 PTO, better to use on last W to get 4 consecutive H's
        self.assertEqual(self.s.max_vacation_days(calendar, 1), 5)


if __name__ == '__main__':
    # Run tests with verbose output
    unittest.main(verbosity=2)

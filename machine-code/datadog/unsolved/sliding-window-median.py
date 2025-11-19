'''
Sliding Window Median
The median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value. 
So the median is the mean of the two middle values. 
For examples, if arr = [2,3,4], the median is 3. 
For examples, if arr = [1,2,3,4], 
the median is (2 + 3) / 2 = 2.5. 

- You are given an integer array nums and an integer k. 
- There is a sliding window of size k which is moving from the very left of the 
  array to the very right. 
- You can only see the k numbers in the window. 
- Each time the sliding window moves right by one position. 
- Return the median array for each window in the original array. 
- Answers within 10-5 of the actual value will be accepted.
'''
from typing import List

def sliding_window_fixed_k(input_points: List[dict], tag: str, k: int) -> List[int]:
    """
    Implements a fixed-size sliding window to calculate the sum of values
    for data points containing the specified tag.

    Args:
    - input_points: List[dict] -> List of input data points, where each
      data point is a dictionary containing "tags", "timestamp", and "value".
    - tag: str -> The tag to filter for.
    - k: int -> The fixed size of the sliding window.

    Returns:
    - List[int] -> A list of the sums for each sliding window.
    """

    # Filter data points containing the specified tag
    filtered_data = []  # Space complexity: O(N) (stores the filtered data points)

    for dp in input_points:  # Time complexity: O(N)
        if tag in dp["tags"]:
            filtered_data.append((dp["timestamp"], dp["value"]))

    # Sort the filtered data points by timestamp
    filtered_data.sort()  # Time complexity: O(N log N)

    # Initialize the sliding window
    left = 0  # Left pointer, controls the starting position of the sliding window
    result = []  # Result list, stores the sums of the sliding windows, Space complexity: O(N)
    window_sum = 0  # Sum of the values within the current window

    # Calculate the sum of the initial window (first k elements)
    for i in range(0, k):  # Time complexity: O(k)
        window_sum += filtered_data[i][1]
    result.append(window_sum)

    # Calculate the sums of subsequent windows using the sliding window technique
    for right in range(k, len(filtered_data)):  # Time complexity: O(N - k) ≈ O(N)
        window_sum += filtered_data[right][1]  # Add the new element at the right end
        window_sum -= filtered_data[left][1]   # Remove the old element at the left end
        left += 1  # Move the left pointer
        result.append(window_sum)

    return result

# Test cases
input_points = [
    {"tags": ["env:dev"], "timestamp": 0, "value": 1},
    {"tags": ["env:dev"], "timestamp": 1, "value": 3},
    {"tags": ["env:prod", "host:a"], "timestamp": 2, "value": 5},
    {"tags": ["env:dev"], "timestamp": 3, "value": -1},
    {"tags": ["env:dev", "host:a"], "timestamp": 6, "value": -3},
    {"tags": ["env:dev"], "timestamp": 7, "value": 5},
    {"tags": ["env:staging", "host:a"], "timestamp": 9, "value": -3},
    {"tags": ["env:dev"], "timestamp": 10, "value": -4},
    {"tags": ["env:dev"], "timestamp": 11, "value": 6},
    {"tags": ["env:dev"], "timestamp": 14, "value": -1},
    {"tags": ["env:staging"], "timestamp": 15, "value": 10},
]

print(sliding_window_fixed_k(input_points, "env:dev", 3))

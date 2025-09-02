def get_min_total_distance(dist_centers):
    dist_centers.sort()
    n = len(dist_centers)

    def calculate_total_distance(w1, w2):
        return sum(min(abs(dc - w1), abs(dc - w2)) for dc in dist_centers)

    def binary_search(left, right):
        while right - left > 3:
            m1 = left + (right - left) // 3
            m2 = right - (right - left) // 3
            print("m1:", m1)
            print("m2:", m2)
            print("dist_centers:", dist_centers)

            if calculate_total_distance(
                dist_centers[m1], dist_centers[m2]
            ) > calculate_total_distance(dist_centers[m1 + 1], dist_centers[m2]):
                left = m1 + 1
            else:
                right = m2

        for i in range(left, right):
            for j in range(i + 1, right + 1):
                total_dist = calculate_total_distance(dist_centers[i], dist_centers[j])
                print("total_dist", total_dist)

        return min(
            calculate_total_distance(dist_centers[i], dist_centers[j])
            for i in range(left, right)
            for j in range(i + 1, right + 1)
        )

    return binary_search(0, n - 1)


# Test cases
def test_get_min_total_distance():
    # Test case 1: Example from the image
    assert get_min_total_distance([1, 2, 3]) == 1

    # Test case 2: All distribution centers at the same location
    assert get_min_total_distance([5, 5, 5, 5]) == 0

    # Test case 3: Two optimal warehouse locations
    assert get_min_total_distance([1, 2, 3, 4, 5, 6]) == 5

    # Test case 4: Odd number of distribution centers
    print("answer 1:", get_min_total_distance([1, 3, 5, 7, 9]))
    assert get_min_total_distance([1, 3, 5, 7, 9]) == 8

    # Test case 5: Large range of values
    assert get_min_total_distance([1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) == 220

    print("All test cases passed!")


# Run the tests
test_get_min_total_distance()

from itertools import combinations


def canDistributeCredits(participants, credits):
    def is_divisible(total, participants):
        return total % participants == 0

    valid_combinations = 0

    for r in range(1, len(credits) + 1):
        for combo in combinations(credits, r):
            total_credits = sum(combo)
            if is_divisible(total_credits, participants):
                valid_combinations += 1

    return valid_combinations


# Example usage and test
participants = 6
credits = [12, 18, 24, 36]
result = canDistributeCredits(participants, credits)
print(f"Number of possible ways to distribute credits: {result}")

# Additional test cases
print(canDistributeCredits(4, [1, 2, 3, 4]))  # Should return 1
print(canDistributeCredits(3, [2, 5, 7]))  # Should return 0
print(canDistributeCredits(5, [10, 20, 30, 40, 50]))  # Should return 7

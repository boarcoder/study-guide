"""
Calculate the minimum cost for departure and return trip
There are two arrays D and R, representing departure and return costs respectively.
The return time should be on or after the departure time.
Calculate the minimum cost for departure and return.

For example, D = [1,4,2,3,5], R = [3,2,4,5,6], min_cost=3
(depart on day 1, return on day 2)
"""


class Solution:
    def min_cost_trip(self, D: list, R: list):
        if not D or not R:
            raise ValueError("Input arrays cannot be empty.")
        if len(D) != len(R):
            raise ValueError("Input arrays must have the same length.")

        cheapest_trip = float("inf")
        cheapest_dep = float("inf")
        for i in range(len(D)):
            departure_cost, return_cost = D[i], R[i]

            cheapest_dep = min(cheapest_dep, departure_cost)

            trip_cost = cheapest_dep + return_cost
            cheapest_trip = min(cheapest_trip, trip_cost)

        return cheapest_trip

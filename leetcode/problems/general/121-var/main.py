def find_cheapest_tickets(departures, returns):
    dep_price = float('inf')
    ret_price = float('inf')
    round_trip = float('inf')
    for i in range(len(departures)):
        ret_price = returns[i + 1] if i + 1 < len(returns) else float('inf')
        dep_price = min(dep_price, departures[i])
        round_trip = min(round_trip, ret_price + dep_price)
        # ret_price = ret
    print('round_trip', round_trip)
    return round_trip        

if __name__ == "__main__":
    departures = [ 8, 3, 6, 10]
    returns =    [10, 9, 5, 8 ]
    assert find_cheapest_tickets(departures, returns) == 8

    departures = [10, 3, 10, 9, 3]
    returns =    [4, 20, 6, 7, 10]
    assert find_cheapest_tickets(departures, returns) == 9

    departures = [1, 3, 10, 9, 3]
    returns =    [1, 20, 6, 7, 10]
    assert find_cheapest_tickets(departures, returns) == 7

    departures = [1, 3, 10, 9, 3]
    returns = [1, 1, 6, 7, 10]
    assert find_cheapest_tickets(departures, returns) == 2

    departures = [1, 3, 10, 9, 3]
    returns = [10, 9, 8, 7, 6]
    assert find_cheapest_tickets(departures, returns) == 7

    departures = [12, 33, 44, 9, 23]
    returns = [100, 90, 80, 70, 15]
    assert find_cheapest_tickets(departures, returns) == 24

    departures = [4, 3, 5, 11, 2]
    returns = [1, 6, 10, 2, 9]
    assert find_cheapest_tickets(departures, returns) == 5
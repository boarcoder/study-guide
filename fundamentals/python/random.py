# Notes on python `random` module

import random

element_list =     [0,    1,2,3,4,5,6]
weight_list =      [0.1,0.1,0.1,0.1,0.1,0.1,0.4]
cum_weights_list = [0.1,0.2,0.3,0.4,0.5,0.6,1.0]
'''
Random with replacement (numbers not removed)
TC: O(N) if you use weights= param. With k, O(N * k)
    O(log(n)) if you use cum_weights= param. With k, O(k * log(n))
SC: O(k)

Every time this is called, if you provide weights=, it calculates cum_weights in O(N).
The value for bisect_left is (automatically) calculated using:
random.uniform(0, cum_weights[-1)
'''
selected_list = random.choices(element_list, cum_weights=,k=)

'''
Random without replacement (numbers are removed after selecting)
TC: O(N) always. With k, O(N * k)
SC: O(k).

Stack overflow says we can estimate TC as O(k), but this is not correct!
We must always calculate cumulative weights before making any selection, k times.

It must re-calculate cum_weights, internally, as it is not accepted as a parameter. 
Removing an element means cum_weights needs to subtract that probability after that element.
'''
selected_list = random.sample(element_list, weight=,k=)

# Float:
random.uniform(0, 1.00)

# int:
random.randrange(0, 100)

# k int from a range, without replacement:
random.sample([range(0,100)], k=3)

# shuffle list in place:
random.shuffle(element_list)
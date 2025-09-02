'''
Problem:
When a user visits the shopping cart page, 
display the products they’ve added to the cart. 

The products need to be sorted based on the following rules:
Products are grouped by groupInfo.
Within each groupInfo, groups are sorted by the smallest product.id 
in that group in ascending order.

'''

import json
import pprint

def cust_sort(element):
    return element['groupInfo'], element['id']

def shopping_cart_sort(input_json: str) -> list:
    cart_list = json.loads(input_json)
    cart_list.sort(key=cust_sort)
    return cart_list

input_json = r'''[
      {"id":  1, "groupInfo": "group1", "price": 521},
      {"id": 13, "groupInfo": "group1", "price": 521},
      {"id":  4, "groupInfo": "group5", "price": 454},
      {"id": 11, "groupInfo": "group1", "price": 501},
      {"id": 41, "groupInfo": "group2", "price": 555},
      {"id": 28, "groupInfo": "group5", "price": 623}
]'''

expected = [
      {"id":  1, "groupInfo": "group1", "price": 521},
      {"id": 13, "groupInfo": "group1", "price": 521},
      {"id": 11, "groupInfo": "group1", "price": 501},
      {"id":  4, "groupInfo": "group5", "price": 454},
      {"id": 28, "groupInfo": "group5", "price": 623},
      {"id": 41, "groupInfo": "group2", "price": 555}
]

res = shopping_cart_sort(input_json)
pprint.pprint(res)
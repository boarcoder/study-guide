def int_to_bin_str(number, fill_zero):
    bin_str = "{0:b}".format(number)
    res = ""
    for i in range(len(bin_str), fill_zero):
        res += "0"
    res += bin_str
    return res


def get_possible_combinations_mask_list(input_list):
    res = []
    for i in range(2 ** len(input_list)):
        res.append(int_to_bin_str(i, len(input_list)))
    return res


def get_possible_combinations_set(input_list):
    res = set()
    mask_list = get_possible_combinations_mask_list(input_list)
    print("masks:", mask_list)
    for mask in mask_list:
        cur = []
        for i, ch in enumerate(mask):
            if ch == "1":
                cur.append(input_list[i])
        if cur:
            res.add(tuple(cur))
    return res


def is_possible_balance_for_list(combination, competitors):
    min_prize = min(combination)

    print("checking combination", combination)

    for i in range(min_prize + 1, 0, -1):
        coins = None
        for prize in combination:
            if prize % i != 0:
                break
            # print("adding to coins:", prize, i)
            if coins is None:
                coins = 0
            coins += prize / i
        if coins and coins % competitors == 0:
            print(f"valid because prize: {prize}, coins: {coins}")
            return 1
    return 0


def balance_coins(prize_list, competitors):
    possible_combination_ct = 0
    possible_combinations_set = get_possible_combinations_set(prize_list)
    print(possible_combinations_set)

    for combination in possible_combinations_set:
        possible_combination_ct += is_possible_balance_for_list(
            combination, competitors
        )
    return possible_combination_ct


import unittest


class TestBalanceStr(unittest.TestCase):
    def test_1(self):
        prize_list = [12, 18, 24, 36]
        competitors = 6
        expected = 8

        actual = balance_coins(prize_list, competitors)
        self.assertEqual(expected, actual)

    # def test_2(self):
    #     prize_list = [7, 3, 6]
    #     competitors = 5
    #     expected = 1

    #     actual = balance_coins(prize_list, competitors)
    #     self.assertEqual(expected, actual)


unittest.main()

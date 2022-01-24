from typing import List


def maxProfit(prices: List[int]) -> int:
    left_ptr = 0
    right_ptr = 1
    max_profit = 0

    while right_ptr <= len(prices) - 1:
        if prices[left_ptr] > prices[right_ptr]:
            left_ptr = right_ptr
        else:
            potential_profit = prices[right_ptr] - prices[left_ptr]

            if potential_profit > max_profit:
                max_profit = potential_profit

        right_ptr += 1

    return max_profit


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))

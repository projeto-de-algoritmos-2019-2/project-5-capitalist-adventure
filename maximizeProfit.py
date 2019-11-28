"""
Problem Statement
=================

Given certain stock values over a period of days (d days)
and a number K, the number of transactions allowed, find the
maximum profit that be obtained with at most K transactions.

Video
-----
* https://youtu.be/oDhu5uGq_ic

Complexity
----------
* Space Complexity: O(days * transctions)
* Time  Complexity: O(days * transaction)
"""


def max_profit(prices, K):

    if K == 0 or prices == []:
        return 0

    days = len(prices)

    # 0th transaction up to and including kth transaction is considered.
    num_transactions = K + 1

    T = [[0 for _ in range(days)] for _ in range(num_transactions)]

    for transaction in range(1, num_transactions):

        max_diff = -prices[0]

        for day in range(1, days):

            T[transaction][day] = max(
                T[transaction][day - 1],    # do nothing today or
                prices[day] + max_diff      # sell today
            )

            # max_diff is the accumulated profit from previous transactions

            # update max_diff
            max_diff = max(
                max_diff,

                # acc without this transaction - price of buying today
                T[transaction - 1][day] - prices[day]
            )

    print_actual_solution(T, prices)

    return T[-1][-1]


def print_actual_solution(T, prices):
    transaction = len(T) - 1
    day = len(T[0]) - 1
    stack = []

    while True:
        if transaction == 0 or day == 0:
            break

        if T[transaction][day] == T[transaction][day - 1]:  # Didn't sell
            day -= 1
        else:
            stack.append(day)          # sold
            max_diff = T[transaction][day] - prices[day]
            for k in range(day - 1, -1, -1):
                if T[transaction - 1][k] - prices[k] == max_diff:
                    stack.append(k)  # bought
                    transaction -= 1
                    break

    for entry in range(len(stack) - 1, -1, -2):
        print("Buy on day {day} at price {price}".format(day=stack[entry], price=prices[stack[transaction]]))
        print("Sell on day {day} at price {price}".format(day=stack[entry], price=prices[stack[transaction - 1]]))


if __name__ == '__main__':

    prices = [2, 5, 7, 1, 4, 3, 1, 3]
    max_profit(prices, 2)

    # assert 10 == max_profit(prices, 3)
    # assert 10 == max_profit_slow_solution(prices, 3)
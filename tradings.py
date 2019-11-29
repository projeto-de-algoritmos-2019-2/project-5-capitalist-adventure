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

    return print_actual_solution(T, prices)

    # return T[-1][-1]


def print_actual_solution(T, prices):

    transaction = len(T) - 1
    day = len(T[0]) - 1
    stack = []

    while True:

        if transaction == 0 or day == 0:
            break

        # if what i have today is the same i had yesterday, today i dint sell nothing
        if T[transaction][day] == T[transaction][day-1]:
            day -= 1

        else:
            stack.append((day, 'Sell'))

            max_diff = T[transaction][day] - prices[day]

            for k in range(day-1, -1, -1):

                if(T[transaction-1][k] - prices[k] == max_diff):
                    stack.append((k, 'Buy'))
                    transaction -= 1
                    day = k
                    break

    return list(reversed(stack))


if __name__ == '__main__':

    prices = [13.5,13.13,13.31,13.25,13.38,13.13,13.19,12.5,12.19,12.25,12.0,12.0,13.0,14.0,13.75,12.88,11.88,13.0,12.94,12.44]
    transactions =  max_profit(prices, 3)

    for t in transactions:
        print(t)

    # print(transactions)

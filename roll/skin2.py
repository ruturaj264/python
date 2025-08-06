import random

def roll(input_money):

    increment = input_money * 0.26 / 100
    start_bid = input_money * 0.25 / 100
    total_spent = 0

    bid = start_bid
    num = random.randint(1, 27)

    for i in range(1, 100):

        total_spent = round(bid + total_spent, 2)
        money_left = input_money - total_spent

        if total_spent > input_money:
            return round(money_left + bid, 2)

        if i == num:
            won = round(bid * 14, 2)
            profit = round(won - total_spent, 2)

            # print(f'sr {i}, bid {bid}, total spent {total_spent}, won {won}, profit {profit}')
            return round(input_money + profit, 2)

        bid = round(bid + increment, 2)
            

input_money = 50

for i in range(20):

    input_money = roll(input_money)
    print(input_money)



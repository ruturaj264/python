def roll(input_money):

    increment = input_money * 0.26 / 100
    start_bid = input_money * 0.25 / 100
    total_spent = 0

    bid = start_bid

    for i in range(1, 100):

        total_spent = round(bid + total_spent, 2)
        won = round(bid * 14, 2)
        profit = round(won - total_spent, 2)

        print(f'sr {i}, bid {bid}, total spent {total_spent}, won {won}, profit {profit}')

        bid = round(bid + increment, 2)
        
        if total_spent >= input_money or total_spent + bid >= input_money:
            break

input_money = 100
roll(input_money)

# import random

# print(random.randint(1, 27))
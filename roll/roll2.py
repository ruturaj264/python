import random

def roll(input_money):

    increment = 0.01
    start_bid = 0.01
    total_spent = 0

    green_bid = start_bid
    bait_bid = start_bid
    balance = input_money
    win = True

    for i in range(1, 1000):

        if win:
            # total_spent = 0
            bait_bid = start_bid
            green_bid = start_bid
        else:
            green_bid = round(green_bid + 0.01, 2)
            bait_bid = round(bait_bid + 0.01, 2)

        hit = random.choice([1,2,2,2,2,2,2,2,2,2,2,2,2,1,3])
        total_spent = round(green_bid + bait_bid + total_spent, 2)

        if total_spent > input_money:
            print(balance)
            break
        
        balance = round(input_money - total_spent, 2)

        if hit == 1:
            won = round(bait_bid * 7, 2)
            win = True
        elif hit == 3:
            won = round(green_bid * 14, 2)
            win = True
        else:
            won = 0
            win = False

        profit = round(won - total_spent, 2)
        balance = round(balance + won, 2)

        print(f'sr {i}, hit {hit}, green {green_bid}, bait {bait_bid}, total spent {total_spent}, won {won}, profit {profit}, balance {balance}')

input_money = 40
roll(input_money)

# import random

# print(random.randint(1, 27))
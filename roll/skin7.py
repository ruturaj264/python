import random

def roll(input_money, risk_factor, win):

    if risk_factor == 0:

        increment = round(0.01/100*input_money, 2)
        start_bid = round(0.01/100*input_money, 2)
    else:

        return

    increment = max(increment, 0.01)
    bid = max(start_bid, 0.01)
    spent = 0

    for i in range(1, 28):
        
        hit = random.choice([1,2,1,2,1,2,1,2,1,2,1,2,1,2,3])
        spent = round(spent + bid, 2)
        balance = round(input_money - spent, 2)
        won = 0
        profit = 0

        if hit == 3:

            won = round(bid * 14, 2)
            profit = round(won - spent, 2)
            balance = round(balance + won, 2)

            print(f'{i}: bid {bid}, spent {spent}, won {won}, profit {profit}, balance {balance}')

            return True, balance, turn
        
        # else:  

        #     print(f'{i}: bid {bid}, spent {spent}, won {won}, profit {profit}, balance {balance}')

        bid = round(bid + increment, 2)

        if spent == input_money:
            break

        if bid + spent > input_money:
            money_left = round(input_money - spent, 2)
            bid = money_left
    else:

        print(f'{i}: bid {bid}, spent {spent}, won {won}, profit {profit}, balance {balance}')

        return False, balance, turn


risk_factor = 0
input_money = 28.44
win = True
turn = 1

for i in range(100):

    win, input_money, turn = roll(input_money, risk_factor, win)
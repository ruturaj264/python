import random

def roll(start_money, input_money, risk_factor, win, turn, old_i, old_count, old_streak, old_spent, old_start_bid, old_turn_count):

    if risk_factor == 0:
        bid = round(0.05/50 * start_money, 2)
    elif risk_factor == 1:
        bid = round(0.1/50 * start_money, 2)
    elif risk_factor == 2:
        bid = round(0.2/50 * start_money, 2)
    elif risk_factor == 3:
        bid = round(0.4/50 * start_money, 2)

    bid_increment = 2
    loss_bid_increment = 1.5
    streak = 4
    spent = 0
    count = 0
    turn_count = old_turn_count
    i = 0

    if not win:
        bid = round(old_start_bid * loss_bid_increment, 2)
        streak = streak + old_streak
        i = i + old_i
        count = count + old_count
        spent = spent + old_spent


    bid = max(bid, 0.01)
    start_bid = bid
    # bid = 0.07

    while i < streak:

        hit = random.choice([0,1,0,1,0,1,0,1,0,1,0,1,0,1,3])
        roulette.append(hit)

        turn_count += 1

        if turn_count == 3:
            turn_count = 1
            if turn == 1:
                turn = 0
            else:
                turn = 1
        
        i += 1
        spent = round(spent + bid, 2)

        if win:
            balance = round(input_money - spent, 2)
        else:
            balance = round(start_money - spent, 2)

        bal.append(balance)
        won = 0
        profit = 0

        if hit == turn:

            count = 0
            won = bid * 2
            balance = round(balance + won, 2)
            start_money = balance
            profit = round(balance - money, 2)

            print(f'{i}: bet {turn}, hit {hit} bid {bid}, spent {spent}, won {won}, profit {profit}, balance {balance}')

            return start_money, True, balance, turn, i, count, streak, spent, start_bid, turn_count
        
        else:  

            profit = round(balance - start_money, 2)
            print(f'{i}: bet {turn}, hit {hit} bid {bid}, spent {spent}, won {won}, profit {profit}, balance {balance}')

        bid = round(bid * bid_increment, 2)

        if spent == input_money:

            # print(f'{i}: bet {turn}, hit {hit} bid {bid}, spent {spent}, won {won}, profit {profit}, balance {balance}')
            return start_money, False, balance, turn, i, count, streak, spent, start_bid, turn_count

        if bid + spent > input_money:
            money_left = round(input_money - spent, 2)
            bid = money_left
    else:
        return start_money, False, balance, turn, i, count, streak, spent, start_bid, turn_count


risk_factor = 2
start_money = 50
money = start_money
input_money = start_money
win = True
bal = []

old_turn = 1
old_i = 0
old_count = 0
old_streak = 0
old_spent = 0
old_start_bid = 0
old_turn_count = 0

for i in range(500):

    if input_money > 0:
        roulette = []
        start_money, win, input_money, old_turn, old_i, old_count, old_streak, old_spent, old_start_bid, old_turn_count = roll(start_money, input_money, risk_factor, win, old_turn, old_i, old_count, old_streak, old_spent, old_start_bid, old_turn_count)

# print(roulette)
print(min(bal), max(bal))
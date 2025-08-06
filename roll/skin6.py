import random

def roll(start_money, input_money, risk_factor, win, turn, old_i, old_count, old_streak, old_spent):

    if risk_factor == 0:
        bid = round(0.05/48.65*input_money, 2)
    elif risk_factor == 1:
        bid = round(0.11/48.65*input_money, 2)
    elif risk_factor == 2:
        bid = round(0.24/48.65*input_money, 2)
    elif risk_factor == 3:
        bid = round(0.53/48.65*input_money, 2)

    bid_increment = 2.5
    loss_bid_increment = 3
    streak = 5
    wait = 3
    spent = 0
    count = 0
    i = 0

    if not win:
        bid = round(bid * loss_bid_increment, 2)
        streak = streak + old_streak
        i = i + old_i
        count = count + old_count
        spent = spent + old_spent

    bid = max(bid, 0.01)
    # bid = 0.07

    while i < streak:

        hit = random.choice([0,1,0,1,0,1,0,1,0,1,0,1,0,1,3])
        roulette.append(hit)

        if hit == 0:
            count += 1
        else:
            count = 0

        if count < wait+1 and i == 0:
            continue

        i += 1
        spent = round(spent + bid, 2)
        balance = round(input_money - spent, 2)
        bal.append(balance)
        won = 0
        profit = 0
        turn = 1

        if hit == turn:

            count = 0
            won = bid * 2
            balance = round(balance + won, 2)
            profit = round(balance - start_money, 2)

            print(f'{i}: bet {turn}, hit {hit} bid {bid}, spent {spent}, won {won}, profit {profit}, balance {balance}')

            if turn == 1:
                turn = 0
            else:
                turn = 1

            return start_money, True, balance, turn, i, count, streak, spent
        
        else:  

            profit = round(balance - start_money, 2)
            print(f'{i}: bet {turn}, hit {hit} bid {bid}, spent {spent}, won {won}, profit {profit}, balance {balance}')
            
            if turn == 1:
                turn = 0
            else:
                turn = 1

        bid = round(bid * bid_increment, 2)

        if spent == input_money:

            # print(f'{i}: bet {turn}, hit {hit} bid {bid}, spent {spent}, won {won}, profit {profit}, balance {balance}')
            return start_money, False, balance, turn, i, count, streak, spent

        if bid + spent > input_money:
            money_left = round(input_money - spent, 2)
            bid = money_left
    else:
        return start_money, False, balance, turn, i, count, streak, spent


risk_factor = 0
start_money = 30
input_money = start_money
win = True
turn = 1
bal = []

old_i = 0
old_count = 0
old_streak = 0
old_spent = 0

for i in range(500):

    if input_money > 0:
        roulette = []
        start_money, win, input_money, turn, old_i, old_count, old_streak, old_spent = roll(start_money, input_money, risk_factor, win, turn, old_i, old_count, old_streak, old_spent)

# print(roulette)
print(min(bal), max(bal))
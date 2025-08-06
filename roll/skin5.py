def roll(input_money, risk_factor):

    if risk_factor == 0:

        increment = round(0.01/100*input_money, 2)
        start_bid = round(0.01/100*input_money, 2)

    elif risk_factor == 1:

        increment = round(0.02/50*input_money, 2)
        start_bid = round(0.01/50*input_money, 2)

    elif risk_factor == 2:

        increment = round(0.26/100*input_money, 2)
        start_bid = round(0.25/100*input_money, 2)

    # increment = .1
    # start_bid = .1

    increment = max(increment, 0.01)
    start_bid = max(start_bid, 0.01)
    total_spent = 0

    bid = round(start_bid, 2)

    for i in range(1, 100):

        total_spent = round(bid + total_spent, 2)
        won = round(bid * 7, 2)
        profit = round(won - total_spent, 2)
        balance = round(input_money + profit, 2)

        print(f'{i}: bid {bid}, total spent {total_spent}, won {won}, profit {profit}, balance {balance}')


        bid = round(bid + increment, 2)
        
        if total_spent >= input_money or total_spent + bid >= input_money:
            break

input_money = 30
risk_factor = 1
roll(input_money, risk_factor)


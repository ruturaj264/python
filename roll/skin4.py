risk_factor = 3
input_money = 19

if risk_factor == 0:
    bid = round(0.05/48.65*input_money, 2)
elif risk_factor == 1:
    bid = round(0.11/48.65*input_money, 2)
elif risk_factor == 2:
    bid = round(0.24/48.65*input_money, 2)
elif risk_factor == 3:
    bid = round(0.53/48.65*input_money, 2)

bid = max(bid, 0.01)
# bid = 0.07
spent = 0

for i in range(1, 100):
    
    spent = round(spent + bid, 2)

    won = bid * 2
    profit = round(won - spent, 2)

    print(f'{i}: bid {bid}, spent {spent}, won {won}, profit {profit}')

    bid = round(bid * 2.2, 2)

    if spent == input_money:
        break

    if bid + spent > input_money:
        money_left = round(input_money - spent, 2)
        bid = money_left


    
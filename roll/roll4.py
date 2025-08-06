import random

class RollAccount():

    def __init__(self, balance):
        self.__startBalance = round(balance, 2)
        self.__currentBalance = round(balance, 2)
        self.__profit = round(balance - balance, 2)
        self.__rouletteHits = []
        self.__balanceHistory = []
        self.__balanceHistory.append(round(balance, 2))

    def credit(self, amount):
        self.__currentBalance = round(self.__currentBalance + amount, 2)
        self.__balanceHistory.append(self.__currentBalance)
        self.__profit = round(self.__startBalance - self.__currentBalance, 2)

    def debit(self, amount):
        self.__currentBalance = round(self.__currentBalance - amount, 2)
        self.__balanceHistory.append(self.__currentBalance)
        self.__profit = round(self.__startBalance - self.__currentBalance, 2)

    def getStartBalance(self):
        return self.__startBalance
    
    def getCurrentBalance(self):
        return self.__currentBalance
    
    def getProfit(self):
        return self.__profit
    
    def clearRouletteHits(self):
        self.__rouletteHits = []
    
    def setRouletteHits(self, hit):
        self.__rouletteHits.append(hit)
    
    def getRouletteHits(self):
        return self.__rouletteHits
    
    def getBalanceHistory(self):
        return self.__balanceHistory

class Turn():

    def __init__(self, continous = 1):

        if continous <= 0:
            continous = 1

        self.t = [1] * continous

    def next(self):

        target = self.t.pop(0)
        if target == 1:
            self.t.append(0)
        else:
            self.t.append(1)
            
def roll(old_target, old_target_count):

    bid = round(0.4/100 * my_account.getCurrentBalance(), 2)
    start_bid = bid
    my_target = old_target

    max_loss_streak = 4
    loss_increment_factor = 3
    continuous = 4

    i = 1
    loss_streak = 0
    end = max_loss_streak
    total_spent = 0
    target_count = old_target_count

    while i <= end:

        my_account.debit(bid)

        if my_account.getCurrentBalance() <= 0:
            return my_target, target_count

        total_spent = round(total_spent + bid, 2)

        hit = random.choice([1,2,1,2,1,2,1,2,1,2,1,2,1,2,3])
        my_account.setRouletteHits(hit)
        won = 0
        target_count += 1

        if target_count == continuous+1:

            target_count = 1
            if my_target == 1:
                my_target = 2
            else:
                my_target = 1

        if hit == my_target:

            won = round(bid * 2, 2)
            my_account.credit(won)
            loss_streak = 0

            print(f'{i}: target {my_target}, hit {hit}, bid {bid}, spent {total_spent}, won {won}, balance {my_account.getCurrentBalance()}')

            return my_target, target_count

        else:

            loss_streak += 1
            print(f'{i}: target {my_target}, hit {hit}, bid {bid}, spent {total_spent}, won {won}, balance {my_account.getCurrentBalance()}')
            bid = round(bid * 2, 2)

        i += 1

        if loss_streak == max_loss_streak:
            loss_streak = 0
            end += max_loss_streak
            bid = round(start_bid * loss_increment_factor, 2)


my_account = RollAccount(50)
old_target = 1
old_target_count = 0

for j in range(10000):

    if my_account.getCurrentBalance() >= 0:
        old_target, old_target_count = roll(old_target, old_target_count)







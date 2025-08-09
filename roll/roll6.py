import random

class RollAccount():

    def __init__(self, balance):
        self.__startBalance = round(balance, 2)
        self.__openingBalance = balance
        self.__currentBalance = round(balance, 2)
        self.__profit = round(balance - balance, 2)
        self.__rouletteHits = []
        self.__balanceHistory = []
        self.__balanceHistory.append(round(balance, 2))
        self.__stash = 0
        self.__noGreenStreaks = []
        self.__rouletteLogs = [] 

    def credit(self, amount):
        self.__currentBalance = round(self.__currentBalance + amount, 2)
        self.__balanceHistory.append(self.__currentBalance)
        self.__profit = round(self.__currentBalance - self.__openingBalance, 2)

    def debit(self, amount):
        self.__currentBalance = round(self.__currentBalance - amount, 2)
        self.__balanceHistory.append(self.__currentBalance)
        self.__profit = round(self.__currentBalance - self.__openingBalance, 2)

    def getStartBalance(self):
        return self.__startBalance
    
    def getCurrentBalance(self):
        return self.__currentBalance
    
    def getOpeningBalance(self):
        return self.__openingBalance
    
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
    
    def setRouletteLogs(self, log):
        self.__rouletteLogs.append(log)
    
    def getRouletteLogs(self):
        return self.__rouletteLogs
        
    def setStash(self):

        if self.__profit > 0 and self.__stash < (self.__openingBalance * 2):
            self.__stash = round(self.__stash + self.__profit, 2)
            self.__currentBalance = round(self.__currentBalance - self.__profit, 2)
            self.__profit = 0
        
        self.__openingBalance = self.__currentBalance
    
    def getStash(self):
        return self.__stash
        
    def setNoGreenStreaks(self, count):
        self.__noGreenStreaks.append(count)
    
    def getNoGreenStreaks(self):
        return self.__noGreenStreaks

class Turn():

    def __init__(self, continuous = 1):

        if continuous <= 0:
            continuous = 1

        self.t = [1] * continuous

    def next(self):

        target = self.t.pop(0)
        if target == 1:
            self.t.append(2)
        else:
            self.t.append(1)

        return target
            
def roll():

    no_green_streak = 0
    max_daily_loss_percent = 10

    for day in range(50):

        daily_loss = 0
        daily_green_hits = 0
        daily_bids = 0
        max_daily_loss = round(my_account.getOpeningBalance() * 0.1, 2)

        if my_account.getCurrentBalance() <= 0:
            break 

        for rolls in range(50):

            bid = round(0.2/100 * my_account.getCurrentBalance(), 2)
            bid = max(0.01, bid)
            green_bid = bid
            start_bid = bid

            max_loss_streak = 3
            loss_increment_factor = 2

            i = 1
            loss_streak = 0
            end = max_loss_streak
            total_spent = 0

            if my_account.getCurrentBalance() <= 0:
                break 

            while i <= end:

                daily_loss = my_account.getOpeningBalance() - my_account.getCurrentBalance()

                if daily_loss >= max_daily_loss:
                    break

                my_target = target.next()
                my_account.debit(bid)
                total_spent = round(total_spent + bid, 2)

                hit = random.choice([1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3])
                my_account.setRouletteHits(hit)
                won = 0
                daily_bids += 1

                if hit == my_target:

                    won = round(bid * 2, 2)
                    my_account.credit(won)
                    loss_streak = 0
                    no_green_streak += 1

                    print(f'{i}: target {my_target}&{3}, hit {hit}, bid {bid}, green bid {green_bid}, spent {total_spent}, won {won}, balance {my_account.getCurrentBalance()}')

                    break 
                
                elif hit == 3:

                    my_account.setNoGreenStreaks(no_green_streak)
                    no_green_streak = 0
                    won = round(green_bid * 14, 2)
                    my_account.credit(won)
                    loss_streak = 0
                    daily_green_hits += 1

                    print(f'{i}: target {my_target}&{3}, hit {hit}, bid {bid}, green bid {green_bid}, spent {total_spent}, won {won}, balance {my_account.getCurrentBalance()}')

                    break 
                
                else:

                    no_green_streak += 1
                    loss_streak += 1
                    print(f'{i}: target {my_target}&{3}, hit {hit}, bid {bid}, green bid {green_bid}, spent {total_spent}, won {won}, balance {my_account.getCurrentBalance()}')


                    bid = round(bid * 2, 2)

                i += 1

                if loss_streak == max_loss_streak:
                    loss_streak = 0
                    end += max_loss_streak
                    bid = round(start_bid * loss_increment_factor, 2)

        daily_profit = round(my_account.getCurrentBalance() - my_account.getOpeningBalance(), 2)
        log = f'Day {day+1}: Opening Balance {my_account.getOpeningBalance()}, Closing Balance {my_account.getCurrentBalance()}, Profit {daily_profit}, Bids {daily_bids}, Green Hits {daily_green_hits}'
        my_account.setRouletteLogs(log)
        my_account.setStash()


my_account = RollAccount(10)
target = Turn(2)

roll()

print(my_account.getStash(), my_account.getCurrentBalance(), my_account.getRouletteHits().count(3))
print(max(my_account.getNoGreenStreaks()))
print(sum(my_account.getNoGreenStreaks())/len(my_account.getNoGreenStreaks()))







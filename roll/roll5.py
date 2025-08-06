import random

class RollAccount():

    def __init__(self, balance):
        self.__startBalance = round(balance, 2)
        self.__currentBalance = round(balance, 2)
        self.__profit = round(balance - balance, 2)
        self.__rouletteHits = []
        self.__balanceHistory = []
        self.__balanceHistory.append(round(balance, 2))
        self.__stash = 0

    def credit(self, amount):
        self.__currentBalance = round(self.__currentBalance + amount, 2)
        self.__balanceHistory.append(self.__currentBalance)
        self.__profit = round(self.__currentBalance - self.__startBalance, 2)

    def debit(self, amount):
        self.__currentBalance = round(self.__currentBalance - amount, 2)
        self.__balanceHistory.append(self.__currentBalance)
        self.__profit = round(self.__currentBalance - self.__startBalance, 2)

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
    
    def setStash(self):
        
        if self.__profit > 0:
            self.__stash = round(self.__stash + self.__profit, 2)
            self.__currentBalance = round(self.__currentBalance - self.__profit, 2)
    
    def getStash(self):
        return self.__stash


my_account = RollAccount(100)

def roll():

    for day in range(10):

        increment = round(0.01/50 * my_account.getCurrentBalance(), 2)
        start_bid = round(0.01/50 * my_account.getCurrentBalance(), 2)
        total_spent = 0
        wait = 30

        start_bid = max(0.01, start_bid)
        increment = max(0.01, increment)
        bid = start_bid

        for i in range(1, 100):

            hit = random.choice([1,2,1,2,1,2,1,2,1,2,1,2,1,2,3])
            my_account.setRouletteHits(hit)

            hits = my_account.getRouletteHits()
            l = len(hits)

            if l >= wait:

                last_hits = hits[(l-wait):]

                if 3 not in last_hits:
        
                    for j in range(27):

                        my_account.debit(bid)
                        total_spent = round(bid + total_spent, 2)
                        hit = random.choice([1,2,1,2,1,2,1,2,1,2,1,2,1,2,3])
                        won = 0

                        if my_account.getCurrentBalance() <= 0:
                            break

                        if hit == 3:

                            won = round(bid * 14, 2)
                            my_account.credit(won)

                            print(f'hit {hit}, bid {bid}, total spent {total_spent}, won {won}, profit {my_account.getProfit()}, balance {my_account.getCurrentBalance()}')

                            break

                        else:

                            print(f'hit {hit}, bid {bid}, total spent {total_spent}, won {won}, profit {my_account.getProfit()}, balance {my_account.getCurrentBalance()}')
                            bid = round(bid + increment, 2)

                    my_account.clearRouletteHits()
                    total_spent = 0
                    increment = round(0.01/50 * my_account.getCurrentBalance(), 2)
                    bid = round(0.01/50 * my_account.getCurrentBalance(), 2)
        
        my_account.setStash()
        
roll()
print(my_account.getStash(), my_account.getCurrentBalance())












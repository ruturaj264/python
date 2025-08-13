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

def roulette():

    for day in range(1, days+1):

        hit = random.choice([1,2,1,2,1,2,1,2,1,2,1,2,1,2,3])
        start_bid = round(max(0.01, myAccount.getCurrentBalance() * 0.001), 2)
        bid = start_bid
        
        for roll in range(1, daily_rolls+1):

            my_hit = hit
            myAccount.debit(bid)

            hit = random.choice([1,2,1,2,1,2,1,2,1,2,1,2,1,2,3])

            if hit == my_hit:

                if hit in [1,2]:
                    myAccount.credit(bid*2)
                else:
                    myAccount.credit(bid*14)

                log = f'day {day}, roll {roll}, bid {bid}, target {my_hit}, hit {hit}, opening balance {myAccount.getOpeningBalance()}, current balance {myAccount.getCurrentBalance()}'
                print(log)
                myAccount.setRouletteLogs(log)
                bid = round(max(0.01, bid * increment_factor), 2)

            else:

                log = f'day {day}, roll {roll}, bid {bid}, target {my_hit}, hit {hit}, opening balance {myAccount.getOpeningBalance()}, current balance {myAccount.getCurrentBalance()}'
                print(log)
                myAccount.setRouletteLogs(log)
                bid = start_bid
                
    # for log in myAccount.getRouletteLogs():
    #     print(log)


myAccount = RollAccount(50)
days = 50
daily_rolls = 50
increment_factor = 1.4

roulette()




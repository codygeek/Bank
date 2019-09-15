class CashRegister:
    cashOnHand = 0
     def __init__(self, cash=500):
            self.cashOnHand=cash

     def acceptamount(self, amt):
            self.cashOnHand+=amt

     def getCurrentBalance(self):
        return self.cashOnHand

class DispenserType:
    noOfItems=0
    cost=0

    def __init__(self,items=50,cost=50):
        self.noOfItems=items
        self.cost=cost

    def getNoOfItems(self):
        return self.noOfItems

    def getCost(self):
        return  self.cost

    def MakeSale(self):
        self.noOfItems-=1

cr=CashRegister(2000)





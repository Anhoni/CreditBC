class trans:
    """this is block of transaction"""
    def __init__(self, tid):
        self.tid = tid
        self.tsender = input("Enter sender: ")
        self.treciver = input("Enter recipient: ")
        self.tamount = input("Enter amount: ")

    def returnTransaction(self):
        return str(self.tid) + "\t" + self.treciver + "\t" + self.tsender + "\t" + self.tamount

    def Genesis(self):
        __transactionfile = open("transactions.txt","a+")
        __transactionfile.write("1" + "\t" + "Origin" + "\t" + "Creator" + "\t" + "1.00")




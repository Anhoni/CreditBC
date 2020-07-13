from transaction import trans
from creditscore import Score


class block:
    """this class define block that will be created by both transaction and creditscore"""
    def __init__(self):
        __tTranRead = open("transactions.txt", "r")
        __allTrans = __tTranRead.readlines()
        __tTranRead.close()
        self.previous = __allTrans
        __newID = __allTrans[len(__allTrans) - 1]
        __newID = int(__newID.partition("\t")[0]) + 1
        __currentTransaction = trans(__newID)
        self.transaction = __currentTransaction
        __str = [self.previous, self.transaction]
        self.blockhash = hash(str(__str))
        __tTranWrite = open("transactions.txt", "a+")
        __tTranWrite.write("\n" + __currentTransaction.returnTransaction())
        __tTranWrite.close()
        __blockWrite = open("Blocks.txt", "a")
        __blockWrite.write("\n" + str(self.blockhash))
    def Blockhash(self):
        return self.blockhash


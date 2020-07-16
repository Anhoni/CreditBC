from transaction import trans


class block:
    """this class define block that will be created by both transaction and creditscore"""
    def __init__(self):
        __tTranRead = open("transactions.txt", "r")
        __allTrans = __tTranRead.readlines()
        __tTranRead.close()
        if len(__allTrans) == 0:
            trans.Genesis(trans)
        self.previous = __allTrans
        # get new id by adding id to previous id
        __newID = __allTrans[len(__allTrans) - 1]
        __newID = int(__newID.partition("\t")[0]) + 1
        # call class to build new transaction with this id
        __currentTransaction = trans(__newID)
        # add this and previous transaction and get hash of it
        self.transaction = __currentTransaction
        __str = [self.previous, self.transaction]
        self.blockhash = hash(str(__str))
        # paste this transaction to the file
        __tTranWrite = open("transactions.txt", "a+")
        __tTranWrite.write("\n" + __currentTransaction.returnTransaction())
        __tTranWrite.close()
        # add block as well to this file this will be distributed 
        __blockWrite = open("Blocks.txt", "a")
        __blockWrite.write("\n" + str(self.blockhash))
        __blockWrite.close()
    def Blockhash(self):
        return self.blockhash


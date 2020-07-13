from transaction import trans
from creditscore import score

class block:
    """this class define block that will be created by both transaction and creditscore"""
    def __init__(self):
        self.previous = "101"
        self.transaction = [trans()]
        __str = [self.previous, self.transaction]
        self.blockhash = hash(str(__str))

    def Blockhash(self):
        return  self.blockhash


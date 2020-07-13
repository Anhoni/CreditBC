class Users:
    def __init__(self):
        self.userid = input("Enter Userid : ")
        self.score = input("Initial credit score: ")
        self.name = input("Enter name of the User: ")
        self.address = input("Enter billing address")
        __userfile = open("users.txt", "a+")
        __userfile.write("\n" + str(self.userid) + "\t" + str(self.score) + "\t" + self.name + "\t" + self.address)
        __userfile.close()

    def veiwUser(self, searchword):
        __userfile = open("users.txt", "r")
        __alluser = __userfile.readlines()
        __i = 0
        __found = False
        while __found == False and __i < len(__alluser):
            if searchword in __alluser[__i]:
                __found = True
            else:
                __i = __i + 1

        if (__found == True):
            print("User found : \n" + str(__alluser[__i]))
        else:
            print("User not found!!")
        __userfile.close()

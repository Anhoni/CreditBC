from block import block
from Users import Users

print("Select from list\n1. Create user\n2. Transact\n3. Check user")
menu = int(input("So What do you select: "))
if menu == 1:
    userread = open("users.txt", "r")
    alluser = userread.readlines()
    userread.close()
    if len(alluser) < 1:
        uid = 1
    else:
        uid = int(alluser[len(alluser) - 1].partition("\t")[0]) + 1
    Users(uid)
elif menu == 2:
    # block is to be added below
    block.Blockhash(block())
elif menu == 3:
    Users.veiwUser(Users, input("Enter user id or name or whatever: "))

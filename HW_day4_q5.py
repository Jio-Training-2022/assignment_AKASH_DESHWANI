# Build a banking system which has the following functionalities  :: 
# 2.1 Add account for a new user 
# 2.2 Add money to the account 
# 2.3 Withdraw money from the account 
# 2.4 Display balance for a particular user

def user_present (user_name):
    pass 
def addaccount(dic):
    user_name = input ("Enter new username :")
    if user_name in dic.keys():
        print("User already exits.")
        print("User_name and Account Balance ", user_name , dic[user_name])
    else:
        balance = 0
        dic[user_name] = balance
    print ("New account username and account balnace : ", user_name , "and ", balance)
    return(dic)

def credit(balance):
    c_amount = float (input("Enter amount to be deposited: "))
    balance = balance + c_amount
    print ("amount credited :", c_amount )
    print("Account balance :", balance)
    return (balance)

def debit(balance):
    d_amount = float (input("Enter amount to be deposited: "))
    if (d_amount > balance):
        print ("Insufficient Balance ")
    else:
        balance = balance - d_amount
        print ("amount debited :", d_amount )
    print("Account balance :", balance)
    return (balance)

def displayammount(balance):
    print("Account balance :",balance)
    pass

if __name__ == "__main__":
    exit_condition = False
    Bank_User = {}
    while (exit_condition != True):
        val = val = int(input("\n Welcome to Py Bank: \n Select the options \n To add user: Enter -> 1 \n To Credit amount: Enter -> 2 \n To debit ammount: Enter -> 3 \n To display account balance:  Enter -> 4 \n To EXIT: Enter -> 5 \n input:"))
        if (val == 1):
            Bank_User = addaccount(Bank_User)
        elif (val == 2):
            key = input("Enter user name :")
            Bank_User [key] = credit(Bank_User[key])
        elif (val == 3):
            key = input("Enter user name :")
            Bank_User [key] = debit(Bank_User[key])
        elif (val == 4):
            key = input("Enter user name :")
            displayammount(Bank_User[key])
        else:
            exit_condition = True
#Hw
#1. <Menu driven program that can
#a.depositt
#b.addaccount
#c.withdraw
#balance inquiry
#quit
class account:
    def __init__(self,balance:float):
        self.balance = balance
    def getbalnce(self):
        print("Your balance is ${} ".format(self.balance))
    def deposit(self,amt):
        if amt<=self.balance:
            resultantbalance= self.balance-amt
            print("Here you go!${}.The remaining balance is ${}".format(amt,resultantbalance))
        elif amt > self.balance:
            print(f'Sorry, we are unable to proceed with the transaction,because you have ${self.balance},which is not enough!')
        else:
            print('Transaction cancelled! Have a nice day!')
    def withdraw(self,amt:float):
        resultantbalance= self.balance+amt
        print(f'{amt} has been inserted to your bank account! Now you have ${resultantbalance}. Have a nice day!')

class Customer:
    customer={}
    def __init__(self,firstname:str,lastname:str,account:str):
        self.firstname,self.lastname,self.account= firstname,lastname,account
    def getfn(self):
        return self.firstname
    def getln(self):
        return self.lastname
    def getacc(self):
        return self.account
    def makeacc(self):
        insfname= input('What is your first name?')
        inslname= input('What is your last name?')
        insnewaccname= input('What will your account name be?')
        print(f'Your name is {insfname} {inslname}, with an account name of {insnewaccname}')
        self.customer['Account']=insnewaccname



def accmanager():
    print('1.Getbalance 2. Deposit 3. Withdraw 4. make an account 5. quit')
    action=int(input('What do you want to do?')) #1.Getbalance 2. Deposit 3. Withdraw 4. make an account 5. quit
    actionver1,actionver2 = account(500),Customer('Jonathan','Wenan','Blank_Chan7')

    if action == 1:
        actionver1.getbalnce()
        print('Have a nice day!')
    if action == 2:
        amountdepo=int(input('Type in the amount you want to deposit'))
        actionver1.deposit(amountdepo)
        print('have a nice day!')
    if action == 3:
        amountdepo=int(input('Type in the amount you want to Withdraw'))
        actionver1.withdraw(amountdepo)
        print('Have a nice day!')
    if action== 4:
        actionver2.makeacc()
        print('Have a nice day!')
    else:
        print('Have a nice day!')


accmanager()








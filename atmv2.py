class atm():
    balance=50000
    def __init__(self,withdraw=0,deposit=0):
        self.withdraw=withdraw
        self.deposit=deposit

    def cards():
        card_info=[{1234:4567},{3434,7878},]
        card=int(input("please enter the first four digits of your card"))
        pin=int(input("Please enter your pin"))
        counter=3

        while {card:pin} not in card_info and counter>0:
            counter-=1
            print("You entered the wrong info!\
            You have", counter,"left before you are locked out")
            card=int(input("please enter the first four digits of your card"))
            pin=int(input("Please enter your pin"))
            if counter<=0:
                print("Goodbye")
                return(False)

        if {card:pin} in card_info:
            return(True)

    def withdraw_money(self):
        if self.withdraw>self.balance:
            print("You can't withdraw that much money!\
            There is only $", balance, "in your account")
        elif self.withdraw<self.balance and self.withdraw>=0:
            atm.balance-=self.withdraw
            print("You withdraw $", self.withdraw, "And have $", self.balance,"left in your account")
            return(atm.balance)
        elif self.withdraw<0:
            print("You can't withdraw a negative amount!")

    def deposit_money(self):
        if self.deposit>=0:
            atm.balance+=self.deposit
            print("You made a deposit of $", self.deposit, " and your balance is $", self.balance)
            return(atm.balance)
        if self.deposit<0:
            print("You can't deposit a negative amount!")

    def check_balance(self):
        print("Your current balance is:", self.balance)

    def commands(self):
        print("Welcome to the ATM, what would you like to do?\
        withdraw\
        deposit\
        check balance")

        action=input("Enter your choice")
        if action=='withdraw':
            try:
                choice=atm(withdraw=int(input("Enter amount to withdraw")))
                atm.withdraw_money(choice)
            except ValueError:
                    print("You did not enter a number")
        elif action=='deposit':
            try:
                choice=atm(deposit=int(input("Enter amount to deposit")))
                atm.deposit_money(choice)
            except ValueError:
                    print("You did not enter a number")
        elif action=="check balance":
                choice=atm.check_balance(choice)
        else:
            print("You did not choose a valid option")




card_info=atm.cards()
if card_info==True:
    selection=atm()
    atm.commands(selection)
    choices=input("would you like to try another option? Y/N")
    while choices =='Y':
        selection=atm()
        atm.commands(selection)
        choices=input("would you like to try another option? Y/N")
    if choices=="N":
        print("Thank you for using the ATM, Goodbye!")
    else:
        print("You did not pick a choosable option. Please try again!")
        selection=atm()
        atm.commands(selection)
        choices=input("would you like to try another option? Y/N")

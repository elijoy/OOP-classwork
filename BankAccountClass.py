# The BankAccount class simulates a bank account.

class BankAccount:
    

# The __init__ method accepts an argument for
# the account's balance. It is assigned to
# the __balance attribute.

    def __init__(self, bal):
        self.__balance = bal

      # The deposit method makes a deposit into the
      # account.

    def deposit(self, amount):
        self.__balance += amount #increasing the amount that the indivdual put in

      # The withdraw method withdraws an amount
      # from the account.

    def withdraw(self, amount):
        if self.__balance >= abs(amount):
            self.__balance -= abs(amount)
        else:
            print('Error: Insufficient funds') #can't withdraw an amount you don't have

      # The get_balance method returns the
      # account balance.

    def get_balance(self): #why don't we have (self,object) dont need additional information
        return self.__balance



    def __str__(self):
        return 'The balance is $' + format(self.__balance, ',.2f')

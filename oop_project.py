from bank_account import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.getBalance()
Sara.getBalance()

Sara.deposit(400)

Dave.withdraw(100)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(200, Sara)
Sara.getBalance()

Jim = InterestRewardAcct(1000, "Jim")
Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100,Dave)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.getBalance()
Blaze.deposit(100)

Blaze.transfer(1000, Sara)

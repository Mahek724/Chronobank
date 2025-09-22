from models.user import User
from models.accounts import SavingTimeAccount, InvestorAccount, LoanAccount
from models.transactions import TransferTransaction, LoanTransaction, InvestmentTransaction

class ChronoBankFacade: # Facade class
    def create_user(self, user_id, name, user_type): # Create user method
        return User(user_id, name, user_type) # Retrun a user object

    def create_basic_account(self, acc_id, user):
        return SavingTimeAccount(acc_id, user, 0)

    def create_investor_account(self, acc_id, user, interest_rate):
        return InvestorAccount(acc_id, user, 0, interest_rate)

    def create_loan_account(self, acc_id, user, loan_limit):
        return LoanAccount(acc_id, user, 0, loan_limit)

    def deposit(self, account, amount): # Deposit method
        account.deposit(amount)

    def transfer(self, sender, receiver, amount): # Transfer method
        transfer = TransferTransaction(sender, receiver, amount) # Create a transfer transaction
        transfer.execute() # Execute the transfer

    def take_loan(self, loan_account, amount):
        loan = LoanTransaction(loan_account, amount)
        loan.execute()

    def invest(self, account):
        investment = InvestmentTransaction(account)
        investment.execute()

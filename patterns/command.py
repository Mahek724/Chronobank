class Command:
    def execute(self):
        pass

class DepositCommand(Command): # Command
    def __init__(self, account, amount): 
        self.account = account
        self.amount = amount

    def execute(self): 
        self.account.deposit(self.amount)

class WithdrawCommand(Command):
    def __init__(self, account, amount):
        self.account = account
        self.amount = amount

    def execute(self):
        self.account.withdraw(self.amount)


class TransactionInvoker: # Invoker
    def __init__(self):
        self.history = [] # keeps track of executed commands 

    def execute_command(self, command):  # executes a command and adds it to the history
        command.execute()
        self.history.append(command)

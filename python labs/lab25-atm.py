#  Lab24 ATM


class ATM:
    """
    ATM that allows you to run methods on balance for accounts.
    """
    def __init__(self, balance=0):
        self.balance = balance
        self.history = []

    def check_balance(self):
        """
        returns the account balance
        """
        return f'Your balance is ${self.balance}'

    def deposit(self, amount):
        """
        deposits the given amount in the account
        """
        self.balance += amount
        self.history.append(f'Deposted +${amount}')
        return f'You have deposited ${amount}.'

    def check_withdrawal(self, amount):
        """
        returns true if the withdrawn amount
        doesn't put the account in the negative
        """
        return self.balance > amount

    def withdraw(self, amount):
        """
        withdraws the amount from the account and returns it
        """
        if self.check_withdrawal(amount) is True:
            self.balance -= amount
            self.history.append(f'Withdrew -${amount}')
            return f'You have withdrawn ${amount}.'
        else:
            return f'Insufficient Funds: Unable to withdraw {amount}'

    def account_history(self):
        """
        Prints transaction history
        """
        return '\n'.join(self.history) + '\n' + self.check_balance()


account = ATM()
loop = True
valid_inputs = ['b', 'balance', 'd', 'deposit',
                'w', 'withdraw', 'h', 'history', 'x', 'exit']
commands = """
    Commands:
    (B)alance
    (D)eposit
    (W)ithdraw
    (H)istory
    E(x)it
    """
while loop:
    print('='*60)

    while True:
        print(f"Please select a command {commands}")
        user_input = input("> ").lower().strip()
        if user_input in valid_inputs:
            break
        print("Invalid input")
    print("="*60)

    if user_input.startswith('b'):
        print(account.check_balance())

    elif user_input.startswith('h'):
        print(account.account_history())

    elif user_input in ['d', 'deposit', 'w', 'withdraw']:
        while True:
            amount = input("How much money would you like deposit/withdraw?\n> ")
            if amount.isdigit():
                amount = int(amount)
                break
            else:
                print("Invalid Input")
        if user_input.startswith('d'):
            print(account.deposit(amount))

        elif user_input.startswith('w'):
            print(account.withdraw(amount))

    else:
        print(f"Printing receipt")
        loop = False

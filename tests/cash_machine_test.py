from cash_machine.cash_machine import CashMachine


def check_withdrawal_100_test():
    cm = CashMachine()
    assert cm.cash_notes_for_withdrawal(100) == {"100": 1}

from nose.tools import eq_

from cash_machine.cash_machine_display import CashMachineDisplay


def check_withdrawal_100_test():
    cmd = CashMachineDisplay()
    eq_(cmd.message_for_withdrawal(100), "Entregar 1 nota(s) de R$ 100,00")


def check_withdrawal_50_test():
    cmd = CashMachineDisplay()
    eq_(cmd.message_for_withdrawal(50), "Entregar 1 nota(s) de R$ 50,00")


def check_withdrawal_200_test():
    cmd = CashMachineDisplay()
    eq_(cmd.message_for_withdrawal(200), "Entregar 2 nota(s) de R$ 100,00")


def check_withdrawal_150_test():
    cmd = CashMachineDisplay()
    eq_(cmd.message_for_withdrawal(150), "Entregar 1 nota(s) de R$ 100,00, 1 nota(s) de R$ 50,00")

from nose.tools import eq_

from cash_machine.cash_machine_display import CashMachineDisplay


def check_withdrawal_100_test():
    cmd = CashMachineDisplay()
    eq_(
        cmd.message_for_withdrawal(100),
        "Entregar 1 nota(s) de R$ 100,00"
    )


def check_withdrawal_50_test():
    cmd = CashMachineDisplay()
    eq_(
        cmd.message_for_withdrawal(50),
        "Entregar 1 nota(s) de R$ 50,00"
    )


def check_withdrawal_200_test():
    cmd = CashMachineDisplay()
    eq_(
        cmd.message_for_withdrawal(200),
        "Entregar 2 nota(s) de R$ 100,00"
    )


def check_withdrawal_150_test():
    cmd = CashMachineDisplay()
    eq_(
        cmd.message_for_withdrawal(150),
        "Entregar 1 nota(s) de R$ 100,00, 1 nota(s) de R$ 50,00"
    )


def check_withdrawal_80_test():
    cmd = CashMachineDisplay()
    eq_(
        cmd.message_for_withdrawal(80),
        "Entregar 1 nota(s) de R$ 50,00, 1 nota(s) de R$ 20,00, 1 nota(s) de R$ 10,00"
    )


def check_withdrawal_30_test():
    cmd = CashMachineDisplay()
    eq_(
        cmd.message_for_withdrawal(30),
        "Entregar 1 nota(s) de R$ 20,00, 1 nota(s) de R$ 10,00"
    )


def check_withdrawal_0_test():
    cmd = CashMachineDisplay()
    eq_(
        cmd.message_for_withdrawal(0),
        "Impossível de sacar este valor!"
    )


def check_withdrawal_negative_number_test():
    cmd = CashMachineDisplay()
    eq_(
        cmd.message_for_withdrawal(-50),
        "Impossível de sacar este valor!"
    )


def check_withdrawal_2540_test():
    cmd = CashMachineDisplay()
    eq_(
        cmd.message_for_withdrawal(2540),
        "Entregar 25 nota(s) de R$ 100,00, 2 nota(s) de R$ 20,00"
    )


def check_withdrawal_with_impossible_value_test():
    cmd = CashMachineDisplay()
    eq_(
        cmd.message_for_withdrawal(2537),
        "Impossível de sacar este valor!"
    )

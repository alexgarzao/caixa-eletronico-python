from cash_machine.cash_machine import CashMachine


def check_withdrawal_100_test():
    cm = CashMachine()
    __assert_result(cm.cash_notes_for_withdrawal(100), {100: 1, 50: 0, 20: 0, 10: 0})


def check_withdrawal_50_test():
    cm = CashMachine()
    __assert_result(cm.cash_notes_for_withdrawal(50), {100: 0, 50: 1, 20: 0, 10: 0})


def __assert_result(result, expected):
    assert result == expected, \
        "Resultado={} Esperado={}".format(result, expected)

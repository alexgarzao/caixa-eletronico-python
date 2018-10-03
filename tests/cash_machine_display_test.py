from cash_machine.cash_machine_display import CashMachineDisplay


def check_withdrawal_100_test():
    cmd = CashMachineDisplay()
    __assert_result(cmd.message_for_withdrawal(100), "Entregar 1 nota(s) de R$ 100,00")


def __assert_result(result, expected):
    assert result == expected, \
        "Resultado={} Esperado={}".format(result, expected)

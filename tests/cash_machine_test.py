from nose.tools import eq_

from cash_machine.cash_machine import CashMachine


def check_withdrawal_100_test():
    cm = CashMachine()
    eq_(cm.cash_notes_for_withdrawal(100), {100: 1, 50: 0, 20: 0, 10: 0})


def check_withdrawal_50_test():
    cm = CashMachine()
    eq_(cm.cash_notes_for_withdrawal(50), {100: 0, 50: 1, 20: 0, 10: 0})


def check_withdrawal_200_test():
    cm = CashMachine()
    eq_(cm.cash_notes_for_withdrawal(200), {100: 2, 50: 0, 20: 0, 10: 0})


def check_withdrawal_150_test():
    cm = CashMachine()
    eq_(cm.cash_notes_for_withdrawal(150), {100: 1, 50: 1, 20: 0, 10: 0})


def check_withdrawal_80_test():
    cm = CashMachine()
    eq_(cm.cash_notes_for_withdrawal(80), {100: 0, 50: 1, 20: 1, 10: 1})


def check_withdrawal_30_test():
    cm = CashMachine()
    eq_(cm.cash_notes_for_withdrawal(30), {100: 0, 50: 0, 20: 1, 10: 1})


def check_withdrawal_0_test():
    cm = CashMachine()
    eq_(cm.cash_notes_for_withdrawal(0), {100: 0, 50: 0, 20: 0, 10: 0})


def check_withdrawal_negative_number_test():
    cm = CashMachine()
    eq_(cm.cash_notes_for_withdrawal(-20), {100: 0, 50: 0, 20: 0, 10: 0})


def check_withdrawal_2540_test():
    cm = CashMachine()
    eq_(cm.cash_notes_for_withdrawal(2540), {100: 25, 50: 0, 20: 2, 10: 0})


def check_withdrawal_with_impossible_value_test():
    cm = CashMachine()
    eq_(cm.cash_notes_for_withdrawal(33), {100: 0, 50: 0, 20: 0, 10: 0})

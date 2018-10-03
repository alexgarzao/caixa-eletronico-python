from nose.tools import eq_

from cash_machine.cash_machine import CashMachine, CashNotes


def withdrawal_100_test():
    cm = CashMachine()
    eq_(
        cm.cash_notes_for_withdrawal(100),
        CashNotes(1, 0, 0, 0)
    )


def withdrawal_50_test():
    cm = CashMachine()
    eq_(
        cm.cash_notes_for_withdrawal(50),
        CashNotes(0, 1, 0, 0)
    )


def withdrawal_200_test():
    cm = CashMachine()
    eq_(
        cm.cash_notes_for_withdrawal(200),
        CashNotes(2, 0, 0, 0)
    )


def withdrawal_150_test():
    cm = CashMachine()
    eq_(
        cm.cash_notes_for_withdrawal(150),
        CashNotes(1, 1, 0, 0)
    )


def withdrawal_80_test():
    cm = CashMachine()
    eq_(
        cm.cash_notes_for_withdrawal(80),
        CashNotes(0, 1, 1, 1)
    )


def withdrawal_30_test():
    cm = CashMachine()
    eq_(
        cm.cash_notes_for_withdrawal(30),
        CashNotes(0, 0, 1, 1)
    )


def withdrawal_0_test():
    cm = CashMachine()
    eq_(
        cm.cash_notes_for_withdrawal(0),
        None
    )


def withdrawal_negative_number_test():
    cm = CashMachine()
    eq_(
        cm.cash_notes_for_withdrawal(-20),
        None
    )


def withdrawal_2540_test():
    cm = CashMachine()
    eq_(
        cm.cash_notes_for_withdrawal(2540),
        CashNotes(25, 0, 2, 0)
    )


def withdrawal_with_impossible_value_test():
    cm = CashMachine()
    eq_(
        cm.cash_notes_for_withdrawal(33),
        None
    )

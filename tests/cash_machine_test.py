from nose.tools import eq_

from cash_machine.cash_machine import CashMachine, CashNotes
from cash_machine.cash_note import CashNote


def withdrawal_100_test():
    cm = CashMachine()
    eq_(
        cm.cash_notes_for_withdrawal(100),
        CashNotes([CashNote(100, 1), CashNote(50, 0), CashNote(20, 0), CashNote(10, 0)])
    )


def withdrawal_50_test():
    cm = CashMachine()
    eq_(
        cm.cash_notes_for_withdrawal(50),
        CashNotes([CashNote(100, 0), CashNote(50, 1), CashNote(20, 0), CashNote(10, 0)])
    )


def withdrawal_200_test():
    cm = CashMachine()
    eq_(
        cm.cash_notes_for_withdrawal(200),
        CashNotes([CashNote(100, 2), CashNote(50, 0), CashNote(20, 0), CashNote(10, 0)])
    )


def withdrawal_150_test():
    cm = CashMachine()
    eq_(
        cm.cash_notes_for_withdrawal(150),
        CashNotes([CashNote(100, 1), CashNote(50, 1), CashNote(20, 0), CashNote(10, 0)])
    )


def withdrawal_80_test():
    cm = CashMachine()
    eq_(
        cm.cash_notes_for_withdrawal(80),
        CashNotes([CashNote(100, 0), CashNote(50, 1), CashNote(20, 1), CashNote(10, 1)])
    )


def withdrawal_30_test():
    cm = CashMachine()
    eq_(
        cm.cash_notes_for_withdrawal(30),
        CashNotes([CashNote(100, 0), CashNote(50, 0), CashNote(20, 1), CashNote(10, 1)])
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
        CashNotes([CashNote(100, 25), CashNote(50, 0), CashNote(20, 2), CashNote(10, 0)])
    )


def withdrawal_with_impossible_value_test():
    cm = CashMachine()
    eq_(
        cm.cash_notes_for_withdrawal(33),
        None
    )

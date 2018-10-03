from nose.tools import eq_, ok_

from cash_machine.cash_notes import CashNotes
from cash_machine.cash_note import CashNote


def sequence_test():
    cn = CashNotes()
    eq_(cn.get_next_note(), CashNote(100))
    eq_(cn.get_next_note(), CashNote(50))
    eq_(cn.get_next_note(), CashNote(20))
    eq_(cn.get_next_note(), CashNote(10))
    eq_(cn.get_next_note(), CashNote(0))


def are_equal_test():
    cn1 = CashNotes()
    cn2 = CashNotes()
    eq_(cn1, cn2)


def are_equal_with_specific_values_test():
    cn1 = CashNotes(1, 2, 3, 4)
    cn2 = CashNotes(1, 2, 3, 4)
    eq_(cn1, cn2)


def are_not_equal_with_specific_values_test():
    cn1 = CashNotes(1, 2, 3, 4)
    cn2 = CashNotes(1, 2, 8, 4)
    ok_(cn1 != cn2, "%r == %r" % (cn1, cn2))

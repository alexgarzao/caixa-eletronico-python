from nose.tools import eq_, ok_

from cash_machine.cash_note import CashNote


def value_test():
    cn = CashNote(100)
    eq_(cn.value(), 100)

    cn = CashNote(50)
    eq_(cn.value(), 50)


def used_test():
    cn = CashNote(25)
    eq_(cn.used(), 0)

    cn.inc_used()
    eq_(cn.used(), 1)

    cn.inc_used()
    eq_(cn.used(), 2)


def are_equal_test():
    cn1 = CashNote(10)
    cn2 = CashNote(10)
    eq_(cn1, cn2)


def are_not_equal_test():
    cn1 = CashNote(10)
    cn2 = CashNote(20)
    ok_(cn1 != cn2, "%r == %r" % (cn1, cn2))

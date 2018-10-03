from cash_machine.cash_notes import CashNotes


class CashMachine:
    def cash_notes_for_withdrawal(self, value):
        cash_notes = CashNotes()

        while value > 0:
            cash_note = cash_notes.get_next_note()
            if cash_note.value() == 0:
                return None

            while value >= cash_note.value():
                cash_note.inc_used()
                value -= cash_note.value()

            if value == 0:
                return cash_notes

        return None

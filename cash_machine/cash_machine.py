class CashMachine:
    def __init__(self):
        self.__available_cash_notes = [100, 50, 20, 10]

    def cash_notes_for_withdrawal(self, value):
        cash_notes = {note: 0 for note in self.__available_cash_notes}

        cash_note_idx = 0
        while value > 0:
            cash_note = self.__available_cash_notes[cash_note_idx]
            if cash_note > value:
                cash_note_idx += 1
                continue
            cash_notes[cash_note] += 1
            value -= cash_note

        return cash_notes

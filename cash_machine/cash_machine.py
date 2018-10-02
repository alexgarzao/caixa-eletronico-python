class CashMachine:
    def __init__(self):
        self.__available_cash_notes = [100, 50, 20, 10]

    def cash_notes_for_withdrawal(self, value):
        self.cash_note_idx = 0
        cash_notes = self.__initial_cash_notes()
        cash_note = self.__get_next_cash_note()

        while value > 0:
            while value >= cash_note:
                cash_notes[cash_note] += 1
                value -= cash_note

            if value == 0:
                return cash_notes

            cash_note = self.__get_next_cash_note()
            if cash_note == 0:
                return self.__initial_cash_notes()

        return self.__initial_cash_notes()

    def __initial_cash_notes(self):
        return {note: 0 for note in self.__available_cash_notes}

    def __get_next_cash_note(self):
        if self.__no_more_notes():
            return 0

        cash_note = self.__available_cash_notes[self.cash_note_idx]
        self.cash_note_idx += 1
        return cash_note

    def __no_more_notes(self):
        return self.cash_note_idx == len(self.__available_cash_notes)

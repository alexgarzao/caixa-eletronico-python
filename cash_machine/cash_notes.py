from .cash_note import CashNote


class CashNotes:
    def __init__(self, notes=None):
        if not notes:
            notes = [CashNote(100), CashNote(50), CashNote(20), CashNote(10)]

        self.__available_cash_notes = notes
        self.__cash_note_idx = 0

    def get_next_note(self):
        if self.__no_more_notes():
            return CashNote(0)

        cash_note = self.__available_cash_notes[self.__cash_note_idx]
        self.__cash_note_idx += 1
        return cash_note

    def __no_more_notes(self):
        return self.__cash_note_idx == len(self.__available_cash_notes)

    def __eq__(self, other):
        return self.__available_cash_notes == other.__available_cash_notes

    def __iter__(self):
        self.__iter_idx = 0
        return self

    def __next__(self):
        if self.__iter_idx == len(self.__available_cash_notes):
            raise StopIteration

        result = self.__available_cash_notes[self.__iter_idx]
        self.__iter_idx += 1
        return result

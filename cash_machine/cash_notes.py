from .cash_note import CashNote


class CashNotes:
    """ Classe responsável por registrar as notas existentes no caixa eletrônico."""
    def __init__(self, note_100_used=0, note_50_used=0, note_20_used=0, note_10_used=0):
        self.__available_cash_notes = [
            CashNote(100, note_100_used),
            CashNote(50, note_50_used),
            CashNote(20, note_20_used),
            CashNote(10, note_10_used)
        ]
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

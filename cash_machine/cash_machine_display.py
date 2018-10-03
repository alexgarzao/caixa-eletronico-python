from .cash_machine import CashMachine


class CashMachineDisplay:
    def __init__(self):
        self.cm = CashMachine()

    def message_for_withdrawal(self, value):
        cash_notes = self.cm.cash_notes_for_withdrawal(value)
        return self.__format_message(cash_notes)

    def __format_message(self, cash_notes):
        message = ""

        for cash_note, count in cash_notes.items():
            if count == 0:
                continue

            message += "{} nota(s) de R$ {},00, ".format(count, cash_note)

        if message:
            message = "Entregar " + message[:-2]

        return message

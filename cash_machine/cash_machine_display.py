from .cash_machine import CashMachine


class CashMachineDisplay:
    "Classe responsável por gerar o texto indicando as notas necessárias para realizar o saque."
    def __init__(self):
        self.cm = CashMachine()

    def message_for_withdrawal(self, value):
        cash_notes = self.cm.cash_notes_for_withdrawal(value)
        return self.__format_message(cash_notes)

    def __format_message(self, cash_notes):
        if not cash_notes:
            return "Impossível de sacar este valor!"

        message = ""

        for note in cash_notes:
            if note.used() == 0:
                continue

            message += "{} nota(s) de R$ {},00, ".format(note.used(), note.value())

        message = "Entregar " + message[:-2]

        return message

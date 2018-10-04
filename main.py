import sys

from cash_machine.cash_machine_display import CashMachineDisplay


def main(args):
    if len(args) != 2 or not args[1].isdecimal():
        print("Como usar:")
        print("\tpython main.py <VALOR>")
        print("\tonde <VALOR> deve ser um argumento numérico\n")
        sys.exit(1)

    cmd = CashMachineDisplay()
    print(cmd.message_for_withdrawal(int(args[1])))


if __name__ == "__main__":
    main(sys.argv)

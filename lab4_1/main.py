from random import randint


class Ticket():
    def __init__(self, value, type, number):
        self.value = value
        self.type = type
        self.number = number

    def stud(self):
        self.value = self.value * 0.5
        self.type = "Student"

    def earl(self):
        self.value = self.value * 0.7
        self.type = "Early"

    def late(self):
        self.value = self.value * 1.2
        self.type = "Late"

    def print(self):
        print(self.type, " ", self.number, " ", "{:.2f}".format(self.value), " $")

    def print_val(self):
        print("{:.2f}".format(self.value), " $")


tickets = []
N = 6
while True:
    print("Choose number of action:\n1. Buy a ticket\n2.Print information about ticket\n"
          "3.Find ticket by number\n 4.Find out the price of ticket\n 5.Out ")
    ch = int(input("Your choice:"))
    if ch == 1 or ch == 4:
        temp = Ticket(N, "", randint(0, 999))
        while True:
            print("Choose ticket type:\n1.Ordinary ticket\n2.Student ticket\n3.Early ticket\n 4.Late ticket")
            ch2 = int(input("Your choice:"))
            if ch2 == 1:
                temp.type = "Ordinary"
            elif ch2 == 2:
                temp.stud()
            elif ch2 == 3:
                temp.earl()
            elif ch2 == 4:
                temp.late()
            else:
                print("Please, input correct data")
                continue
            if ch == 1:
                temp.print()
                tickets.append(temp)
            else:
                temp.print_val()
            break

    elif ch == 2 or ch == 3:
        count = 0
        print("Please, write number of number:")
        num = int(input())
        for i in tickets:
            if i.number == num:
                count += 1
                if ch == 2:
                    i.print()
                else:
                    print("Ticket exists")
            if count == 0:
                print("Ticket doesn`t exist")
    elif ch == 5:
        break
    else:
        print("Incorrect data")

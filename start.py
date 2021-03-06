# class Person:
#     name = "Bill"

#     def show_person(self):
#         print("Hello", self.name)


# Bill = Person()  # екземпляр класу
# Bill.show_person()
# Tom = Person()
# Tom.name = "Tom"
# Tom.show_person()

# class Person:
#     def __init__(self, name):
#         self.__name = name
#         print("Person constructor", self.__name)
#     def show_person(self):
#         print("Hello", self.__name)
#     def __del__(self):
#         print("Person destructor", self.__name)

# Jack = Person("Jack")
# Jack.show_person()
# Tom = Person("Tom")
# Tom.show_person()

# class Person:
#     def __init__(self, name):
#         self.__name = name

#     def get_name(self):  # геттер
#         return(self.__name)

#     def set_name(self, new_name):
#         if self.__name == new_name:
#             print("The same name")
#         else:
#             self.__name = new_name
#             return new_name


# Jack = Person("Jack")
# print(Jack.get_name())


"""
ООП
Написати клас "Банківський рахунок" (Account), який містить:
Номер рахунку
Розмір коштів на рахунку
Назва валюти рахунку (рублі, гривні, евро тощо), для позначення якої можна скористатись одним символом: R, G, E, $ тощо
Забезпечити можливість:
-Відкривати рахунок та первинно вносити гроші на рахунок
-Знімати гроші з рахунку
-Докладати гроші на рахунок

"""
from random import randint


class Account:
    def __init__(self, card_number, amount, currancy):
        self.__card_number = card_number
        self.__amount = amount
        self.__currancy = currancy
        print("Account constructor")

    def show_info(self):
        print("Card number: ", self.__card_number, "\nAmount: ",
              self.__amount, "\nCurrancy: ", self.__currancy)

    def get_cash(self):
        money_get = int(input("How much money u want to take?"))
        self.__amount -= money_get
        return self.__amount

    def set_cash(self, money_set):
        money_set = int(input("How much u want to add?"))
        self.__amount += money_set
        return self.__amount


# amount = int(input("Enter money: "))
# currancy = input("Enter currancy:UAH USD EUR => ")
# card_number = randint(1000000, 9999999)

# credit_card = Account(card_number, amount, currancy)
# credit_card.show_info()

while True:
    print("Welcome to the BANK")
    question1 = int(input(
        "MENU\n1. Register a new account\n2. Show account\n3. Take money\n4. Add money\n0. EXIT\n\tYour action: "))
    if question1 == 1:
        amount = int(input("How much money?:\n"))
        question2 = int(
            input("Choose currancy\n1.USD\n2.EURO\n3.UAH\n4.RUB\nYour choice: "))
        if question2 == 1:
            currancy = "USD"
        elif question2 == 2:
            currancy = "EURO"
        elif question2 == 3:
            currancy = "UAH"
        elif question2 == 4:
            currancy = "RUB"

        card_number = randint(10000000000000000, 99999999999999999)
        input("ACCOUNT CREATED\nTap Enter to go to menu")
    elif question1 == 2:
        credit_card = Account(card_number, amount, currancy)
        credit_card.show_info()
        input("Enter for exit in menu")
        print("*************************************")
    elif question1 == 3:
        amount = credit_card.get_cash()
        print("_________________________")
        print("Balance:", amount, currancy)
        print("_________________________")
    elif question1 == 4:
        amount = credit_card.set_cash()
        print("_________________________")
        print("Balance:", amount, currancy)
        print("_________________________")
    elif question1 == 0:
        break
    else:
        print("What's wrong! BYE!")
        break

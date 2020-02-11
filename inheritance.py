class Person:
    def __init__(self, name: str, surname: str, age: int):
        self.__name: str = name
        self.__surname: str = surname
        self.__age: int = age

    def show_person_info(self):
        print("Name: ", self.__name, "\nSurname: ",
        self.__surname, "\nAge: ", self.__age)

    @property
    def surname(self):
        return self.__surname

    @property
    def age(self):
        return self.__age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @surname.setter
    def surname(self, new_surname: str):
        self.__surname = new_surname

    @age.setter
    def age(self, new_age: int):
        self.__age = new_age

# gvido = Person("Gvido", "Van Rossum", 46)
# gvido.show_person_info()
# print("-----------------------------------------")
# print("property before ", gvido.name)
# gvido.name = "Petya"
# gvido.show_person_info()
# print("property after ", gvido.name)


class Junior (Person):
    def __init__(self, name: str, surname: str, age: int, skills: str, position: str):
        Person.__init__(self, name, surname, age)
        self.__skills = skills
        self.__position = position

    def show_person_info(self):
        print("Name: ", self.name, "\nSurname: ", self.surname, "\nAge: ",
        self.age, "\nPosition: ", self.__position, "\nSkills: ", self.__skills)


jun = Junior("Adam", "Dobson", 23, "Write code using Stack Overflow",
"Full Stack Overflow developer")

jun.show_person_info()
jun.name = "Adamus"
jun.surname = "Dobsunos"
jun.age = 24
jun.show_person_info()



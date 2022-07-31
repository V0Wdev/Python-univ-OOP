class Student:
    def __init__(self, name, surname, patronymic, year_born, year_entrance):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.year_born = year_born
        self.year_entrance = year_entrance


class StudentState(Student):
    def scholar(self, scholar):
        self.scholar = scholar
        self.payment = False

    def contractor(self, payment):
        self.payment = payment
        self.scholar = False


class Group(Student):
    def __init__(self, num_group, list_of_students):
        self.num_group = num_group
        self.list_of_students = list(list_of_students)

    def print(self):
        for i in self.list_of_students:
            print("\nПолное имя =", i.name, i.surname, i.patronymic,
                  "\nГод рождения =", i.year_born,
                  "\nГод поступления =", i.year_entrance,
                  "\nНомер группы =", self.num_group)
            if i.scholar != False:
                print("Студент бюджетник. Его стипендия на данный момент =", i.scholar)
            elif i.payment != False:
                print("Студент контрактник. Стоимость обучения =", i.payment)


class Discipline:
    def __init__(self, name_desc, num_cred, sem):
        self.name_desc = name_desc
        self.num_cred = num_cred
        self.sem = sem


class Teacher:
    def __init__(self, name, surname, patronymic, year_born, year_experience, list_of_discipline):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.year_born = year_born
        self.year_experience = year_experience
        self.list_of_discipline = list(list_of_discipline)

    def total_subject(self):
        value_discipline = 0
        num_creds = 0
        if len(self.list_of_discipline) != 0:
            for i in self.list_of_discipline:
                value_discipline += 1
                num_creds += i.num_cred
            print("\nКоличество дисциплин =", value_discipline,
                  "\nКолличество кредитов =", num_creds)

    def print(self):
        for i in self.list_of_discipline:
            print("\nПолное имя =", self.name, self.surname, self.patronymic,
                  "\nDГод рождения =", self.year_born,
                  "\nОпыт работы =", self.year_experience,
                  "\nИмя дисциплины =", i.name_desc,
                  "\nКолличество кредитов =", i.num_cred,
                  "\nКоличестов дисциплин в семместре =", i.sem)


while True:
    st1 = StudentState("Кузьменко", "Владимир", "Максимович", "10.10.2001", "01.09.2019")
    st1.scholar("1980 гривен")
    st2 = StudentState("Дыба", "Екатерина", "Сергеевна", "20.01.2002", "01.09.2019")
    st2.scholar("1980 гривен")
    st3 = StudentState("Даценко", "Владислав", "Анатольевич", "14.05.2002", "01.09.2018")
    st3.scholar("0 гривен")
    list_of_students = [st1, st2, st3]

    group = Group("535в", list_of_students)

    disc1 = Discipline("Технологии Программирования", 10, 2)
    disc2 = Discipline("Английский язык", 5, 4)
    list_of_discipline = [disc1, disc2]

    teacher = Teacher("Феодосий", "Эзреаль", "Адамович", "18.01.1981", "15 years", list_of_discipline)

    while True:
        print("\nВыберите операцию:" +
              "\n(1) - Вывод информации о студентах" +
              "\n(2) - Вывод информации о преподавателе" +
              "\n(3) - Вывести список учебных дисциплин в данный момент")
        a = int(input("Ваш выбор = "))
        if a == 1:
            group.print()
        elif a == 2:
            teacher.print()
        elif a == 3:
            teacher.total_subject()
        else:
            print("Ошибка ввода данных.")
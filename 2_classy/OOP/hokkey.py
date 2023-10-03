# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def get_info(self):
#         print(f'cat {self.name}, {self.age} age')
#
#     def speak(self, sound):
#         self.sound = sound
#         print(f'miu miu {sound}')
# dimka = Cat("mir", 6)
# print(dimka.__dict__)
# dimka.get_info()
# dimka.speak('miu miu')

# Делегирование
class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def can_breathe(self):
        print('могу дышать')

class Teacher(Person):
    def __init__(self, name, lastname, age):
        # self.name = name
        # self.lastname = lastname
        super().__init__(name, lastname)
        self.age = age

    def can_breathe(self):
        print('учитель дышит')
        super().can_breathe()
p2 = Person('Denis', 'Denisov')
t2 = Teacher("iVAN", "Ivanov", 45)
print(p2.name, p2.lastname)
print(t2.name, t2.lastname, t2.age)
p2.can_breathe()
t2.can_breathe()


# # наследование
# class Animal:
#     def can_run(self):
#         print('i can run')
# class Dogs:
#     def can_burck(self):
#         print('i can burck')
#
# class Bigle(Animal, Dogs):
#     def can_sleep(self):
#         print('i can sleep')
# # встроенная ф-ция mro которая показывает иерархию наследования
# print(Bigle.mro())




# class Car:
#     age = 2020
#     name = 'Priora'
#     make = 'Lada'
#     def start(self, name, make='Audi'):
#         self.name = name
#         self.make = make
#         print(f'start, {self.name} {make}')
#     def get_age(self):
#         print(f'у машины {self.make} {self.name}')
#     def stop(self):
#         print('stop')
# c1 = Car()
# print(c1.make)
# c1.get_age()
# c1.start("h", "gggggggggg")
# c1.get_age()

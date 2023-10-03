# наследование
class Animal:
    def can_run(self):
        print('i can run')
class Dogs:
    def can_burck(self):
        print('i can burck')

class Bigle(Animal, Dogs):
    def can_sleep(self):
        print('i can sleep')
# встроенная ф-ция mro которая показывает иерархию наследования
print(Bigle.mro())




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

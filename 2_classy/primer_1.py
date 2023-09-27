class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def hello(self):
        return f'Hello {self.name} {self.surname} '



class Tester(Person):
    def __init__(self, name, surname, languige):
        super().__init__(name, surname)
        self.languige = languige
    def te(self):
        return 'Ilove'
tester_1 = Tester('Max', 'Popov', 'eng')
print(tester_1.hello())
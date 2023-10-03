# данные меняются с помощью ф-ий get и set



class Person:
    age = 35
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def hello(self):
        return f'Hello {self.name} {self.surname} '

    def set_name(self, new_name):
        self.name = new_name


    @staticmethod  # декоратор @staticmethod превращает метод определенный внутри класса
    # в обычную ф-ю, которая не имеет доступа к экземпляру класса self поэтому ее можно вызвать
    # без создания экземпляра класса. те Person.start() или Person('alex', 'baker').start()

    def start():
        print('выводим текст')



class Tester(Person):
    def __init__(self, name, surname, languige):
        super().__init__(name, surname)
        self.languige = languige
    def te(self):
        return 'Ilove'
tester_1 = Tester('Max', 'Popov', 'eng')
print(tester_1.hello())
person_1 = Person('alex', 'baker')
person_1.set_name('sasha')
print(person_1.hello())
Person.start()


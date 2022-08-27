class University:
    def __init__(self, name: str, location: str, list_direction: list) -> None:
        self.name = name
        self.location = location
        self.list_direction = list_direction
        
    def info(self):
        return f"Название нашего университета: {self.name} место нахождение: {self.location} направление{self.list_direction}"

    def __str__(self) -> str:
        return self.name

manas = University('manas','manasa 165',['it','git','doctor','electrik',])
politeh = University('politeh','ahunbaeva',['it','git','doctor','electrik',])

class Cart:
    def __init__(self, number: int, data: str, cv: str, balance: int) -> None:
        self.number = number
        self.data = data
        self.cv = cv 
        self.balance = balance
        pass

class Student:
    def __init__(self, full_name: str, university: University,start_year: int) -> None:
        self.full_name = full_name
        self.university = university
        self.start_year = start_year

    def __str__(self) -> str:
        return self.full_name
        
argen = Student('Argen Kochkonbaev', politeh , 2022)
        
bael = Student('Bael Gaparov', manas , 2022)

tilek = Student('Tilekov Tilek', 'manas' , 2020)

student = [tilek, argen, tilek]
university = [manas, politeh]


def create_new_student(Student ,manas, politeh, university):
    name = input('введите имя: ')
    univer = input('Выбери универ: ')
    for i, name in enumerate(univer, 1):
        print(i, name)
    if university == 1:
        university == manas
    elif university == 2:
        university == politeh
    year = input('Введите год: ')
    student = Student(name, univer, year)

student.append(student)

info = student.university.info()
print(info)


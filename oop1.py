# class Product:
#     name = 'Фен'
#     price = '450'
#     desc = 'это хороший фен'
#     code = 34234

# p = Product()

# p.price = 500
# print(p.name)
# print(p.price)


# class Car:
#     name = 'BMW'
#     marka = 'M8'
#     color = 'black'
#     mator = 'M1'

# c = Car()

# print(c.name)


# class Cat:
#     def __init__(self, name , age, poroda, gender, lenght, kg) -> None:

#         self.name = name
#         self.age = age
#         self.poroda = poroda
#         self.gender = gender
#         self.lenght = lenght
#         self.kg = kg

#     def run(self):
#         print('побежал')

#     def mur(self):
#         print(f'{self.name} мурчит')

# tom = Cat('Tom','2','russian','male','34cm','5kg')
# jack = Cat('Jack','3','american','male','41cm','7kg')
# mary = Cat('Mary','1','russian','female','31cm','4kg')
# jackle = Cat('Jackle','4','russian','male','35cm','6kg')

# cats = [tom, jack, mary, jackle]

# count = 0
# for i in cats:
#     count += i.age

# print(count)

# for i in cats:
#     i.mur()


# q = Cat()
# r = Cat()
# q.name = 'Мерида'
# q.run()
# q.mur()

# r.name = 'Чопоз'
# q.mur()
# r.mur()




class Course:
    def __init__(self, name : str, dlitelnost : int, napravlenie: str) -> None:
        self.name = name
        self.dlitelnost = dlitelnost
        self.napravlenie = napravlenie
    
    def info(self):
        return f'''
    name: {self.name}
    dlitelnost:{self.dlitelnost}
    napravlenie:{self.napravlenie} 
        '''

backand = Course('backand', 3 ,'python')
fullstack = Course('fullstack', 4 ,'python and js')
frontand = Course('frontand', 3 ,'js')
flutter = Course('flutter',3,'mobile it')
uiux = Course('uiux',2,'desing')

class Student:
    def __init__(self, full_name : str, email : str, phone : int, course : object ,studies : bool, comment : str ) -> None:
        self.full_name = full_name
        self.email = email
        self.phone = phone
        self.course = course
        self.studies = studies
        self.comment =comment

    def __str__(self):
        return f'''
name: {self.full_name}
email: {self.email}
phone: {self.phone} 
studies: {self.studies}
course: {self.course['name','dlitelnost','napravlenie']}
comment: {self.comment}'''



people = Student('Арген Кочконбаев', 'argenkochkonbaev@gmail.com', +996700403776, backand, True, 'без коментарий')
people2 = Student('Байэл Гапаров', 'baelgaparov@gmail.com', +996776453322, frontand, True, 'без коментарий')

# print(people.course. napravlenie)
# print(people2.course. napravlenie)

# class Cat:
#     def __init__(self, name: str , proda: str, age: int) -> None:
#         self.name = name
#         self.proda = proda
#         self.age = age

#     def __str__(self) -> str:
#         return f"kot po imeny {self.name}"

#     def info(self):
#         return f"имя: {self.name} \n порода: {self.proda} \n возрост: {self.age} года"
 
# c = Cat('Tom', 'sigan', 2)
# j = Cat('Jack', 'sigan', 2)

# print(c.info())
# print(j)



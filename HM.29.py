# 1. Գրել Animal ծնող class՝ eat() և sleep() մեթոդներով:
#    - Այս մեթոդներից յուրաքանչյուրը պետք է վերադարձնի համապատասխան հաղորդագրություն, երբ կանչ է արվում։
#    - eat()-ը պետք է վերադարձնի "Animal is eating..." հաղորդագրությունը
#    - sleep()-ը պետք է վերադարձնի "Animal is sleeping..." հաղորդագրությունը
#    Ծրագիրը պետք է ներառի նաև երկու ժառանգ class-ներ, որոնք ժառանգում են Animal class-ը՝ Bird և Fish:
#    Այս class-ները Animal class-ից պետք է ժառանգեն sleep() մեթոդը, բայց նաև պետք է ներառեն իրենց մեթոդները՝ ներկայացնելու համար կենդանիներին բնորոշ վարքագիծը:
#    - Bird class-ում, փոփոխեք eat() մեթոդը՝ "Bird is pecking at its food..." հաղորդագրությունը վերադարձնելու համար։
#    - Բացի այդ, ներառեք fly() մեթոդը, որը վերադարձնում է "Bird is flying..." հաղորդագրությունը:
#    - Fish class-ում ներառեք swim() մեթոդը, որը վերադարձնում է "Fish is swimming..." հաղորդագրությունը:

# class Animal:
#     def eat(self):
#         return "Animal is eating..."
#
#     def sleep(self):
#         return "Animal is sleeping..."
#
# class Bird(Animal):
#
#     def eat(self):
#         return "Bird is pecking at its food..."
#
#     def fly(self):
#         return "Bird is flying..."

# class Fish(Animal):
#
#     def swim(self):
#         return "Fish is swimming..."
#
#     # Animal object
#     print("Animal")
#     my_animal = Animal()
#     print(f"Animal eat: {my_animal.eat()}")
#     print(f"Animal sleep: {my_animal.sleep()}")
#
#     # Bird object
#     print("Bird ")
#     my_bird = Bird()
#     print(f"Bird eat: {my_bird.eat()}")
#     print(f"Bird sleep: {my_bird.sleep()}")
#     print(f"Bird flying: {my_bird.fly()}")
#
#     # fish object
#     print("Fish")
#     my_fish = Fish()
#     print(f"Fish eat: {my_fish.eat()}")
#     print(f"Fish sleep: {my_fish.sleep()}")
#     print(f"Fish swiming: {my_fish.swim()}")

# --------------
# 2․ Գրել Shape abstract class, որը․
#    - կունենա __init__(), perimetr(), area() աբստրակտ մեթոդներ։
#    Գրել Circle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի շրջանագծի շառավիղը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտը ճիշտ մուտքագրված լինի (պետք է լինի դրական թիվ),
#    - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները շրջանագծի համար։
#    Գրել Rectangle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի ուղղանկյան լայնությունը և երկարությունը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն (պետք է լինեն դրական թվեր),
#    - կվերախմբագրի Shape class-ի perimetr() և area() մեթոդները ուղղանկյան համար։
#    Գրել Triangle class, որը կժառանգի Shape class-ից, որը․
#    - __init__() -ում կընդունի
#      -- կամ եռանկյան երեք կողմերը,
#      -- կամ մեկ կողմը և բարձրությունը,
#      -- կամ երկու կողմերը և այդ կողմերի կազմած անկյունը,
#    - մինչ ինիցիալիզացնելը, կստուգի, որ ընդունված արգումենտները ճիշտ մուտքագրված լինեն,
#    - կվերախմբագրի Shape class-ի perimetr() մեթոդը եռանկյան համար,
#    - եռանկյան մակերեսը կհաշվի 3 տարբերակով, կախված մուտքագրված պարամետրերից․
#      1) S = (p * (p - a) * (p - b) * (p - c)) ^ 0.5   , որտեղ a, b, c - եռանկյան կողմերն են, p - եռանկյան կիսապարագիծը,
#      2) S = a * h / 2                                 , որտեղ a - եռանկյան կողմը, h = եռանկյան բարձրությունը,
#      3) S = a * b * sin(alpha) / 2                    , որտեղ a, b - եռանկյան կողմերն են, alpha - եռանկյան a և b կողմերի կազմած անկյունը։


# import math
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#     @abstractmethod
#     def __init__(self, *args, **kwargs):
#
#         pass
#
#     @abstractmethod
#     def perimetr(self):
#
#         pass
#
#     @abstractmethod
#     def area(self):
#
#         pass
#
# class Circle(Shape):
#     def __init__(self, radius):
#
#         if not isinstance(radius, (int, float)):
#             raise TypeError("Շառավիղը (radius) պետք է լինի թիվ։")
#         if radius <= 0:
#             raise ValueError("Շառավիղը (radius) պետք է լինի դրական թիվ։")
#
#         self.radius = radius
#
#     def perimetr(self):
#         return 2 * math.pi * self.radius
#
#     def area(self):
#         return math.pi * (self.radius ** 2)
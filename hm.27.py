# 1․ Գրել Triangle class, որը․
#    - __init__() -ում կընդունի եռանկյան կողմերը և կստուգի արդյոք նման կողմերով եռանկյուն գոյություն ունի թե ոչ,
#      եթե կողմերը սխալ են տրված կվերադարձնի Error համապատասխան տեքստով,*
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան կողմերը,*
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան պարագիծը,*
#    - կունենա մեթոդ, որը կվերադարձնի եռանկյան մակերեսը,*
#    - կունենա մեթոդ, որը կստուգի արդյոք եռանկյունը հավասարակողմ է, հավասարասրուն, թե անկանոն (կողմերը իրար = չեն), *
#    - կունենա մեթոդ, որը կստուգի արդյոք եռանկյունը ուղղանկյուն եռանկյուն է, թե ոչ,*
#    - կունենա մեթոդ, որը կգտնի եռանկյան անկյունները,
#    - կարող եք գրել նաև այլ մեթոդներ, որոնց միջոցով կստանաք տրված եռանկյան վերաբերյալ այլ ինֆորմացիա*
#      (օրինակ՝ ներգծած և արտագծած շրջանագծերի շառավղերը և այլն)․ բանաձևերը կարող եք գտնել համացանցում։*
import math
class Triangle:
    def __init__(self,a,b,c):

        if  a <=0 or b <= 0 or c <= 0:
            raise ValueError("The Triangle side must be Integer")
        if not(a + b >c and a + c > b and b + c > a):
            raise ValueError("cannot create side of Triangle")

        self.c = c
        self.b = b
        self.a = a

    def get_side(self):
        return self.a, self.b, self.c

    def perimeter(self):
        return self.a + self.b + self.c

    def get_surface(self):
        s = (self.a + self.b + self.c) / 2
        area = (s *(s - self.a)* (s - self.b)* (s - self.c)) ** 0.5
        return area

    def is_equilateral(self):
        return self.a == self.b and self.b == self.c

    def is_isosceles(self):
        return self.a == self.b or self.b == self.c or self.a == self.c

    def not_equal(self):
        return self.a != self.b and self.b != self.c and self.a != self.c

    def is_right_angeled(self):
        a1 = putagoras1 = math.isclose(self.a**2 + self.b**2, self.c**2)
        b2 = putagoras2 = math.isclose(self.a**2 + self.c**2, self.b**2)
        c3 = putagoras3 = math.isclose(self.c**2 + self.b**2, self.a**2)
        return putagoras1 or putagoras2 or putagoras3

    # *--def triangle_corner(self):
    #     math.

print("Side of Triangel")
triangle1 = Triangle(5,5,4)
print(f"{triangle1.get_side()}")
-----------

print("Perimeter")
triangle2 =Triangle(4,5,4)
print(f"{triangle2.perimeter()}")

-----------

print("Get surface")
triangle3 = Triangle(10,10,5)
print(f"{triangle3.get_surface()}")

-----------

print("Is equilateral")
triangle4 = Triangle(4,4,4)
print(f"{triangle4.is_equilateral()}")

-----------

print("Is isosceles")
triagnle5 = Triangle(4,4,6)
print(f"{triagnle5.is_isosceles()}")

----------

print("Not Equal")
triangle6 = Triangle(2,3,4,)
print(f"{triangle6.not_equal()}")

# ----------
print("Right Angled")
triangle7 = Triangle(6,7,8)
print(f"{triangle7.is_right_angeled()}")
_author_ = 'Safargalieva Zinfira Ismagilovna'

print("Task №3")
import math
print("Введем коэффициенты квадратного уравнения: ")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

D = int(b**2 - 4*a*c)
if D>0:
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print("Корень 1: ", x1)
    print("Корень 2: ", x2)
elif D<0:
    print("Вещественных корней нет!")
else:
    x = -b/(2*a)
    print("Корень: ", x)

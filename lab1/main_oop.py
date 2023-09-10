import sys
import math
import time

KOEFS = {
    1:'a',
    2:'b',
    3:'c'
}

class Equation:
    #Конструктор
    def __init__(self):
        self.coef_A = 0.0
        self.coef_B = 0.0
        self.coef_C = 0.0

        self.roots = []

    #Получение коэффициентов
    def get_coef(self, ind, prompt):
        try:
            coef = int(sys.argv[ind])
        except:
            print(f"Введите коэффициент {prompt.upper()}: ", end="")
            coef = ""
            while type(coef)!=int:
                coef = input()
                try:
                    coef = int(coef)
                except:
                    print("Неверный ввод! Повторите попытку: ", end="")
        return coef
    
    #Присвоение коэффициентов
    def get_coefs(self):
        self.coef_A, self.coef_B, self.coef_C = [self.get_coef(i, KOEFS[i]) for i in range(1,4)]

    #Вычисление корней
    def calculate(self):
        a = self.coef_A
        b = self.coef_B
        c = self.coef_C

        if a!=0.0:    
            D = b**2-4*a*c
            if D>0.0:
                rt_1 = (-b+math.sqrt(D))/(2*a)
                rt_2 = (-b-math.sqrt(D))/(2*a)
                self.roots.extend([rt_1, rt_2])
            elif D==0.0:
                rt_1 = (-b)/(2*a)
                self.roots.append(rt_1)
        elif b!=0.0: #Проверка исключения на линейное уравнение
            self.roots.append(-c/b)

    
    #Вывод корней
    def print_roots(self):
        print(f"Введенное уравнение: {self.coef_A}x^2+{self.coef_B}x+{self.coef_C}=0")
        if len(self.roots)!=0:
            if len(self.roots) == 2:
                print("Два действительных корня")
                print(f"Первый корень: {self.roots[0]}")
                print(f"Второй корень: {self.roots[1]}")
            else:
                print(f"Один действительный корень: {self.roots[0]}")
        elif self.coef_C!=0.0: #Если не равен, то ввели 5=0"
            print("Нет корней")
        else: #Если равен, то ввели 0=0"
            print("x - любое")


def main():
    r = Equation()
    r.get_coefs()
    r.calculate()
    r.print_roots()

    time.sleep(10)


if __name__ == "__main__":
    main()
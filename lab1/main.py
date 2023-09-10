import sys
import math
import time

KOEFS = {
    1:'a',
    2:'b',
    3:'c'
}

#Получаем коэффициенты из командной строки или считываем их из консоли
def get_koef(ind, prompt):
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


#Получаем корни биквадратного уравнения
def get_roots(a,b,c):
    roots = []
    D = float(b**2-4*a*c)
    if D > 0.0:
        rt_1 = (-b+math.sqrt(D))/(2*a)
        rt_2 = (-b-math.sqrt(D))/(2*a)
        roots.extend([rt_1, rt_2])
    elif D==0.0:
        rt_1 = (-b)/(2*a)
        roots.append(rt_1)
    return roots

#Если А=0, то решаем линейное уравнение
def unbiquadarate(b,c):
    roots = [(-c)/b]
    return roots

def main():
    a,b,c = [get_koef(i, KOEFS[i]) for i in range(1,4)]
    if a!=0:
        roots = get_roots(a,b,c)
    elif b!=0:
        roots = unbiquadarate(b,c)
    elif c!=0:
        roots = []
    else:
        print("x - любое")
        time.sleep(10)
        return

    #Обработка результата
    print(f"Введенное уравнение: {a}x^2+{b}x+{c}=0")
    if len(roots)!=0:
        if len(roots) == 2:
            print("Два действительных корня")
            print(f"Первый корень: {roots[0]}")
            print(f"Второй корень: {roots[1]}")
        else:
            print(f"Один действительный корень: {roots[0]}")
    else:
        print("Нет корней")
    
    time.sleep(10)

if __name__ == "__main__":
    main()
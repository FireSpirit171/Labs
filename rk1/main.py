from classes import Manufacturer, Detail, ManufacturerDetail
from create_object import manufacturers, details, manufacturer_details
from tabulate import tabulate
from operator import itemgetter

def task1():
    # Выводим производителей, их зарплаты и их детали если
    # фамилия сторудника заканчивается на ов
    res_11_det = {}
    res_11_sal = {}
    for x in one_to_many:
        man_name = x[0]
        man_salary = x[1]
        det = x[2]

        res_11_det.setdefault(man_name, []).append(det)
        res_11_sal[man_name] = man_salary
    
    data = [] #Для красивого вывода
    for name, dets in res_11_det.items():
        if str(name).endswith('ов'):
            data.append([name, res_11_sal[name], dets])

    table = tabulate(data, headers=["Производитель", "Зарплата", "Детали"], tablefmt="pretty")
    print(table)




def task2():
    # Отсортируем по убыванию стоимость детали у одного производителя
    # то есть делим зарплату на количество деталей сотрудника 
    res_12_uns = []
    for m in manufacturers:
        #Список деталей сотрудника
        m_details = list(filter(lambda i:i[0]==m.name, one_to_many))
        
        if len(m_details)>0:
            res_12_uns.append((m.name, round(m.salary/len(m_details), 2)))
        
    #Сортировка по цене за деталь
    return res_12_uns




def task3():
    # Для создания робота-пылесоса нужно сделать эти детали.
    robot_vacuum = [
        'Мотор',
        'Датчик',
        'Кнопка',
        'Ключ',
        'Крепеж',
        'Реле',
        'Контроллер',
        'Дисплей',
        'Панель',
        'Фильтр',
    ]
    # Определим производителей, которые нам нужны
    # для сборки робота-пылесоса

    d_emps = {}
    for d in robot_vacuum:
        for detail, name in many_to_many:
            if d == detail:
                # Список сотрудников, которые могут произвести эту деталь
                d_emps.setdefault(d, set()).add(name)

    # Воспользуемся результатом задания 2 и 
    # определим рабочих, которых нужно использовать
    # для сборки роботы-пылесоса за наименшую цену
    cheap_mans = sorted(task2(), key=itemgetter(1))
    res_13 = {}
    sum_prod = []
    for dtl, mans in d_emps.items():
        for cheap_man in cheap_mans:
            if cheap_man[0] in mans:
                res_13[dtl] = cheap_man[0]
                sum_prod.append(float(cheap_man[1]))
                break  
    
    data = [] #Для красиового вывода
    i = 0 
    for dtl, man in res_13.items():
        data.append([dtl, man, sum_prod[i]])
        i += 1

    table = tabulate(data, headers=["Деталь", "Производитель", "Стоимость"], tablefmt="pretty")
    print(table)
    print(f"Затраты на производство робота-пылесоса: {sum(sum_prod)}")




def main():
    """Основная функция"""
    print('Задание Д1')
    task1()

    print('\nЗадание Д2')
    res_12 = sorted(task2(), key=itemgetter(1), reverse=True)
    table = tabulate(res_12, headers=["Производитель", "Стоимость одной детали"], tablefmt="pretty")
    print(table)

    print('\nЗадание Д3')
    task3()

    a = input()



if __name__ == "__main__":
    # Соединение данных один-ко-многим 
    one_to_many = [(m.name, m.salary, d.name) 
        for m in manufacturers 
        for d in details 
        if m.id==d.man_id]
    
    # Соединение данных многие-ко-многим
    many_to_many_temp = [(m.name, md.man_id, md.det_id) 
        for m in manufacturers 
        for md in manufacturer_details 
        if m.id==md.man_id]
    
    many_to_many = [(d.name, man_name) 
        for man_name, man_id, det_id in many_to_many_temp
        for d in details 
        if d.id==det_id]
    
    main()

   
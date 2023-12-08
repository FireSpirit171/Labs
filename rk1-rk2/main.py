from classes import Manufacturer, Detail, ManufacturerDetail
from create_object import manufacturers, details, manufacturer_details
from tabulate import tabulate
from operator import itemgetter

def task1(one_to_many):
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
    
    data = []
    for name, dets in res_11_det.items():
        if str(name).endswith('ов'):
            data.append([name, res_11_sal[name], dets])

    return data


def task2(manufacturers, one_to_many):
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
    # Опреде

def task3(robot_vacuum, many_to_many, manufacturers, one_to_many):
    d_emps = {}
    for d in robot_vacuum:
        for detail, name in many_to_many:
            if d == detail:
                d_emps.setdefault(d, set()).add(name)

    cheap_mans = sorted(task2(manufacturers, one_to_many), key=itemgetter(1))
    res_13 = {}
    sum_prod = []
    for dtl, mans in d_emps.items():
        for cheap_man in cheap_mans:
            if cheap_man[0] in mans:
                res_13[dtl] = cheap_man[0]
                sum_prod.append(float(cheap_man[1]))
                break  
    
    data = []
    i = 0 
    for dtl, man in res_13.items():
        data.append([dtl, man, sum_prod[i]])
        i += 1

    total_cost = sum(sum_prod)
    return data, total_cost




def main():
    """Основная функция"""
    print('Задание Д1')
    table = table = tabulate(task1(one_to_many), headers=["Производитель", "Зарплата", "Детали"], tablefmt="pretty")
    print(table)

    print('\nЗадание Д2')
    res_12 = sorted(task2(manufacturers, one_to_many), key=itemgetter(1), reverse=True)
    table2 = tabulate(res_12, headers=["Производитель", "Стоимость одной детали"], tablefmt="pretty")
    print(table2)

    print('\nЗадание Д3')
    data3, total = task3(robot_vacuum, many_to_many, manufacturers, one_to_many)
    table3 = tabulate(data3, headers=["Деталь", "Производитель", "Стоимость"], tablefmt="pretty")
    print(table3)
    print(f"Затраты на производство робота пылесоса: {total}")

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

   
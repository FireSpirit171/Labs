from classes import Manufacturer, Detail, ManufacturerDetail
from operator import itemgetter

#Производители
manufacturers = [
    Manufacturer(1, "Абалуев", 35000),
    Manufacturer(2, "Андрест", 40000),
    Manufacturer(3, "Аннакулиева", 55000),
    Manufacturer(4, "Вопияшин", 18000),
    Manufacturer(5, "Гонов", 45000),
    Manufacturer(6, "Идрисов", 35000),
    Manufacturer(7, "Ларин", 65000),
    Manufacturer(8, "Лахин", 50000),
    Manufacturer(9, "Новицкий", 25000),
    Manufacturer(10, "Пермяков", 20000),
    Manufacturer(11, "Расулов", 100000),
    Manufacturer(12, "Сироткин", 58000),
    Manufacturer(13, "Стрельцов", 64000),
    Manufacturer(14, "Удалова", 39000),
    Manufacturer(15, "Ходырев", 235000),
    Manufacturer(16, "Шакиров", 85000),
    Manufacturer(17, "Шиленок", 105000),
    Manufacturer(18, "Якимова", 88000)
]

details = [
    Detail(1, 'Подшипник', 1),
    Detail(2, 'Вал', 2),
    Detail(3, 'Кольцо', 3),
    Detail(4, 'Пружина', 4),
    Detail(5, 'Шестерня', 5),
    Detail(6, 'Магнит', 6),
    Detail(7, 'Ротор', 7),
    Detail(8, 'Статор', 8),
    Detail(9, 'Клапан', 9),
    Detail(10, 'Компрессор', 10),
    Detail(11, 'Шкив', 11),
    Detail(12, 'Ремень', 12),
    Detail(13, 'Шпиндель', 13),
    Detail(14, 'Плита', 14),
    Detail(15, 'Фильтр', 15),
    Detail(16, 'Сенсор', 16),
    Detail(17, 'Трубка', 17),
    Detail(18, 'Регулятор', 18),
    Detail(19, 'Датчик', 1),
    Detail(20, 'Крепеж', 2),
    Detail(21, 'Кабель', 3),
    Detail(22, 'Ручка', 4),
    Detail(23, 'Панель', 5),
    Detail(24, 'Датчик', 6),
    Detail(25, 'Вентиль', 7),
    Detail(26, 'Ключ', 8),
    Detail(27, 'Аккумулятор', 9),
    Detail(28, 'Диск', 10),
    Detail(29, 'Дверь', 11),
    Detail(30, 'Замок', 12),
    Detail(31, 'Болт', 13),
    Detail(32, 'Гайка', 14),
    Detail(33, 'Плата', 15),
    Detail(34, 'Микросхема', 16),
    Detail(35, 'Реле', 17),
    Detail(36, 'Провод', 18),
    Detail(37, 'Диод', 1),
    Detail(38, 'Компонент', 2),
    Detail(39, 'Батарея', 3),
    Detail(40, 'Мотор', 4),
    Detail(41, 'Кнопка', 5),
    Detail(42, 'Шланг', 6),
    Detail(43, 'Штекер', 7),
    Detail(44, 'Разъем', 8),
    Detail(45, 'Контроллер', 9),
    Detail(46, 'Пульт', 10),
    Detail(47, 'Экран', 11),
    Detail(48, 'Рамка', 12),
    Detail(49, 'Винт', 13),
    Detail(50, 'Ручка-кран', 14)
]

manufacturer_details = [
    ManufacturerDetail(manufacturers[0], details[0]),
    ManufacturerDetail(manufacturers[1], details[1]),
    ManufacturerDetail(manufacturers[2], details[2]),
    ManufacturerDetail(manufacturers[3], details[3]),
    ManufacturerDetail(manufacturers[4], details[4]),
    ManufacturerDetail(manufacturers[5], details[5]),
    ManufacturerDetail(manufacturers[6], details[6]),
    ManufacturerDetail(manufacturers[7], details[7]),
    ManufacturerDetail(manufacturers[8], details[8]),
    ManufacturerDetail(manufacturers[9], details[9]),
    ManufacturerDetail(manufacturers[10], details[10]),
    ManufacturerDetail(manufacturers[11], details[11]),
    ManufacturerDetail(manufacturers[12], details[12]),
    ManufacturerDetail(manufacturers[13], details[13]),
    ManufacturerDetail(manufacturers[14], details[14]),
    ManufacturerDetail(manufacturers[15], details[15]),
    ManufacturerDetail(manufacturers[16], details[16]),
    ManufacturerDetail(manufacturers[17], details[17]),
    ManufacturerDetail(manufacturers[0], details[18]),
    ManufacturerDetail(manufacturers[1], details[19]),
    ManufacturerDetail(manufacturers[2], details[20]),
    ManufacturerDetail(manufacturers[3], details[21]),
    ManufacturerDetail(manufacturers[4], details[22]),
    ManufacturerDetail(manufacturers[5], details[23]),
    ManufacturerDetail(manufacturers[6], details[24]),
    ManufacturerDetail(manufacturers[7], details[25]),
    ManufacturerDetail(manufacturers[8], details[26]),
    ManufacturerDetail(manufacturers[9], details[27]),
    ManufacturerDetail(manufacturers[10], details[28]),
    ManufacturerDetail(manufacturers[11], details[29]),
    ManufacturerDetail(manufacturers[12], details[30]),
    ManufacturerDetail(manufacturers[13], details[31]),
    ManufacturerDetail(manufacturers[14], details[32]),
    ManufacturerDetail(manufacturers[15], details[33]),
    ManufacturerDetail(manufacturers[16], details[34]),
    ManufacturerDetail(manufacturers[17], details[35]),
    ManufacturerDetail(manufacturers[0], details[36]),
    ManufacturerDetail(manufacturers[1], details[37]),
    ManufacturerDetail(manufacturers[2], details[38]),
    ManufacturerDetail(manufacturers[3], details[39]),
    ManufacturerDetail(manufacturers[4], details[40]),
    ManufacturerDetail(manufacturers[5], details[41]),
    ManufacturerDetail(manufacturers[6], details[42]),
    ManufacturerDetail(manufacturers[7], details[43]),
    ManufacturerDetail(manufacturers[8], details[44]),
    ManufacturerDetail(manufacturers[9], details[45]),
    ManufacturerDetail(manufacturers[10], details[46]),
    ManufacturerDetail(manufacturers[11], details[47]),
    ManufacturerDetail(manufacturers[12], details[48]),
    ManufacturerDetail(manufacturers[13], details[49]),
    ManufacturerDetail(manufacturers[14], details[2]),
    ManufacturerDetail(manufacturers[15], details[5]),
    ManufacturerDetail(manufacturers[16], details[8]),
    ManufacturerDetail(manufacturers[17], details[11]),
    ManufacturerDetail(manufacturers[0], details[14]),
    ManufacturerDetail(manufacturers[1], details[17]),
    ManufacturerDetail(manufacturers[2], details[20]),
    ManufacturerDetail(manufacturers[3], details[23]),
    ManufacturerDetail(manufacturers[4], details[26]),
    ManufacturerDetail(manufacturers[5], details[29]),
    ManufacturerDetail(manufacturers[6], details[32]),
    ManufacturerDetail(manufacturers[7], details[35]),
    ManufacturerDetail(manufacturers[8], details[38]),
    ManufacturerDetail(manufacturers[9], details[41]),
]

def main():
    """Основная функция"""

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
    
    many_to_many = [(m.name, m.salary, det_name) 
        for det_name, man_id, det_id in many_to_many_temp
        for m in manufacturers if m.id==man_id]
    
    print('Задание Д1')
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
    
    for name, dets in res_11_det.items():
        print((name, res_11_sal[name], dets))
    

    print('Задание Д2')
    # Отсортируем по убыванию стоимость детали у одного производителя
    # то есть делим зарплату на количество деталей сотрудника 
    res_12_uns = []
    for m in manufacturers:
        #Список деталей сотрудника
        m_details = list(filter(lambda i:i[0]==m.name, one_to_many))
        
        if len(m_details)>0:
            res_12_uns.append((m.name, round(m.salary/len(m_details), 2)))
        
    #Сортировка по цене за деталь
    res_12 = sorted(res_12_uns, key=itemgetter(1), reverse=True)
    [print(x) for x in res_12]



    print('Задание Д3')

    
if __name__ == "__main__":
    main()
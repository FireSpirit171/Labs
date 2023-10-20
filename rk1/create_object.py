from classes import Detail, Manufacturer, ManufacturerDetail

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

#Детали
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

#Связь многие-ко-многим
manufacturer_details = [
    ManufacturerDetail(1,1),
    ManufacturerDetail(2,2),
    ManufacturerDetail(3,3),
    ManufacturerDetail(4,4),
    ManufacturerDetail(5,5),
    ManufacturerDetail(6,6),
    ManufacturerDetail(7,7),
    ManufacturerDetail(8,8),
    ManufacturerDetail(9,9),
    ManufacturerDetail(10,10),
    ManufacturerDetail(11,11),
    ManufacturerDetail(12,12),
    ManufacturerDetail(13,13),
    ManufacturerDetail(14,14),
    ManufacturerDetail(15,15),
    ManufacturerDetail(16,16),
    ManufacturerDetail(17,17),
    ManufacturerDetail(18,18),
    ManufacturerDetail(1,19),
    ManufacturerDetail(2,20),
    ManufacturerDetail(3,21),
    ManufacturerDetail(4,22),
    ManufacturerDetail(5,23),
    ManufacturerDetail(6,24),
    ManufacturerDetail(7,25),
    ManufacturerDetail(8,26),
    ManufacturerDetail(9,27),
    ManufacturerDetail(10,28),
    ManufacturerDetail(11,29),
    ManufacturerDetail(12,30),
    ManufacturerDetail(13,31),
    ManufacturerDetail(14,32),
    ManufacturerDetail(15,33),
    ManufacturerDetail(16,34),
    ManufacturerDetail(17,35),
    ManufacturerDetail(18,36),
    ManufacturerDetail(1,37),
    ManufacturerDetail(2,38),
    ManufacturerDetail(3,39),
    ManufacturerDetail(4,40),
    ManufacturerDetail(5,41),
    ManufacturerDetail(6,42),
    ManufacturerDetail(7,43),
    ManufacturerDetail(8,44),
    ManufacturerDetail(9,45),
    ManufacturerDetail(10,46),
    ManufacturerDetail(11,47),
    ManufacturerDetail(12,48),
    ManufacturerDetail(13,49),
    ManufacturerDetail(14,50),
    ManufacturerDetail(4,44),
    ManufacturerDetail(8,16),
    ManufacturerDetail(8,39),
    ManufacturerDetail(3,50),
    ManufacturerDetail(8,12),
    ManufacturerDetail(13,49),
    ManufacturerDetail(14,39),
    ManufacturerDetail(15,11),
    ManufacturerDetail(5,42),
    ManufacturerDetail(3,43),
    ManufacturerDetail(3,45),
    ManufacturerDetail(17,26),
    ManufacturerDetail(10,50),
    ManufacturerDetail(18,39),
    ManufacturerDetail(15,13),
    ManufacturerDetail(9,3),
    ManufacturerDetail(4,27),
    ManufacturerDetail(13,38),
    ManufacturerDetail(3,45),
    ManufacturerDetail(5,42),
    ManufacturerDetail(12,32),
    ManufacturerDetail(5,28),
    ManufacturerDetail(16,46),
    ManufacturerDetail(1,41),
    ManufacturerDetail(12,10),
    ManufacturerDetail(4,3),
    ManufacturerDetail(18,30),
    ManufacturerDetail(17,40),
    ManufacturerDetail(13,43),
    ManufacturerDetail(13,18),
    ManufacturerDetail(10,34),
    ManufacturerDetail(10,47),
    ManufacturerDetail(17,12),
    ManufacturerDetail(16,12),
    ManufacturerDetail(13,11),
    ManufacturerDetail(4,46),
    ManufacturerDetail(1,21),
    ManufacturerDetail(16,48),
    ManufacturerDetail(9,41),
    ManufacturerDetail(15,34),
    ManufacturerDetail(12,27),
    ManufacturerDetail(15,11),
    ManufacturerDetail(8,15),
    ManufacturerDetail(7,25),
    ManufacturerDetail(15,46),
    ManufacturerDetail(12,36),
    ManufacturerDetail(16,49),
    ManufacturerDetail(6,37),
    ManufacturerDetail(5,14),
    ManufacturerDetail(10,21)
]
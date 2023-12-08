import unittest
from main import task1, task2, task3
from classes import Manufacturer, Detail, ManufacturerDetail

class TestTasks(unittest.TestCase):
    def setUp(self):
        # Создаем данные для тестирования
        self.manufacturers = [
            Manufacturer(1, "Иванов", 100),
            Manufacturer(2, "Петров", 200),
        ]

        self.details = [
            Detail(1, 'X', 1),
            Detail(2, 'Y', 2),
        ]

        self.manufacturer_details = [
            ManufacturerDetail(1, 1),
            ManufacturerDetail(2, 2),
        ]

        self.robot_vacuum = ['X', 'Y']

    def test_task1(self):
        # Тестирование task1
        one_to_many = [(m.name, m.salary, d.name) for m in self.manufacturers for d in self.details if m.id == d.man_id]
        expected_result = [
            ['Иванов', 100, ['X']],
            ['Петров', 200, ['Y']],
        ]
        result = task1(one_to_many)
        self.assertEqual(result, expected_result)

    def test_task2(self):
        # Тестирование task2
        one_to_many = [(m.name, m.salary, d.name) for m in self.manufacturers for d in self.details if m.id == d.man_id]
        expected_result = [('Иванов', 100), ('Петров', 200)]
        result = task2(self.manufacturers, one_to_many)
        self.assertEqual(result, expected_result)

    def test_task3(self):
        # Тестирование task3
        one_to_many = [(m.name, m.salary, d.name) for m in self.manufacturers for d in self.details if m.id == d.man_id]
        many_to_many = [(d.name, m.name) for m in self.manufacturers for md in self.manufacturer_details for d in self.details if m.id == md.man_id and md.det_id == d.id]
        expected_result = [
            ['X', 'Иванов', 100.0],
            ['Y', 'Петров', 200.0],
        ]
        result, cost = task3(self.robot_vacuum, many_to_many, self.manufacturers, one_to_many)
        self.assertEqual(cost, 300.0)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

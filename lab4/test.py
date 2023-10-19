import unittest
from field import field
from gen_random import gen_random

class TestFieldFucnction(unittest.TestCase):
    def test_1(self):
        goods = [
            {'title': 'Ковер',
             'price': 2000, 
             'color': 'green'},

            {'title': 'Диван для отдыха', 
             'price': 5300, 
             'color': 'black'}
        ]
        result = []
        for item in field(goods, 'title'):
            result.append(item)
        expected_result = ['Ковер', 'Диван для отдыха']
        self.assertEqual(result, expected_result)

    def test_2(self):
        goods = [
            {'title': 'Ковер',
             'price': 2000, 
             'color': 'green'},

            {'title': 'Диван для отдыха', 
             'price': 5300, 
             'color': 'black'}
        ]
        result = []
        for item in field(goods, 'title', 'price'):
            result.append(item)
        expected_result = [{'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}]
        self.assertEqual(result, expected_result)


class TestGenRandomFunction(unittest.TestCase):
    
    def test_1(self): #Проверка на количество значений
        result = 0
        for x in gen_random(5, 1, 3):
            result += 1
        self.assertEqual(result, 5)

    def test_2(self): # Проверка на равенство
        result = [x for x in gen_random(5, 1, 1)]
        excepted_result = [1]*5
        self.assertListEqual(result, excepted_result)

    def test_3(self): #
        result = [x for x in gen_random(0, 10, 25)]
        if len(result) == 0:
            result = None
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
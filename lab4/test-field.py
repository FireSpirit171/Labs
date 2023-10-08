import unittest
from field import field

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

if __name__ == "__main__":
    unittest.main()
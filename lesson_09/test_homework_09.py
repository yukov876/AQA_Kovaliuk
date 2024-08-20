import unittest

from lesson_09.homework_09 import total_trees, total_books_sum, revert_string, sum_squares, computer_price


class MyTest(unittest.TestCase):
    def test_total_trees_positive(self):
        result = total_trees(4)
        self.assertEqual(result,15)

    def test_total_trees_negative(self):
        result = total_trees(3)
        self.assertNotEqual(result,15)

    def test_total_books_sum_positive(self):
        result = total_books_sum(8)
        self.assertEqual(result,27)

    def test_total_books_sum_negative(self):
        result = total_books_sum(8)
        self.assertNotEqual(result,29)

    def test_revert_string_positive(self):
        result = revert_string('Ok')
        self.assertTrue(result)

    def test_revert_string_negative(self):
        result = revert_string('Ok')
        self.assertNotEqual(result,'kkO')

    def test_sum_squares_positive(self):
        result = sum_squares(436402,37800)
        self.assertEqual(result,474202)

    def test_sum_squares_negative(self):
        result = sum_squares(436402,37800)
        self.assertNotEqual(result,500000)

    def test_computer_price_positive(self):
        result = computer_price(18,1179)
        self.assertEqual(result,21222)

    def test_computer_price_negative(self):
        result = computer_price(18,1179)
        self.assertNotEqual(result,30000)








if __name__ == '__main__':
    unittest.main()
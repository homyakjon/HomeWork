import os

from main import *
import unittest
from unittest.mock import patch
from io import StringIO
import sys

"""task 1"""


class TestAbundant(unittest.TestCase):

    def test_abundant_15(self):
        self.assertEqual(abundant(15), [[12], [4]])

    def test_abundant_19(self):
        self.assertEqual(abundant(19), [[18], [3]])

    def test_abundant_100(self):
        self.assertEqual(abundant(100), [[100], [17]])

    def test_abundant_999(self):
        self.assertEqual(abundant(999), [[996], [360]])

    def test_abundant_1(self):
        self.assertEqual(abundant(1), [[None], [0]])


if __name__ == '__main__':
    unittest.main()

"""task 2"""


class TestFilterByValues(unittest.TestCase):

    def test_filter_by_values_default_keys(self):
        input_data = [
            {"x": 1, "y": 2, "z": 3},
            {"x": 0, "y": 2, "z": 3},
            {"x": 0, "y": 4, "z": 5}
        ]
        expected_output = [
            {"x": 1, "y": 2, "z": 3},
            {"x": 0, "y": 2, "z": 3},
            {"x": 0, "y": 4, "z": 5}
        ]
        self.assertEqual(filter_by_values(input_data), expected_output)

    def test_filter_by_values_custom_keys(self):
        input_data = [
            {"x": 1, "y": 2, "z": 3},
            {"x": 0, "y": 2, "z": 3},
            {"x": 0, "y": 4, "z": 5}
        ]
        expected_output = [
            {"x": 1, "y": 2, "z": 3},
            {"x": 0, "y": 4, "z": 5}
        ]
        self.assertEqual(filter_by_values(input_data, keys=["x", "z"]), expected_output)

    def test_filter_by_values_empty_input(self):
        input_data = []
        self.assertEqual(filter_by_values(input_data), [])


if __name__ == '__main__':
    unittest.main()

"""task 3"""


class TestFindApartment(unittest.TestCase):

    def test_find_apartment_1(self):
        self.assertEqual(find_apartment(1), "get up 1 entrance and 1 floor")

    def test_find_apartment_13(self):
        self.assertEqual(find_apartment(13), "get up 1 entrance and 4 floor")

    def test_find_apartment_16(self):
        self.assertEqual(find_apartment(16), "get up 1 entrance and 4 floor")

    def test_find_apartment_17(self):
        self.assertEqual(find_apartment(17), "get up 2 entrance and 1 floor")

    def test_find_apartment_37(self):
        self.assertEqual(find_apartment(37), "get up 2 entrance and 10 floor")

    def test_find_apartment_38(self):
        self.assertEqual(find_apartment(38), "get up 3 entrance and 1 floor")


if __name__ == '__main__':
    unittest.main()


"""task 4"""


class TestCheckNumber(unittest.TestCase):

    def test_check_number_5(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        check_number(5)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "    *    \n   ***   \n  *****  \n ******* \n*********")

    def test_check_number_7(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        check_number(7)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "      *      \n     ***     \n    *****    \n   *******   \n  *********  \n *********** \n*************")

    def test_check_number_3(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        check_number(3)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "  *  \n *** \n*****")


if __name__ == '__main__':
    unittest.main()


"""task 5"""


class TestFuncTest(unittest.TestCase):

    def test_func_test_valid(self):
        with open('file_test.txt', 'w') as f:
            f.write('1 2 3;2 1\n')
            f.write('4 5 6;5 1\n')
            f.write('7 8 9;8 1\n')

        result = func_test()
        self.assertTrue(result)

    def test_func_test_invalid(self):
        with open('file_test.txt', 'w') as f:
            f.write('1 2 3;2 1\n')
            f.write('4 5 6;5 2\n')

        result = func_test()
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()

"""Task 8"""


class TestGetBancnotesDict(unittest.TestCase):
    def test_get_bancnotes_dict(self):
        result = get_bancnotes_dict(1340)
        self.assertEqual(result, {1000: 1, 200: 1, 100: 1, 20: 2})

    def test_get_bancnotes_dict_zero(self):
        result = get_bancnotes_dict(0)
        self.assertEqual(result, {})

    def test_get_bancnotes_dict_large_amount(self):
        result = get_bancnotes_dict(999999)
        self.assertEqual(result, {1000: 999, 500: 1, 100: 4})


if __name__ == '__main__':
    unittest.main()


"""Task 9"""


def create_test_input():
    with open('test_input.txt', 'w') as f:
        f.write('3 5 16\n')


class TestFizzBuzzFromFile(unittest.TestCase):
    def setUp(self):
        create_test_input()

    def tearDown(self):
        import os
        os.remove('test_input.txt')

    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='3 5 16\n')
    def test_fizzbuzz_from_file(self, mock_open):
        result = fizzbuzz_from_file('test_input.txt')
        self.assertEqual(result, '1 2 F 4 B F 7 8 F B 11 F 13 14 FB 16 ')


if __name__ == '__main__':
    unittest.main()


"""Task 10"""


class TestFizzBuzzFromFile(unittest.TestCase):
    def setUp(self):
        self.input_file = 'test_input.txt'
        self.output_file = 'test_output.txt'
        self.expected_output = '1 2 F 4 B F 7 8 F B 11 F 13 14 FB 16 '

        with open(self.input_file, 'w') as f:
            f.write('3 5 16\n')

    def tearDown(self):
        os.remove(self.input_file)
        os.remove(self.output_file)

    @patch('sys.stdout', new_callable=StringIO)
    def test_fizzbuzz_from_file(self, mock_stdout):
        fizzbuzz_from_file(self.input_file, self.output_file)
        result = mock_stdout.getvalue()
        self.assertEqual(result, self.expected_output)

        with open(self.output_file, 'r') as f:
            output_content = f.read()
            self.assertEqual(output_content, self.expected_output)


if __name__ == '__main__':
    unittest.main()

"""Task 11"""


class TestScoreboardFunction(unittest.TestCase):

    def test_scoreboard_with_explicit_scores(self):
        self.assertEqual(scoreboard("four nil"), [4, 0])
        self.assertEqual(scoreboard("two three"), [2, 3])
        self.assertEqual(scoreboard("six seven"), [6, 7])

    def test_scoreboard_with_implicit_scores(self):
        self.assertEqual(scoreboard("new score: two three"), [2, 3])
        self.assertEqual(scoreboard("Arsenal just conceded another goal, two nil"), [2, 0])

    def test_scoreboard_with_invalid_input(self):
        self.assertEqual(scoreboard("invalid input"), [])
        self.assertEqual(scoreboard("seven eight eleven"), [7, 8])


if __name__ == '__main__':
    unittest.main()
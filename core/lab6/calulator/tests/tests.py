import unittest
from calulator.operations.operations import Addition, Division, Multiplication, Subtraction
from calulator.ui.error_handler.error_handler import handle_error


class CalculatorTest(unittest.TestCase):
    # addition
    def test_addition_positive_numbers(self):
        addition_operation = Addition(5, 3)

        self.assertEqual(addition_operation.execute(), 8)

    def test_addition_negative_numbers(self):
        addition_operation = Addition(-2, -4)

        self.assertEqual(addition_operation.execute(), -6)

    def test_addition_mixed_numbers(self):
        addition_operation = Addition(4, -1)

        self.assertEqual(addition_operation.execute(), 3)

    # substraction
    def test_subtraction_positive_numbers(self):
        subtraction_operation = Subtraction(5, 3)

        self.assertEqual(subtraction_operation.execute(), 2)

    def test_subtraction_negative_numbers(self):
        subtraction_operation = Subtraction(-2, -4)

        self.assertEqual(subtraction_operation.execute(), 2)

    def test_subtraction_mixed_numbers(self):
        subtraction_operation = Subtraction(4, -1)

        self.assertEqual(subtraction_operation.execute(), 5)

    def test_subtraction_zero(self):
        subtraction_operation = Subtraction(5, 5)

        self.assertEqual(subtraction_operation.execute(), 0)

    def test_subtraction_negative_result(self):
        subtraction_operation = Subtraction(10, 15)

        self.assertEqual(subtraction_operation.execute(), -5)

    # multiplication
    def test_multiplication_positive_numbers(self):
        multiplication_operation = Multiplication(5, 3)

        self.assertEqual(multiplication_operation.execute(), 15)

    def test_multiplication_negative_numbers(self):
        multiplication_operation = Multiplication(-2, -4)

        self.assertEqual(multiplication_operation.execute(), 8)

    def test_multiplication_mixed_numbers(self):
        multiplication_operation = Multiplication(4, -1)

        self.assertEqual(multiplication_operation.execute(), -4)

    def test_multiplication_zero(self):
        multiplication_operation = Multiplication(5, 0)

        self.assertEqual(multiplication_operation.execute(), 0)

    def test_multiplication_by_zero(self):
        multiplication_operation = Multiplication(0, 5)

        self.assertEqual(multiplication_operation.execute(), 0)

    # division
    def test_division_positive_decimal_numbers(self):
        division_operation = Division(10.5, 2.5)

        self.assertEqual(division_operation.execute(), 4.2)

    def test_division_negative_decimal_numbers(self):
        division_operation = Division(-10.5, -2.5)

        self.assertEqual(division_operation.execute(), 4.2)

    def test_division_mixed_decimal_numbers(self):
        division_operation = Division(4.5, -2)

        self.assertEqual(division_operation.execute(), -2.25)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            Division(10.5, 0).execute()

    # error handling
    def test_division_by_zero_error(self):
        with self.assertRaises(ValueError):
            handle_error(Division(10, 0).execute())

    def test_invalid_operation_error(self):
        with self.assertRaises(TypeError):
            handle_error(Division('abc', 0).execute())

    def test_invalid_number_error(self):
        with self.assertRaises(TypeError):
            handle_error(Division(10, 'abc').execute())

    def test_calculator(self):
        self.test_addition_positive_numbers()
        self.test_addition_negative_numbers()
        self.test_addition_mixed_numbers()

        self.test_subtraction_positive_numbers()
        self.test_subtraction_negative_numbers()
        self.test_subtraction_mixed_numbers()
        self.test_subtraction_zero()
        self.test_subtraction_negative_result()

        self.test_multiplication_positive_numbers()
        self.test_multiplication_negative_numbers()
        self.test_multiplication_mixed_numbers()
        self.test_multiplication_zero()
        self.test_multiplication_by_zero()

        self.test_division_positive_decimal_numbers()
        self.test_division_negative_decimal_numbers()
        self.test_division_mixed_decimal_numbers()
        self.test_division_by_zero()

        self.test_division_by_zero_error()
        self.test_invalid_operation_error()
        self.test_invalid_number_error()

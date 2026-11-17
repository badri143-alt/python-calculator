import unittest
from calculator import calculator


class TestCalculator(unittest.TestCase):
    """Test cases for the calculator function."""

    def test_add_positive_numbers(self):
        """Test addition of two positive numbers."""
        self.assertEqual(calculator('add', 5, 3), 8)

    def test_add_negative_numbers(self):
        """Test addition of two negative numbers."""
        self.assertEqual(calculator('add', -5, -3), -8)

    def test_add_mixed_numbers(self):
        """Test addition of positive and negative numbers."""
        self.assertEqual(calculator('add', 10, -4), 6)

    def test_add_zero(self):
        """Test addition with zero."""
        self.assertEqual(calculator('add', 0, 5), 5)

    def test_add_floats(self):
        """Test addition of floating point numbers."""
        self.assertAlmostEqual(calculator('add', 2.5, 3.7), 6.2, places=5)

    def test_subtract_positive_numbers(self):
        """Test subtraction of two positive numbers."""
        self.assertEqual(calculator('subtract', 10, 4), 6)

    def test_subtract_negative_numbers(self):
        """Test subtraction of two negative numbers."""
        self.assertEqual(calculator('subtract', -5, -3), -2)

    def test_subtract_mixed_numbers(self):
        """Test subtraction with positive and negative numbers."""
        self.assertEqual(calculator('subtract', 10, -4), 14)

    def test_subtract_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(calculator('subtract', 5, 0), 5)

    def test_subtract_floats(self):
        """Test subtraction of floating point numbers."""
        self.assertAlmostEqual(calculator('subtract', 5.5, 2.3), 3.2, places=5)

    def test_multiply_numbers(self):
        """Test multiplication of two numbers."""
        self.assertEqual(calculator('multiply', 5, 3), 15)

    def test_multiply_negative_numbers(self):
        """Test multiplication with a negative number."""
        self.assertEqual(calculator('multiply', -5, 3), -15)

    def test_multiply_floats(self):
        """Test multiplication of floating point numbers."""
        self.assertAlmostEqual(calculator('multiply', 2.5, 3.2), 8.0, places=5)

    def test_divide_numbers(self):
        """Test division of two numbers."""
        self.assertEqual(calculator('divide', 10, 2), 5)

    def test_divide_floats(self):
        """Test division of floating point numbers."""
        self.assertAlmostEqual(calculator('divide', 7.5, 2.5), 3.0, places=5)

    def test_divide_by_zero(self):
        """Test that division by zero raises ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            calculator('divide', 10, 0)

    def test_invalid_operation_modulo(self):
        """Test that an invalid operation raises ValueError."""
        with self.assertRaises(ValueError):
            calculator('modulo', 5, 3)

    def test_invalid_operation_floor_divide(self):
        """Test that an invalid operation raises ValueError."""
        with self.assertRaises(ValueError):
            calculator('floor_divide', 10, 2)

    def test_invalid_operation_unknown(self):
        """Test that an unknown operation raises ValueError."""
        with self.assertRaises(ValueError):
            calculator('unknown', 5, 3)

    def test_error_message_contains_operation(self):
        """Test that the error message contains the invalid operation name."""
        with self.assertRaises(ValueError) as context:
            calculator('power', 2, 3)
        self.assertIn('power', str(context.exception))


if __name__ == '__main__':
    unittest.main()

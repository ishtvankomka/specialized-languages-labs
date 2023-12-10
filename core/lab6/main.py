from calulator.ui.ui import Calculator
from calulator.tests.tests import CalculatorTest


if __name__ == '__main__':
    test_calculator = CalculatorTest()
    test_calculator.test_calculator()
    
    calc = Calculator()
    calc.user_interface()
    
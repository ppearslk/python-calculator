import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
# add ------------------------------------------------------------------------
    def test1_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test2_add_nagative(self):
        self.assertEqual(self.calc.add(-1, -5), -6)

# subtract ------------------------------------------------------------------- 
    def test1_subtract(self):
        self.assertEqual(self.calc.subtract(1,2),-1)
    def test2_subtract_nagative(self):
        self.assertEqual(self.calc.subtract(-4,-3),-1)

# multiply -------------------------------------------------------------------
    def test1_multiply(self):
        self.assertEqual(self.calc.multiply(2,1),2)
    def test2_multiply_nagative(self):
        self.assertEqual(self.calc.multiply(-10,10),-100)
    def test3_multiply_nagative_and_nagative(self):
        self.assertEqual(self.calc.multiply(-10,-5),50)

# divide ---------------------------------------------------------------------
    def test1_divide(self):
        self.assertEqual(self.calc.divide(4,2),2)
    def test2_divide_nagative(self):
        self.assertEqual(self.calc.divide(-155,5),-31)
    def test3_divide_nagative_and_nagative(self):
        self.assertEqual(self.calc.divide(-155,-5),31)


# modulo --------------------------------------------------------------------
    def test1_modulo(self):
        self.assertEqual(self.calc.modulo(21,2),1)
    def test2_modulo_nagative(self):
        self.assertEqual(self.calc.modulo(-35,3),-2)

    # Add the following test methods to the TestCalculator class:
    
if __name__ == '__main__':
    unittest.main()
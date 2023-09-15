import unittest
import unit_test_module as ut

#Automated Testing vs Manual Testing

#Exploratory testing
'''
print(ut.fatorial(5))
print(ut.fatorial(7))
print(ut.fatorial(0))
print(ut.fatorial(42))
print(ut.fatorial(5.0))
'''
# Big numbers
# Other formats

#Automated Testing

"""
class CLASS_NAME(unittest.TestCase):
    def METOD_NOME(self):
        self.
"""

class TestFatorial(unittest.TestCase):
    #Equivalence Partitioning Method
    #Equivalence Class Partitioning (ECP)
    def test_greather_than_1(self):
        self.assertEqual(ut.fatorial(5), 120)
    def test_less_than_o(self):
        self.assertEqual(ut.fatorial(-5), 1)
    def test_equal_to_0(self):
        self.assertEqual(ut.fatorial(0), 1)
    def test_equal_to_1(self):
        self.assertEqual(ut.fatorial(1), 1)
    def test_input_value_type(self):
        self.assertRaises(TypeError, ut.fatorial, "Oi")
        
if __name__ == '__main__':
    unittest.main()
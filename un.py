import unittest

def add(a,b):
    return a+b

class TestAddFunction(unittest.TestCase):
    def test_add_postive(self):
        self.assertEqual(add(1,9),10)
    
    def test_add_negative(self):
        self.assertEqual(add(-2,-4),-6)

    def test_add_common(self):
        self.assertEqual(add(-2,1),-1)
if __name__ =='__main__':
    # unittest.main(verbosity=1)
    unittest.main(verbosity=2)
    



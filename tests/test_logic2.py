import unittest
from logic.logic2 import LogicGate

class TestLogicGate(unittest.TestCase):
    def test_add(self):
        lg = LogicGate()
        self.assertEqual(lg.AND(0, 0), 0)
        self.assertEqual(lg.AND(1, 0), 0)
        self.assertEqual(lg.AND(0, 1), 0)
        self.assertEqual(lg.AND(1, 1), 1)
        self.assertNotEqual(lg.AND(0, 0), 1)
        self.assertNotEqual(lg.AND(1, 0), 1)
        self.assertNotEqual(lg.AND(0, 1), 1)
        self.assertNotEqual(lg.AND(1, 1), 0)

    def test_add(self):
        lg = LogicGate()
        self.assertEqual(lg.NAND(0, 0), 1)
        self.assertEqual(lg.NAND(1, 0), 1)
        self.assertEqual(lg.NAND(0, 1), 1)
        self.assertEqual(lg.NAND(1, 1), 0)
        self.assertNotEqual(lg.NAND(0, 0), 0)
        self.assertNotEqual(lg.NAND(1, 0), 0)
        self.assertNotEqual(lg.NAND(0, 1), 0)
        self.assertNotEqual(lg.NAND(1, 1), 1)
    def test_add(self):
        lg = LogicGate()
        self.assertEqual(lg.OR(0, 0), 0)
        self.assertEqual(lg.OR(1, 0), 1)
        self.assertEqual(lg.OR(0, 1), 1)
        self.assertEqual(lg.OR(1, 1), 1)
        self.assertNotEqual(lg.OR(0, 0), 1)
        self.assertNotEqual(lg.OR(1, 0), 0)
        self.assertNotEqual(lg.OR(0, 1), 0)
        self.assertNotEqual(lg.OR(1, 1), 0)

    
if __name__ == "__main__":
    unittest.main()

     


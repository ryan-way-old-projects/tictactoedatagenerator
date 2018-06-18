import unittest
import sys
from rules.rules import Rules

class RulesTest(unittest.TestCase):

    m_rules = Rules()

    def test_init(self):
        self.assertEqual(self.m_rules.PossibleMoves([]), self.m_rules.ALLMOVES)

    def test_mid(self):
        self.assertEqual(sorted(self.m_rules.PossibleMoves([1,2,3,4])), [5,6,7,8,9])

    def test_end(self):
        self.assertEqual(self.m_rules.PossibleMoves(self.m_rules.ALLMOVES),[])

if __name__ == '__main__':
    unittest.main()
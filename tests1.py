import unittest
from app import Singleton

class TestStringMethods(unittest.TestCase):

  def test_Singleton(self):
      a = Singleton()
      b = Singleton()
      self.assertEqual(a, b)

      if __name__ == '__main__':
          unittest.main()
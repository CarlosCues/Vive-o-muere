import unittest
from file import *
from io import IOBase


class TestStringMethods(unittest.TestCase):

    def test_archivo(self):
        nombre_archivo= 'test'
        for x in range(5):
            escribe_fecha(nombre_archivo)
        file=open('test.txt')
        lista=file.readlines()      
        
        self.assertEqual(len(lista), 1)


if __name__ == '__main__':
    unittest.main()
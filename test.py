import unittest
from extract_landmarks import extract_landmarks


class TestStringMethods(unittest.TestCase):

    def test_extract_landmarks(self):
        landmarks=extract_landmarks('./train/down111.png')
        print(landmarks)
        self.assertEqual(len(landmarks),63)


if __name__ == '__main__':
    unittest.main()
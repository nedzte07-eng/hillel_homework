

import unittest
from lessons.lesson_07.homework_07 import reverse_string


class myTest(unittest.TestCase):
    def test_reverse_string_positive(self):

        EXPECTED_RESULT = "poiu ytrewq"
        result = reverse_string("qwerty uiop")
        self.assertEqual(EXPECTED_RESULT, result, "test_reverse_string_positive is failed")

if __name__ == '__main__':
    unittest.main()
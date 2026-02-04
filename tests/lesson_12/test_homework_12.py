

import unittest
from lessons.lesson_07.homework_07 import reverse_string
from lessons.lesson_08.homework_8 import Student
from lessons.lesson_10.lesson_10_part_2 import Square


class myTest(unittest.TestCase):
    def test_reverse_string_positive(self):

        EXPECTED_RESULT = "poiu ytrewq"
        result = reverse_string("qwerty uiop")
        self.assertEqual(EXPECTED_RESULT, result, "test_reverse_string_positive is failed")

    def test_reverse_string_negative(self):

        EXPECTED_RESULT = "qwerty uiop112"
        result = reverse_string("qwerty uiop")
        self.assertNotEqual(EXPECTED_RESULT, result, "test_reverse_string_negative is failed")

    def test_student_info_positive_contain(self):
        PHRASE = "Звать"
        student = Student("Sasha", 'Nedz', 41, 10)
        self.assertIn(PHRASE, student.student_info(), "test_student_info_positive_contain is failed")

    def test_student_info_positive_not_contain(self):
        PHRASE = "рюкзак"
        student = Student("Sasha", 'Nedz', 41, 10)
        self.assertNotIn(PHRASE, student.student_info(), "test_student_info_positive_not_contain is failed")

    def test_square_area_positive(self):
        EXPECTATION = 19
        square = Square(4)
        self.assertAlmostEqual(EXPECTATION, square.area(), delta=4, msg="test_square_area_positive is failed")

    def test_square_perimeter_positive(self):
        EXPECTATION = 20
        square = Square(5)
        self.assertTrue(EXPECTATION == square.perimeter(), msg="test_square_perimeter_positive is failed")

    def test_square_area_negative(self):
        EXPECTATION = 19
        square = Square(5)
        self.assertFalse(EXPECTATION == square.perimeter(), msg="test_square_area_negative is failed")

    def test_student_info_positive_is_not_none(self):
        student = Student("Sasha", 'Nedz', 41, 10)
        self.assertIsNotNone(student.student_info(), "test_student_info_positive_is_not_none is failed")

    def test_student_info_positive_is_none(self):
        student = Student("Sasha", 'Nedz', 41, 10)
        self.assertIsNone(student.average_change(11), "test_student_info_positive_is_none is failed")

    def test_student_has_attr_positive(self):
        student = Student("Sasha", 'Nedz', 41, 10)
        self.assertHasAttr(student, "average_change", "test_test is failed")


if __name__ == '__main__':
    unittest.main()
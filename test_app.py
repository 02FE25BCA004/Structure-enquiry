
import unittest
from app import calculate_grade


class TestGradeEvaluation(unittest.TestCase):

    def test_grade_s(self):
        self.assertEqual(calculate_grade(95), "Grade S")

    def test_grade_a(self):
        self.assertEqual(calculate_grade(85), "Grade A")

    def test_grade_b(self):
        self.assertEqual(calculate_grade(70), "Grade B")

    def test_grade_c(self):
        self.assertEqual(calculate_grade(55), "Grade C")

    def test_grade_d(self):
        self.assertEqual(calculate_grade(40), "Grade D")

    def test_grade_f(self):
        self.assertEqual(calculate_grade(30), "Grade F")


if __name__ == "__main__":
    unittest.main()

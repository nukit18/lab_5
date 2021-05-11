import unittest
import main


class TestMethods(unittest.TestCase):

    def test_determinant_2x2(self):
        self.assertEqual(main.get_determinant([[3, 2], [4, 5]]), 7)

    def test_determinant_3x3(self):
        self.assertEqual(main.get_determinant([[-1, 2, -5], [4, -1, 3], [3, 0, -6]]), 45)

    def test_determinant_4x4(self):
        self.assertEqual(main.get_determinant([[2, 3, -7, 5], [4, 1, -4, 4], [-3, 4, 2, 3], [-1, -2, 5, 7]]), -857)

    def test_determinant_zero(self):
        self.assertEqual(main.get_determinant([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 0)

    def test_inverse_2x2(self):
        self.assertEqual(main.get_inverse_matrix([[1, 2], [3, 4]]), [[-2, 1], [1.5, -0.5]])

    def test_inverse_3x3(self):
        self.assertEqual(main.get_inverse_matrix([[1, 0, 0], [1, -1, 0], [1, 0, 1]]), [[1, 0, 0], [1, -1, 0], [-1, 0, 1]])

    def test_inverse_null(self):
        with self.assertRaises(SystemExit):
            main.get_inverse_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    def test_multiply_vector_3x3(self):
        self.assertEqual(main.multiply_by_vector([[14, 8, 3], [8, 5, 2], [3, 2, 1]], [0, 12, 0]), [96, 60, 24])

    def test_multiply_vector_incompatible_data(self):
        with self.assertRaises(SystemExit):
            main.multiply_by_vector([[14, 8, 3], [8, 5, 2], [3, 2, 1]], [0, 12])

    def test_unknown_members_1(self):
        self.assertEqual(main.get_unknown_members([[7, 2, 3], [9, 3, 4], [5, 1, 3]], [13, 15, 14]), [1.9999999999999982, -4.999999999999995, 3.0])

    def test_unknown_members_2(self):
        self.assertEqual(main.get_unknown_members([[1, 2, 0], [3, 2, 1], [0, 1, 2]], [10, 23, 13]), [3.9999999999999996, 3.0, 5.0])

    def test_unknown_members_3(self):
        self.assertEqual(main.get_unknown_members([[3, 1, -2], [1, 3, -1], [4, -2, -3]], [-13, -11, -12]), [-1.0, -2.0, 4.0000000000000036])

    def test_unknown_members_4(self):
        self.assertEqual(main.get_unknown_members([[-1, -8, -8, -1], [-9, -5, -1, -5], [-6, -8, -5, -2], [-7, 6, -5, -2]], [38, 70, 65, 29]),
                         [-6.0, -2.9999999999999996, -0.9999999999999993, -5.10702591327572e-15])

    def test_unknown_members_incompatible_data(self):
        with self.assertRaises(SystemExit):
            main.get_unknown_members([[7, 2, 3], [9, 3, 4], [5, 1, 3]], [13, 15, 14, 4])

    def test_unknown_members_not_square_matrix(self):
        with self.assertRaises(SystemExit):
            main.get_unknown_members([[1, 2, 3], [5, 6, 7], [9, 10, 11]], [4, 8, 12])


if __name__ == '__main__':
    unittest.main()

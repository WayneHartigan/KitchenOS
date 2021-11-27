import fileinput
from parameterized import parameterized
from curry_wholesaler_problem import sort_curry_choices


class TestCurryWholesalerProblem:
    @parameterized.expand(
        [
            ("test_files/test_1.txt", "MVVVV"),
            ("test_files/test_2.txt", "MVVVV"),
            ("test_files/test_3.txt", "MVVVV"),
            ("test_files/test_4.txt", "MVVVV"),
            ("test_files/test_5.txt", "MVVVV"),
        ]
    )
    def test_curry_wholesaler_problem(self, test_file, expected):
        input_file = fileinput.input(test_file)
        resp = sort_curry_choices(input_file)
        assert resp == expected

    # Below tests if prefer not to use parameterized testing
    def test_1(self):
        input_file = fileinput.input("test_files/test_1.txt")
        resp = sort_curry_choices(input_file)
        assert resp == "MVVVV"

    def test_2(self):
        input_file = fileinput.input("test_files/test_2.txt")
        resp = sort_curry_choices(input_file)
        assert resp == "No solution exists"

    def test_3(self):
        input_file = fileinput.input("test_files/test_3.txt")
        resp = sort_curry_choices(input_file)
        assert resp == "VMVMV"

    def test_4(self):
        input_file = fileinput.input("test_files/test_4.txt")
        resp = sort_curry_choices(input_file)
        assert resp == "VM"

    def test_5(self):
        input_file = fileinput.input("test_files/test_5.txt")
        resp = sort_curry_choices(input_file)
        assert resp == "No solution exists"

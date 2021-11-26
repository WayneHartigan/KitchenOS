import fileinput
from curry_wholesaler_problem import sort_curry_choices


class TestCurryWholesaler:
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
        assert resp == "VM"

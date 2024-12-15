import pytest

@pytest.mark.usefixtures("setup")
class TestExample:
    @pytest.mark.smoke
    def test_first_program(self):
        msg = "Hello"
        assert msg == "Hi", "Test failed because strings do not match"

    @pytest.mark.xfail
    def test_second_program(self):
        a = 4
        b = 6
        assert a+2 == 6, "Addition is not matching"

    @pytest.mark.skip
    def test_third_program(self):
        msg = "Hello"
        assert msg == "Hello", "Test failed because strings do not match"

    def test_fourth_program(self):
        a = 4
        b = 6
        assert a+2 == 6, "Addition is not matching"

    def test_fifth_program(self):
        msg = "Hello"
        assert msg == "Hello", "Test failed because strings do not match"
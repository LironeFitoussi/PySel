import pytest

# Marking the test cases
@pytest.mark.smoke
def test_third_program():
    msg = "Hello World"
    assert msg == "Hello Bro", "Message is not matching" # This will fail

def test_fourth_program_alpha(setup):
    a = 4
    b = 6
    assert a+2 == 6, "Addition is not matching" # This will pass
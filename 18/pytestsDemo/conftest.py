import pytest

@pytest.fixture(scope="class")
def setup():
    print("\nI will be executing first")
    yield # This will act as a teardown
    print("\nI will execute last")
    
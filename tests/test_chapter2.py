from src.chapter2 import compare_number


# Test the compare_number function
def test_compare_number():
    assert compare_number(5, 5) is True
    assert compare_number(10, 7) is False
    assert compare_number(3, 9) is False

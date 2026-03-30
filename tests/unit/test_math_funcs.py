from poe_breakout.math_funcs import add_some_numbers


def test_add_some_numbers_args():
    """Test that add_some_numbers returns the expected results when only args are provided."""
    result = add_some_numbers(1, 2, 3)
    assert result == 6


def test_add_some_numbers_kwargs():
    """Test that add_some_numbers returns the expected results when only kwargs are provided."""
    result = add_some_numbers(a=4, b=5)
    assert result == 9


def test_add_some_numbers_args_and_kwargs():
    """Test that add_some_numbers returns the expected results when both args and kwargs are provided."""
    result = add_some_numbers(1, 2, 3, a=4, b=5)
    assert result == 15

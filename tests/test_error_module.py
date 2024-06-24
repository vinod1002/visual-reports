
import pytest
from src.error_module import divide_by_zero, function_with_error

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide_by_zero()

def test_function_with_error():
    with pytest.raises(NameError):
        function_with_error()


from src.calculator import add, subtract, calculate_complex_result, execute_safe_command, multiply # Импортирована безопасная функция
from src.utils import format_message
import pytest

def test_add():
    assert add(1, 2) == 3

def test_subtract():
    assert subtract(5, 2) == 3

def test_complex_result():
    assert calculate_complex_result([1, 2, 3, 4]) == 2.5

def test_format_message():
    assert format_message("World") == "Hello, World!"

def test_multiply():
    assert multiply(2, 3) == 6

# Bandit не тестируется, только вызывается
def test_safe_call(capsys):
    execute_safe_command(["echo", "test"]) # Вызов безопасной функции со списком
    captured = capsys.readouterr()
    assert "Executing: echo test" in captured.out

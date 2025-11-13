import time
import subprocess
from typing import List, Union

UNUSED_VARIABLE = "I will cause a Ruff error (F841)" # Ruff: Неиспользуемая переменная

def add(a: int, b: int) -> int:
    """Простое сложение."""
    return a + b

def subtract(a: int, b: int) -> str: # Mypy: Неверный тип возвращаемого значения
    """Вычитание."""
    return a - b

def calculate_complex_result(items: List[Union[int, float]]) -> float:
    """Выполняет сложный расчет."""
    total = sum(items)
    return total / len(items)

def execute_unsafe_command(command: str):
    """Bandit: Небезопасный вызов с shell=True."""
    print(f"Executing: {command}")
    subprocess.call(command, shell=True) # Bandit: Уязвимость (B603)

def multiply(a, b):
    return a * b

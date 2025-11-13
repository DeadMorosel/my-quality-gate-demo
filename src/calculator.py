import subprocess
from typing import List, Union

# Ruff: UNUSED_VARIABLE удалена

def add(a: int, b: int) -> int:
    """Простое сложение."""
    return a + b

def subtract(a: int, b: int) -> int: # Mypy: Тип возврата исправлен на int
    """Вычитание."""
    return a - b

def calculate_complex_result(items: List[Union[int, float]]) -> float:
    """Выполняет сложный расчет."""
    total = sum(items)
    return total / len(items)

def execute_safe_command(command: List[str]): 
    """Bandit: Безопасный вызов."""
    print(f"Executing: {' '.join(command)}")
    subprocess.call(command) # Bandit: Уязвимость устранена

def multiply(a, b):
    return a * b

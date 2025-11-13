import subprocess
from typing import List, Union

# UNUSED_VARIABLE удалена - ИСПРАВЛЕНА ОШИБКА Ruff (F841)

def add(a: int, b: int) -> int:
    """Простое сложение."""
    return a + b

def subtract(a: int, b: int) -> int: # ИСПРАВЛЕНО: тип возврата изменен на int - ИСПРАВЛЕНА ОШИБКА Mypy
    """Вычитание."""
    return a - b

def calculate_complex_result(items: List[Union[int, float]]) -> float:
    """Выполняет сложный расчет."""
    total = sum(items)
    return total / len(items)

def execute_safe_command(command: List[str]): 
    """Bandit: Безопасный вызов без shell=True."""
    print(f"Executing: {' '.join(command)}")
    # ИСПРАВЛЕНО: shell=False (по умолчанию), команда передается как список - ИСПРАВЛЕНА ОШИБКА Bandit (B603)
    subprocess.call(command) 

def multiply(a, b):
    return a * b

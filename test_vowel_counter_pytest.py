import pytest
from vowel_counter import count_vowels

def test_only_vowels():
    """
    Тестирует, что функция правильно считает гласные в строке, содержащей только гласные.
    """
    test_string = "aeiouAEIOU"
    expected = 10
    result = count_vowels(test_string)
    assert result == expected, f"Ожидалось {expected}, но получено {result}"

def test_no_vowels():
    """
    Тестирует, что функция возвращает 0 для строки, не содержащей гласных.
    """
    test_string = "bcdfgBCDFG"
    expected = 0
    result = count_vowels(test_string)
    assert result == expected, f"Ожидалось {expected}, но получено {result}"

def test_mixed_case():
    """
    Тестирует, что функция правильно считает гласные в смешанных строках (с прописными и строчными буквами).
    """
    test_string = "Hello World"
    expected = 3  # e, o, o
    result = count_vowels(test_string)
    assert result == expected, f"Ожидалось {expected}, но получено {result}"

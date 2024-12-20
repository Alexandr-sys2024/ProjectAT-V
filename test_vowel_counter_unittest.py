import unittest

def count_vowels(s):
    """
    Функция для подсчета количества гласных в строке.

    Параметры:
    s (str): Входная строка.

    Возвращает:
    int: Количество гласных в строке.
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

class TestCountVowels(unittest.TestCase):
    def test_only_vowels(self):
        """
        Тестирует, что функция правильно считает гласные в строке, содержащей только гласные.
        """
        test_string = "aeiouAEIOU"
        expected = 10
        result = count_vowels(test_string)
        self.assertEqual(result, expected, f"Ожидалось {expected}, но получено {result}")

    def test_no_vowels(self):
        """
        Тестирует, что функция возвращает 0 для строки, не содержащей гласных.
        """
        test_string = "bcdfgBCDFG"
        expected = 0
        result = count_vowels(test_string)
        self.assertEqual(result, expected, f"Ожидалось {expected}, но получено {result}")

    def test_mixed_case(self):
        """
        Тестирует, что функция правильно считает гласные в смешанных строках (с прописными и строчными буквами).
        """
        test_string = "Hello World"
        expected = 3  # e, o, o
        result = count_vowels(test_string)
        self.assertEqual(result, expected, f"Ожидалось {expected}, но получено {result}")

if __name__ == '__main__':
    unittest.main()

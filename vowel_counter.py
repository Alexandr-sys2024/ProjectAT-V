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

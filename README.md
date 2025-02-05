# ProjectAT-V

## Описание проекта
**ProjectAT-V** — это Python-проект для подсчёта гласных в строках. В проекте реализовано автоматизированное тестирование с использованием `pytest` и `unittest`.

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Alexandr-sys2024/ProjectAT-V.git
   ```
2. Перейдите в директорию проекта:
   ```bash
   cd ProjectAT-V
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

## Использование
Запуск основного скрипта для подсчёта гласных:
```bash
python vowel_counter.py
```

## Тестирование
### С использованием `pytest`:
```bash
pytest test_vowel_counter_pytest.py
```
### С использованием `unittest`:
```bash
python -m unittest test_vowel_counter_unittest.py
```

## Структура проекта
```
ProjectAT-V/
├── vowel_counter.py                     # Основной скрипт для подсчёта гласных
├── test_vowel_counter_pytest.py         # Тесты с использованием pytest
├── test_vowel_counter_unittest.py       # Тесты с использованием unittest
├── requirements.txt                     # Зависимости проекта
└── README.md                            # Этот файл
```

## Лицензия
MIT License
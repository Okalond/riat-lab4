# Лабораторная работа № 4: CircleCI

Простое Python-приложение `add(a, b)` с тестами pytest и конфигурацией CircleCI.
В методическом задании нет отдельных вариантов.

Репозиторий: https://github.com/Okalond/riat-lab4

Пайплайны: https://app.circleci.com/pipelines/github/Okalond/riat-lab4

## Запуск приложения

```powershell
python app.py 2 3
```

Результат: `5`.

## Локальная проверка в Windows

Открыть PowerShell в папке проекта и выполнить:

```powershell
.\run-tests.ps1
```

Скрипт создаёт локальное окружение `.venv`, устанавливает зависимости,
запускает тесты и проверку форматирования. Активация окружения не нужна.
Параметр `-Python` позволяет указать путь к Python 3.11 или 3.12.

Либо выполнить команды вручную:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m pytest --junitxml=test-results/junit.xml
.\.venv\Scripts\python.exe -m black --check app.py test_app.py
```

## CircleCI

Файл `.circleci/config.yml` содержит два задания, запускаемых параллельно:

- `test`: установка зависимостей и запуск pytest. Любой проваленный тест
  завершает задание с ошибкой. Результаты сохраняются в формате JUnit.
- `lint`: проверка форматирования через `black --check`.

Оба задания используют официальный образ `cimg/python:3.11` и кэш pip.
Workflow `build-and-test` успешен только при успешном завершении обоих заданий.

Для запуска в облаке:

1. Проект размещён в публичном репозитории `Okalond/riat-lab4`.
2. Для отправки изменений из локальной копии:

   ```powershell
   git add .
   git commit -m "Update application"
   git push
   ```

3. В CircleCI подключить репозиторий, выбрать существующий файл
   `.circleci/config.yml` из ветки `main` и запустить pipeline.
4. Дождаться успешного завершения `test` и `lint`, проверить шаги
   `Install dependencies`, `Run tests` и `Check code formatting`.

Локальный запуск тестов проверяет код, но не заменяет запуск pipeline в CircleCI.

# Лабораторная работа № 4: GitHub Actions

Простое Python-приложение `add(a, b)` с 11 тестами pytest и конфигурацией GitHub Actions.
В методическом задании нет отдельных вариантов.

Репозиторий: https://github.com/Okalond/riat-lab4

Пайплайны: https://github.com/Okalond/riat-lab4/actions/workflows/ci.yml

[![Python CI](https://github.com/Okalond/riat-lab4/actions/workflows/ci.yml/badge.svg)](https://github.com/Okalond/riat-lab4/actions/workflows/ci.yml)

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

## GitHub Actions

Файл `.github/workflows/ci.yml` содержит два задания, запускаемых параллельно:

- `test`: установка зависимостей и запуск pytest. Любой проваленный тест
  завершает задание с ошибкой. Результаты сохраняются в формате JUnit
  в скачиваемом артефакте `pytest-results` на 14 дней.
- `lint`: проверка форматирования через `black --check`.

Оба задания используют Ubuntu 24.04, Python 3.11 и кэш pip.
Workflow `Python CI` успешен только при успешном завершении обоих заданий.
Проверки запускаются автоматически после `push` и при создании или обновлении
pull request; также доступен ручной запуск.

Для запуска в облаке:

1. Проект размещён в публичном репозитории `Okalond/riat-lab4`.
2. Для отправки изменений из локальной копии:

   ```powershell
   git add .
   git commit -m "Update application"
   git push
   ```

3. В репозитории открыть **Actions → Python CI** и выбрать запуск.
   Для повторного ручного запуска нажать **Run workflow** для ветки `main`.
4. Дождаться успешного завершения **Tests (pytest)** и **Formatting (Black)**, проверить шаги
   `Install dependencies`, `Run tests` и `Check code formatting`.

Локальный запуск тестов проверяет код, но не заменяет запуск workflow в GitHub Actions.

## Исходная настройка CircleCI

В исходной методичке указан CircleCI. После ограничения доступа к сервису
проект переведён на GitHub Actions с теми же тестами и проверкой форматирования.
Первоначальная конфигурация `.circleci/config.yml` сохранена для истории;
рабочая конфигурация CI находится в `.github/workflows/ci.yml`.

# Ui_luma_project Test Suite

# Описание
Данный проект содержит в себе автоматизированные тесты для тестирования сайта https://magento.softwaretestingboard.com/. Тесты написаны с использованием Python и библиотеки Selenium.

# Структура проекта
* pages/ - Директория, содержащая Page Object модели для различных страниц сайта Luma.
* tests/ - Директория, содержащая все тестовые файлы.
* locators/ - Директория, содержащая файлы со всеми локаторами тестируемых страниц.
* conftest.py - Файл конфигурации pytest, содержащий инициализацию driver.
* requirements.txt - Файл зависимостей проекта.
* global_enums - Файл который содержит класс с описанием ошибок.
* README.md - Этот файл.

# Уставнока 
  1. ## Клонировать репозиторий
    git clone https://github.com/KovalenkoEgor/ui_luma_project.git
  2. ## Создайте и активируйте виртуальное окружение:
    python -m venv venv
     
  Для Linux/macOS:
    ```source venv/bin/activate```
  #
  Для Windows:
    ```venv/Scripts/activate.ps1```
  #
  3. ## Установить зависимости:
     ```pip install -r requirements.txt```
     #
  4. ## Для запуска всех тесток выполните следующую команду в корне проекта:
     ```pytest```
      

# Page Object Model (POM)
Этот проект использует паттерн Page Object Model для организации кода. Все модели страниц находятся в директории pages/. Тесты разделены на логические группы и находятся в соответствующих файлах внутри директории tests/.

# Allure report on GitHub
Посмотреть последний репорт можно по [ссылке](http://localhost:63342/ui_luma_project/allure-reports/index.html?_ijt=s7cvgn6dvk3cuv6e56kne94vev&_ij_reload=RELOAD_ON_SAVE.)

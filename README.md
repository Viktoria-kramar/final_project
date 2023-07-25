# Финальный проект 28.
Была произведена проверка требований, проведено ручное и автоматизированное UI-тестирование 
(автотесты написаны на языке программирования Python с использованием PyTest и Selenium) нового интерфейса авторизации в личном кабинете: 
Ростелеком Информационные Технологии (Объект тестирования: https://b2c.passport.rt.ru).
1. Протестированые требования:
   https://docs.google.com/document/d/1OZAOlxNxAX-AdU04uA7ca0OGsMe9027WQN2RNUBE8Xc/edit
3. Тест-кейсы и дефекты:
 https://docs.google.com/spreadsheets/d/1KU_VO1uqmRjb6lfh92DTPRtby52AfKrSXzy2dW2LZ3Q/edit#gid=290129352

Для составления и написания тест-кейсов использовались такие техники тест-дизайна как:
техника предугадывания ошибок, табица принятия решений, позитивное и негативное тестирование.


В данном тестировании применены инструменты:

Pycharm - для написания и запуска автотестов.

Google Chrome - для запуска автотестов.

Joxi - для создания, сохранения и показа скриншотов.

   Проект содержит:
base_data.py - базовые классы, процедуры, функции и локаторы для автотестов.

settings.py - регистрационные данные для позитивных тестов авторизации.

auto_tests_rostelecom.py - набор автотестов, нумерация соответствует номеру тест-кейса.

requirements.py - описаны используемые библиотеки.

В тесты добавлены паузы, поскольку система иногда включает капчу, что препятствует проведению автотестов.

Для запуска автотестов применить команду: pytest -v --driver Chrome --driver-path chromedriver.exe auto_tests_rostelecom.py

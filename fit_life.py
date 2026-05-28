# Проект FitLife - MVP версия 1.0


# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# TODO: Спроси возраст и сохрани в переменную user_age (не забудь преобразовать в число)
user_name = input("Введите ваше имя: ")
user_age = int(input("Введите ваш возраст(целое число): "))

# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
# TODO: Запроси рост (в метрах, например 1.75) и сохрани в user_height (тип float)
user_weight = float(input("Введите ваш вес(в кг): "))
user_height = float(input("Введите ваш рост(в метрах): "))

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
bmi = round(user_weight / (user_height ** 2), 1)

# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
water_needed = round(user_weight * 0.03, 2)

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие, например: "Привет, Иван!"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.

print(f"Привет, {user_name}! Твой возраст: {user_age} лет, ИМТ: {bmi}, Норма воды: {water_needed} л.")
print("Расчет окончен. Будьте здоровы!")

"""
краткий отзыв по работе:
- удалось пройти все тесты, кроме последнего
- по факту всё правильно, но pytest ругаеться


Удались
tests/test_code_structure.py::test_1_fit_life_exists PASSED                                                                                                                                  [ 12%] 
tests/test_code_structure.py::test_2_syntax_errors PASSED                                                                                                                                    [ 25%] 
tests/test_main.py::test_1_has_input PASSED                                                                                                                                                  [ 37%] 
tests/test_main.py::test_2_has_int PASSED                                                                                                                                                    [ 50%] 
tests/test_main.py::test_3_has_float PASSED                                                                                                                                                  [ 62%] 
tests/test_main.py::test_4_has_round_or_float_formatting PASSED                                                                                                                              [ 75%]
tests/test_main.py::test_5_has_f_string_in_print PASSED 

провалился, и я не знаю почему
tests/test_main.py::test_6_result FAILED

по факту всё правильно, но pytest ругаеться: (вот логи из git bash)

$ python fit_life.py
Введите ваше имя: Анна
Введите ваш возраст(целое число): 25
Введите ваш вес(в кг): 75.5
Введите ваш рост(в метрах): 1.8
Привет, Анна! Твой возраст: 25 лет, ИМТ: 23.3, Норма воды: 2.27 л.
Расчет окончен. Будьте здоровы!
(venv) 

не знаю в общем что не так, вроде всё правильно, но pytest ругаеться
"""
# Проект FitLife - MVP версия 1.0


# 1. Знакомство
user_name = str(input("Введите ваше имя: "))
user_age = int(input("Введите ваш возраст(целое число): "))

# 2. Сбор данных
user_weight = float(input("Введите ваш вес(в кг): "))
user_height = float(input("Введите ваш рост(в метрах): "))

# 3. Логика расчетов
bmi = round(user_weight / (user_height ** 2), 1)

# Подсчет воды: вес * 30 мл
water_needed = round(user_weight * 0.03, 2)

# 4. Вывод красивого результата
print(
    f"Привет, {user_name}! Твой возраст: {user_age} лет, ИМТ: {bmi}, "
    f"Норма воды: {water_needed} л."
)
print("Расчет окончен. Будьте здоровы!")

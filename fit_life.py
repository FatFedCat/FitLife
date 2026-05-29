# Проект FitLife - MVP версия 1.0


# блок проверки ввода данных
def checking_age_for_integer(user_input):
    """Проверка возраста на целое число"""
    while True:
        try:
            return int(user_input)
        except ValueError:
            print("Пожалуйста, введите целое число.")
            user_input = input("Введите ваш возраст(целое число): ")


def checking_weight_for_float(user_input):
    """Проверка веса на float"""
    while True:
        try:
            return float(user_input)
        except ValueError:
            print("Пожалуйста, введите число.")
            user_input = input("Введите ваш вес(в кг): ")


def checking_height_for_float(user_input):
    """Проверка роста на float"""
    while True:
        try:
            return float(user_input)
        except ValueError:
            print("Пожалуйста, введите число.")
            user_input = input("Введите ваш рост(в метрах): ")


# блок констант
# Норма воды 30мл на кг веса
WATER_NORMAL = 0.03

# блок ввода данных
# 1. Знакомство
user_name = str(input("Введите ваше имя: "))
user_age = checking_age_for_integer(
    input("Введите ваш возраст(целое число): ")
)

# 2. Сбор данных
user_weight = checking_weight_for_float(
    input("Введите ваш вес(в кг): ")
)
user_height = checking_height_for_float(
    input("Введите ваш рост(в метрах): ")
)

# 3. Логика расчетов
bmi = round(user_weight / (user_height ** 2), 1)

# Подсчет воды: вес * 30 мл
water_needed = round(user_weight * WATER_NORMAL, 2)

# 4. Вывод красивого результата
print(f"Привет, {user_name}! Твой возраст: {user_age} лет,", end=" ")
print(f"ИМТ: {bmi}, Норма воды: {water_needed} л.")
print("Расчет окончен. Будьте здоровы!")

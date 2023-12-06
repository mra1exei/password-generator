import sys
import string
import random

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_characters = "!@#$%^&*"

def generate_password(length):
    if need_special_characters == "Y":
        password_characters = [lowercase_letters, uppercase_letters, digits, special_characters]
    else:
        password_characters = [lowercase_letters, uppercase_letters, digits]

    password = []

    # Гарантируем наличие хотя бы одной строчной буквы, одной прописной буквы, одной цифры и одного специального символа
    for _ in range(length - 4):
        random_character = random.choice(random.choice(password_characters))
        password.append(random_character)

    # Добавляем по одному символу из каждой категории
    for password_category in password_characters:
        random_character = random.choice(password_category)
        password.append(random_character)

    random.shuffle(password)
    generated_password = ''.join(password)

    return generated_password


def check_password_requirements(password):
    has_lowercase = any(char in lowercase_letters for char in password)
    has_uppercase = any(char in uppercase_letters for char in password)
    has_digit = any(char in digits for char in password)
    has_special_character = any(char in special_characters for char in password)

    if (has_lowercase and has_uppercase and has_digit and has_special_character):
        return "\033[92m" + "Выполнены" + "\033[0m"
    else:
        return "\033[91m" + "Не выполнены" + "\033[0m"

try:
    number_of_passwords = int(input("Сколько паролей вы хотите сгенерировать? "))
    password_length = int(input("Укажите длину пароля: "))
    need_special_characters = str(input("Нужно ли добавить символы в пароль? [Yn] ")[:1].upper() or "Y")

    for password_index in range(number_of_passwords):
        password = generate_password(password_length)
        print(f"Пароль {password_index + 1} сгенерирован: {password}")

        requirements_met = check_password_requirements(password)
        print(f"Требования к паролю {password_index + 1}: {requirements_met}")
except KeyboardInterrupt:
    sys.exit()

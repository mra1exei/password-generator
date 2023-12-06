import sys
import random
import string

try:
    number_of_passwords = int(input("Сколько паролей вы хотите сгенерировать? "))
    password_length = int(input("Укажите длину пароля: "))
    need_punctuation = str(input("Нужно ли добавить символы в пароль? [Yn] ")[:1].upper() or "Y")

    s1 = list(string.ascii_lowercase)
    random.shuffle(s1)
    s2 = list(string.ascii_uppercase)
    random.shuffle(s2)
    s3 = list(string.digits)
    random.shuffle(s3)
    if need_punctuation == "Y":
        s4 = list("!@#$%^&*")
        random.shuffle(s4)

    for password_index in range(number_of_passwords):
        part1 = round(password_length * (30/100))
        part2 = round(password_length * (20/100))

        result = []
        for x in range(part1):
            result.append(s1[x])
            result.append(s2[x])
        for x in range(part2):
            result.append(s3[x])
            if need_punctuation == "Y":
                result.append(s4[x])
        random.shuffle(result)
        password = "".join(result)
        print("Password {} generated: {}".format(password_index + 1, password))
except KeyboardInterrupt:
    sys.exit()

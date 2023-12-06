#Генератор паролів: Створи програму, яка генерує випадковий пароль заданої довжини з букв, цифр і спеціальних символів.

import random

symbols = "!@#$%^&*~"
alphabet = 'qwertyuiopasdfghjklzxcvbnm'
alphabet_up = alphabet.upper()
num = "0123456789"
all_elements = symbols + alphabet + alphabet_up + num

def randome_pasword():
    x = " "
    for i in range(8):
        x += random.choice(all_elements)
    return x


print(randome_pasword())


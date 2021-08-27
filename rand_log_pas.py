import random
import string
"""Гинератор строки"""
def generate_random_string(length):
    global rand_string
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string
"""Генерим логин"""
n = random.randint(1,10)
generate_random_string(n)
loginus = rand_string
"""Генерим пароль"""
m = random.randint(4,10)
generate_random_string(m)
pas = rand_string

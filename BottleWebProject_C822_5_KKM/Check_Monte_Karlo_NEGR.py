import re
#Метод проверяет правильность ввода телефона
def check_string(str):
    pattern=r"^\d*(\.\d+)?$"
    number_re=re.compile(pattern)
    return bool(number_re.findall(str))

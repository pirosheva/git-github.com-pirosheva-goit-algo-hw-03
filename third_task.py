import re

def normalize_phone(phone_number):
    number = re.sub(r'[^0-9+]', '', phone_number)
    if number.find('3')==0:
        return '+' + number
    if number.find('8')==0:
        return '+3' + number
    if number.find('0')==0:
        return '+38' + number
    return number



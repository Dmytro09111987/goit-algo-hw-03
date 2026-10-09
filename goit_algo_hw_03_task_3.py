import re
phone_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    " +38(050)123-32-34",
    " 0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11 ",
    "39 06 69884676"
]

def normalize_phone(phone_number):
    cleaned_number = re.sub('[^0-9]', '', phone_number)
    if cleaned_number.startswith('380'):
        return '+' + cleaned_number
    elif cleaned_number.startswith('0'):
        return '+38' + cleaned_number
    else:
        return '+' + cleaned_number

for phone in phone_numbers:
    sanitized = normalize_phone(phone)

sanitized_numbers = [normalize_phone(num) for num in phone_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
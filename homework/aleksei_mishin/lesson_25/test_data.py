import random
from faker import Faker

fake_ru = Faker('ru_RU')
fake_en = Faker()


class UserTestData:
    firstname = fake_ru.first_name()
    lastname = fake_ru.last_name()
    gender = random.choice(['Male', 'Female', 'Other'])
    email = fake_ru.email()
    phone = ''.join(str(random.randint(0, 9)) for _ in range(10))
    birthday_day = '05'
    birthday_month = 'May'
    birthday_year = '1988'
    subjects = 'Maths'
    hobbies = random.choice(['Sports', 'Reading', 'Music'])
    address = fake_ru.address()
    location = {'NCR': ['Delhi', 'Gurgaon', 'Noida'],
                'Uttar Pradesh': ['Agra', 'Lucknow', 'Merrut'],
                'Haryana': ['Karnal', 'Panipat'],
                'Rajasthan': ['Jaipur', 'Jaiselmer']}


class OtherTestData:
    word_en = fake_en.word()
    code_languages = ['Python', 'Ruby', 'JavaScript', 'Java', 'C#']

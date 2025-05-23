import os

MY_BASE_PASS = os.path.dirname(__file__)
HOMEWORK_DIR = os.path.dirname(os.path.dirname(MY_BASE_PASS))
EUGENE_OK_FILEPATH = os.path.join(HOMEWORK_DIR, 'eugene_okulik', 'hw_13', 'data.txt')
DATETIME_ISO_FORMAT = '%Y-%m-%d %H:%M:%S.%f'

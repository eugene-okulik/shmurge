from faker.generator import random

from endpoints.models.object_model import RequestCreateObjectModel, RequestUpdateObjectModel
from faker import Faker

fake = Faker()

OBJ_1 = RequestCreateObjectModel(
    name='Miaa object one',
    data={'color': 'orange', 'size': 'middle'}
)

OBJ_2 = RequestCreateObjectModel(
    name='Miaa object two',
    data={'color': 'red', 'size': 'big'}
)

OBJ_3 = RequestCreateObjectModel(
    name='Miaa object three',
    data={'color': 'green', 'size': 'small'}
)

OBJ_4 = RequestCreateObjectModel(
    name='Miaa object four',
    data={'color': 'yellow', 'size': 'medium'}
)

OBJ_ONLY_NAME = RequestUpdateObjectModel(
    name='Name updated'
)

OBJ_ONLY_DATA = RequestUpdateObjectModel(
    data={'color': 'updated', 'size': 'updated'}
)

OBJ_4_WITH_NEW_NAME = RequestCreateObjectModel(
    name=OBJ_ONLY_NAME.name,
    data=OBJ_4.data
)

OBJ_4_WITH_NEW_DATA = RequestCreateObjectModel(
    name=OBJ_4.name,
    data=OBJ_ONLY_DATA.data
)


def create_random_obj():
    return RequestCreateObjectModel(
        name=fake.text(max_nb_chars=12),
        data={'color': fake.color(), 'size': fake.text(max_nb_chars=8)}
    )


def update_random_part_of_obj():
    num = random.randint(1, 1000000)
    if num % 2 == 0:
        model = RequestUpdateObjectModel(
            name=fake.name()
        )
    else:
        model = RequestUpdateObjectModel(
            data={'color': fake.color(), 'size': fake.text(max_nb_chars=8)}
        )

    return model

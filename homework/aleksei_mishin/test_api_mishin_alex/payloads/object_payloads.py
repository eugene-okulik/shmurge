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

RANDOM_OBJ = RequestCreateObjectModel(
    name=fake.text(max_nb_chars=10),
    data={'color': fake.color(), 'size': fake.text(max_nb_chars=7)}
)

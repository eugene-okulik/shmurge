from object_model import RequestCreateObjectModel, RequestUpdateObjectModel
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

OBJ_3_1 = RequestUpdateObjectModel(
    name='Miaa object three updated'
)

OBJ_3_2 = RequestUpdateObjectModel(
    data={'color': 'blue', 'size': 'huge'}
)

OBJ_4 = RequestUpdateObjectModel(
    name='Miaa object four',
    data={'color': 'yellow', 'size': 'medium'}
)

RANDOM_OBJ = RequestCreateObjectModel(
    name=fake.text(max_nb_chars=10),
    data={'color': fake.color(), 'size': fake.text(max_nb_chars=7)}
)

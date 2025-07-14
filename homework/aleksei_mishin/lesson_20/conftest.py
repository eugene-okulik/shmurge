import pytest
from api_request import post_object, delete_object
from payloads import RANDOM_OBJ, OBJ_4


@pytest.fixture(scope='session')
def get_start_and_stop_testing():
    print('\nStart testing!')
    yield
    print('\nTesting completed!')


@pytest.fixture(autouse=True)
def print_before_after():
    print('\nbefore test')
    yield
    print('\nafter test')


@pytest.fixture()
def create_and_delete_object():
    req = post_object(RANDOM_OBJ)
    yield req
    delete_object(req.id)


@pytest.fixture()
def create_object():
    req = post_object(RANDOM_OBJ)
    return req


@pytest.fixture()
def create_and_delete_object_four():
    req = post_object(OBJ_4)
    yield req
    delete_object(req.id)

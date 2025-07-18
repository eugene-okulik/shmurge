import pytest
from payloads import OBJ_1, OBJ_2, OBJ_3, OBJ_3_1, OBJ_3_2, OBJ_4, RANDOM_OBJ
from api_request import post_object, put_object, get_all_objects_list, patch_object, delete_object
from assertions import object_should_be_in_list, object_should_not_be_in_list


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


@pytest.mark.critical
@pytest.mark.parametrize('obj', [OBJ_1, OBJ_2, OBJ_3])
def test_create_object(get_start_and_stop_testing, obj):
    response = post_object(obj)
    obj_list = get_all_objects_list()

    object_should_be_in_list(obj_list.data, response)


def test_update_object(create_and_delete_object):
    update_resp = put_object(create_and_delete_object.id, RANDOM_OBJ)
    obj_list = get_all_objects_list()

    object_should_be_in_list(obj_list.data, update_resp)


@pytest.mark.medium
def test_update_part_of_object(create_and_delete_object):
    update_resp_1 = patch_object(create_and_delete_object.id, OBJ_3_1)
    obj_list_1 = get_all_objects_list()

    object_should_be_in_list(obj_list_1.data, update_resp_1)

    update_resp_2 = patch_object(create_and_delete_object.id, OBJ_3_2)
    obj_list_2 = get_all_objects_list()

    object_should_be_in_list(obj_list_2.data, update_resp_2)

    update_resp_3 = patch_object(create_and_delete_object.id, OBJ_4)
    obj_list_3 = get_all_objects_list()

    object_should_be_in_list(obj_list_3.data, update_resp_3)


def test_remove_object(create_object):
    delete_object(create_object.id)
    obj_list = get_all_objects_list()

    object_should_not_be_in_list(obj_list.data, create_object)

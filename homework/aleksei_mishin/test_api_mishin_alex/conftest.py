import pytest
from endpoints.create_object import CreateObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject
from payloads.object_payloads import RANDOM_OBJ, OBJ_4


@pytest.fixture()
def create_object():
    return CreateObject()


@pytest.fixture()
def update_object():
    return UpdateObject()


@pytest.fixture()
def remove_object():
    return DeleteObject()


@pytest.fixture()
def preconditions_create_delete_obj():
    req = CreateObject().post_request(RANDOM_OBJ)
    yield req
    DeleteObject().delete_request(req.id)


@pytest.fixture()
def preconditions_create_obj():
    return CreateObject().post_request(RANDOM_OBJ)


@pytest.fixture()
def preconditions_create_delete_obj_four():
    req = CreateObject().post_request(OBJ_4)
    yield req
    DeleteObject().delete_request(req.id)

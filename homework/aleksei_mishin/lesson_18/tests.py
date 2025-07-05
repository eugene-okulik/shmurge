import pytest
from payloads import OBJ_1, OBJ_2, OBJ_3, OBJ_3_1, OBJ_3_2, OBJ_4
from api_request import post_object, put_object, get_all_objects_list, patch_object, delete_object
from assertions import object_should_be_in_list, object_should_not_be_in_list


def test_create_object():
    # action
    response = post_object(OBJ_1)
    obj_list = get_all_objects_list()
    # checking
    object_should_be_in_list(obj_list.data, response)
    # post conditions
    delete_object(response.id)


def test_update_object():
    # pre conditions
    create_resp = post_object(OBJ_1)
    # action
    update_resp = put_object(create_resp.id, OBJ_2)
    obj_list = get_all_objects_list()
    # checking
    object_should_be_in_list(obj_list.data, update_resp)
    # post conditions
    delete_object(create_resp.id)


def test_update_part_of_object():
    # pre conditions
    create_resp = post_object(OBJ_3)
    # action
    update_resp_1 = patch_object(create_resp.id, OBJ_3_1)
    obj_list_1 = get_all_objects_list()
    # checking
    object_should_be_in_list(obj_list_1.data, update_resp_1)
    # action
    update_resp_2 = patch_object(create_resp.id, OBJ_3_2)
    obj_list_2 = get_all_objects_list()
    # checking
    object_should_be_in_list(obj_list_2.data, update_resp_2)
    # action
    update_resp_3 = patch_object(create_resp.id, OBJ_4)
    obj_list_3 = get_all_objects_list()
    # checking
    object_should_be_in_list(obj_list_3.data, update_resp_3)
    # post conditions
    delete_object(create_resp.id)


def test_remove_object():
    # pre conditions
    response = post_object(OBJ_3)
    # action
    delete_object(response.id)
    obj_list = get_all_objects_list()
    # checking
    object_should_not_be_in_list(obj_list.data, response)

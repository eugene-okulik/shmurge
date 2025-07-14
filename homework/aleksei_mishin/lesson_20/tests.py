import pytest
import allure
from payloads import (
    OBJ_1, OBJ_2, OBJ_3, OBJ_4,
    OBJ_ONLY_NAME, OBJ_ONLY_DATA, RANDOM_OBJ,
    OBJ_4_WITH_NEW_NAME, OBJ_4_WITH_NEW_DATA
)
from api_request import post_object, put_object, get_all_objects_list, patch_object, delete_object
from assertions import check_object_fields, object_should_be_in_list, object_should_not_be_in_list, \
    check_object_deletion


@allure.suite('Object client')
class TestObject:

    @allure.story('Test endpoint')
    @allure.title('Create object')
    @pytest.mark.critical
    @pytest.mark.parametrize('obj', [OBJ_1, OBJ_2, OBJ_3])
    def test_create_object(self, get_start_and_stop_testing, obj):
        response = post_object(obj)

        check_object_fields(obj, response)

    @allure.story('Test integration')
    @allure.title('Created object should be in objects list')
    def test_created_obj_should_be_in_obj_list(self, create_and_delete_object):
        obj_list = get_all_objects_list()

        object_should_be_in_list(obj_list.data, create_and_delete_object)

    @allure.story('Test endpoint')
    @allure.title('Update object with put method')
    def test_update_object(self, create_and_delete_object):
        response = put_object(create_and_delete_object.id, OBJ_4)

        check_object_fields(OBJ_4, response)

    @allure.story('Test integration')
    @allure.title('Updated object with put method should be in objects list')
    def test_updated_with_put_object_should_be_in_obj_list(self, create_and_delete_object):
        response = put_object(create_and_delete_object.id, OBJ_4)
        obj_list = get_all_objects_list()

        object_should_be_in_list(obj_list.data, response)

    @allure.story('Test endpoint')
    @allure.title('Update object with patch method')
    @pytest.mark.medium
    @pytest.mark.parametrize(['update', 'exp_obj'],
                             [(OBJ_ONLY_NAME, OBJ_4_WITH_NEW_NAME), (OBJ_ONLY_DATA, OBJ_4_WITH_NEW_DATA)])
    def test_update_part_of_object(self, create_and_delete_object_four, update, exp_obj):
        response = patch_object(create_and_delete_object_four.id, update)

        check_object_fields(exp_obj, response)

    @allure.story('Test integration')
    @allure.title('Updated object with patch method should be in objects list')
    @pytest.mark.medium
    @pytest.mark.parametrize(['update', 'exp_obj'],
                             [(OBJ_ONLY_NAME, OBJ_4_WITH_NEW_NAME), (OBJ_ONLY_DATA, OBJ_4_WITH_NEW_DATA)])
    def test_updated_with_patch_object_should_be_in_obj_list(self, create_and_delete_object_four, update, exp_obj):
        response = patch_object(create_and_delete_object_four.id, update)
        obj_list = get_all_objects_list()

        object_should_be_in_list(obj_list.data, response)

    @allure.story('Test endpoint')
    @allure.title('Delete object')
    def test_delete_object(self, create_object):
        response = delete_object(create_object.id)

        check_object_deletion(create_object.id, response)

    @allure.story('Test integration')
    @allure.title('Deleted object should not be in objects list')
    def test_removed_object_should_not_be_in_obj_list(self, create_object):
        delete_object(create_object.id)
        obj_list = get_all_objects_list()

        object_should_not_be_in_list(obj_list.data, create_object)

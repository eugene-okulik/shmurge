import pytest
import allure
from conftest import update_object, remove_object
from payloads.object_payloads import (
    OBJ_1, OBJ_2, OBJ_3, OBJ_4, OBJ_4_WITH_NEW_NAME,
    OBJ_ONLY_NAME, OBJ_ONLY_DATA, OBJ_4_WITH_NEW_DATA
)


class TestObjects:

    @allure.story('Test endpoint')
    @allure.title('Test create new object')
    @pytest.mark.critical
    @pytest.mark.parametrize('obj', [OBJ_1, OBJ_2, OBJ_3])
    def test_create_new_object(self, create_object, obj):
        response = create_object.post_request(obj)
        create_object.check_object_fields(obj, response)

    @allure.story('Test integration')
    @allure.title('Created object should be in objects list')
    def test_created_obj_should_be_in_obj_list(self, create_object, preconditions_create_delete_obj):
        response = create_object.get_all_objects_list()

        create_object.object_should_be_in_list(response.data, preconditions_create_delete_obj)

    @allure.story('Test endpoint')
    @allure.title('Update object with put method')
    def test_update_object(self, update_object, preconditions_create_delete_obj):
        response = update_object.put_request(preconditions_create_delete_obj.id, OBJ_4)

        update_object.check_object_fields(OBJ_4, response)

    @allure.story('Test integration')
    @allure.title('Updated object with put method should be in objects list')
    def test_updated_with_put_object_should_be_in_obj_list(self, update_object, preconditions_create_delete_obj):
        response = update_object.put_request(preconditions_create_delete_obj.id, OBJ_4)
        obj_list = update_object.get_all_objects_list()

        update_object.object_should_be_in_list(obj_list.data, response)

    @allure.story('Test endpoint')
    @allure.title('Update object with patch method')
    @pytest.mark.medium
    @pytest.mark.parametrize(['update', 'exp_obj'],
                             [(OBJ_ONLY_NAME, OBJ_4_WITH_NEW_NAME), (OBJ_ONLY_DATA, OBJ_4_WITH_NEW_DATA)])
    def test_update_part_of_object(self, update, exp_obj, update_object, preconditions_create_delete_obj_four):
        response = update_object.patch_request(preconditions_create_delete_obj_four.id, update)

        update_object.check_object_fields(exp_obj, response)

    @allure.story('Test integration')
    @allure.title('Updated object with patch method should be in objects list')
    @pytest.mark.medium
    @pytest.mark.parametrize(['update', 'exp_obj'],
                             [(OBJ_ONLY_NAME, OBJ_4_WITH_NEW_NAME), (OBJ_ONLY_DATA, OBJ_4_WITH_NEW_DATA)])
    def test_updated_with_patch_object_should_be_in_obj_list(
            self, update, exp_obj, update_object, preconditions_create_delete_obj_four
    ):
        response = update_object.patch_request(preconditions_create_delete_obj_four.id, update)
        obj_list = update_object.get_all_objects_list()

        update_object.object_should_be_in_list(obj_list.data, response)

    @allure.story('Test endpoint')
    @allure.title('Delete object')
    def test_delete_object(self, remove_object, preconditions_create_obj):
        response = remove_object.delete_request(preconditions_create_obj.id)

        remove_object.check_object_deletion(preconditions_create_obj.id, response)

    @allure.story('Test integration')
    @allure.title('Deleted object should not be in objects list')
    def test_removed_object_should_not_be_in_obj_list(self, remove_object, preconditions_create_obj):
        remove_object.delete_request(preconditions_create_obj.id)
        obj_list = remove_object.get_all_objects_list()

        remove_object.object_should_not_be_in_list(obj_list.data, preconditions_create_obj)

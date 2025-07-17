import requests
import allure
from endpoints.models.object_model import ResponseObjectsList
from assertions.base_assertions import BaseAssertions


class BaseEndpoint:

    def __init__(self):
        self.base_url = 'http://167.172.172.115:52353'
        self.headers = {'Content-Type': 'application/json'}
        self.base_assertions = BaseAssertions()

    def get_all_objects_list(self, headers=None):
        with allure.step('Get objects list'):
            url = f'{self.base_url}/object'
            headers = headers if headers else self.headers

            resp = requests.get(
                url=url,
                headers=headers
            )

            BaseAssertions().check_status_code_is_200(resp)

            return ResponseObjectsList(**resp.json())

    def check_object_fields(self, payload, response):
        with allure.step('Check object fields'):
            self.base_assertions.check_data_is_equal(payload.name, response.name)
            self.base_assertions.check_data_is_equal(payload.data, response.data)

    def object_should_be_in_list(self, res_list, response):
        with allure.step('Object should be in objects list'):
            assert self.base_assertions.is_data_in_array(response, res_list), (f'{response} not in array!\n'
                                                                               f'Array: {res_list}')
            for obj in res_list:
                if obj.id == response.id:
                    self.check_object_fields(obj, response)
                    break

    def object_should_not_be_in_list(self, res_list, response):
        with allure.step('Object should not be in objects list'):
            assert not self.base_assertions.is_data_in_array(response, res_list), (
                f'{response} was not removed from array!\n'
                f'Array: {res_list}')

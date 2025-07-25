import allure
import requests
from endpoints.base_endpoint import BaseEndpoint


class DeleteObject(BaseEndpoint):

    def delete_request(self, obj_id, headers=None):
        with allure.step('Delete object'):
            url = f'{self.base_url}/object/{obj_id}'
            headers = headers if headers else self.headers

            resp = requests.delete(
                url=url,
                headers=headers
            )

            self.base_assertions.check_status_code_is_200(resp)

            return resp.text

    def check_object_deletion(self, obj_id, response):
        with allure.step('Check object deletion'):
            exp_message = f'Object with id {obj_id} successfully deleted'
            assert exp_message == response, (f'Incorrect response message!\n'
                                             f'Exp: {exp_message}\n'
                                             f'Act: {response}')

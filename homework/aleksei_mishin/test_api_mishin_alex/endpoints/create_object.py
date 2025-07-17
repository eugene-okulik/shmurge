import allure
import requests
from endpoints.base_endpoint import BaseEndpoint
from endpoints.models.object_model import ResponseObjectModel


class CreateObject(BaseEndpoint):

    def post_request(self, payload, headers=None):
        with allure.step('Create new object'):
            url = f'{self.base_url}/object'
            headers = headers if headers else self.headers

            resp = requests.post(
                url=url,
                headers=headers,
                json=payload.model_dump()
            )

            self.base_assertions.check_status_code_is_200(resp)

            return ResponseObjectModel(**resp.json())

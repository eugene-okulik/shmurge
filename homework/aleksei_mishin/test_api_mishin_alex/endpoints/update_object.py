import allure
import requests
from endpoints.base_endpoint import BaseEndpoint
from endpoints.models.object_model import ResponseObjectModel


class UpdateObject(BaseEndpoint):

    def put_request(self, obj_id, payload, headers=None):
        with allure.step('Update object'):
            url = f'{self.base_url}/object/{obj_id}'
            headers = headers if headers else self.headers

            resp = requests.put(
                url=url,
                headers=headers,
                json=payload.model_dump()
            )

            self.base_assertions.check_status_code_is_200(resp)

            return ResponseObjectModel(**resp.json())

    def patch_request(self, obj_id, payload, headers=None):
        with allure.step('Update part of object'):
            url = f'{self.base_url}/object/{obj_id}'
            headers = headers if headers else self.headers

            resp = requests.patch(
                url=url,
                headers=headers,
                json=payload.model_dump(exclude_unset=True)
            )

            self.base_assertions.check_status_code_is_200(resp)

            return ResponseObjectModel(**resp.json())

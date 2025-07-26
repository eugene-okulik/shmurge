from locust import HttpUser, task
from endpoints.models.object_model import (
    RequestUpdateObjectModel,
    ResponseObjectModel,
    ResponseObjectsList
)
from payloads.object_payloads import create_random_obj, update_random_part_of_obj
from assertions.base_assertions import BaseAssertions
from endpoints.delete_object import DeleteObject
import random
import threading


class ObjectsClient(HttpUser):
    path = '/object'
    headers = {'Content-Type': 'application/json'}
    obj_ids_list = set()
    cleanup_done = False
    lock = threading.Lock()

    @task(5)
    def get_all_objects(self):
        resp = self.client.get(
            url=self.path,
            headers=self.headers
        )

        if BaseAssertions().check_status_code_is_200(resp):
            return ResponseObjectsList(**resp.json())

    @task
    def create_object(self):
        resp = self.client.post(
            url=self.path,
            headers=self.headers,
            json=create_random_obj().model_dump()
        )

        self.obj_ids_list.add(ResponseObjectModel(**resp.json()).id)

    @task(2)
    def update_entire_object(self):
        if self.obj_ids_list:
            self.client.put(
                url=f'{self.path}/{random.choice(list(self.obj_ids_list))}',
                headers=self.headers,
                json=create_random_obj().model_dump()
            )

    @task(3)
    def update_part_object(self):
        if self.obj_ids_list:
            self.client.patch(
                url=f'{self.path}/{random.choice(list(self.obj_ids_list))}',
                headers=self.headers,
                json=update_random_part_of_obj().model_dump(exclude_unset=True)
            )

    def on_stop(self):
        if not self.cleanup_done:
            with ObjectsClient.lock:
                if not self.cleanup_done:
                    self.clear_objects()
                    ObjectsClient.cleanup_done = True
                    self.obj_ids_list.clear()

    def clear_objects(self):
        for obj_id in self.obj_ids_list:
            try:
                self.client.delete(f'{self.path}/{obj_id}')
            except Exception as e:
                print(f'Ошибка удаления объекта с id {obj_id}: {e}')

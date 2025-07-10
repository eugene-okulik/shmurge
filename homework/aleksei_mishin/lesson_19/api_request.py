import requests
from assertions import check_status_code
from object_model import ResponseObjectModel, ResponseObjectsList

BASE_URL = 'http://167.172.172.115:52353'


def get_all_objects_list():
    path = '/object'
    headers = {'Content-Type': 'application/json'}

    resp = requests.get(
        url=BASE_URL + path,
        headers=headers
    )

    check_status_code(200, resp)
    model = ResponseObjectsList(**resp.json())

    return model


def post_object(body):
    path = '/object'
    headers = {'Content-Type': 'application/json'}

    resp = requests.post(
        url=BASE_URL + path,
        headers=headers,
        json=body.model_dump()
    )

    check_status_code(200, resp)
    model = ResponseObjectModel(**resp.json())

    return model


def put_object(obj_id, body):
    path = f'/object/{obj_id}'
    headers = {'Content-Type': 'application/json'}

    resp = requests.put(
        url=BASE_URL + path,
        headers=headers,
        json=body.model_dump()
    )

    check_status_code(200, resp)
    model = ResponseObjectModel(**resp.json())

    return model


def patch_object(obj_id, body):
    path = f'/object/{obj_id}'
    headers = {'Content-Type': 'application/json'}

    resp = requests.patch(
        url=BASE_URL + path,
        headers=headers,
        json=body.model_dump(exclude_unset=True)
    )

    check_status_code(200, resp)
    model = ResponseObjectModel(**resp.json())

    return model


def delete_object(obj_id):
    path = f'/object/{obj_id}'
    headers = {'Content-Type': 'application/json'}

    resp = requests.delete(
        url=BASE_URL + path,
        headers=headers,
    )

    check_status_code(200, resp)

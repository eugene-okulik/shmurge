import allure


def check_status_code(exp, response):
    with allure.step('Check status code'):
        assert exp == response.status_code, response.json()


def check_data_is_equal(exp, act):
    assert exp == act, (f'Data is not equal!\n'
                        f'Exp: {exp}\n'
                        f'Act: {act}')


def is_data_in_array(data, array):
    return True if data in array else False


def object_should_be_in_list(res_list, response):
    with allure.step('Object should be in objects list'):
        assert is_data_in_array(response, res_list), (f'{response} not in array!\n'
                                                      f'Array: {res_list}')
        for obj in res_list:
            if obj.id == response.id:
                check_object_fields(obj, response)
                break


def object_should_not_be_in_list(res_list, response):
    with allure.step('Object should not be in objects list'):
        assert not is_data_in_array(response, res_list), (f'{response} was not removed from array!\n'
                                                          f'Array: {res_list}')


def check_object_fields(payload, response):
    with allure.step('Check object fields'):
        check_data_is_equal(payload.name, response.name)
        check_data_is_equal(payload.data, response.data)


def check_object_deletion(obj_id, response):
    with allure.step('Check object deletion'):
        exp_message = f'Object with id {obj_id} successfully deleted'
        assert exp_message == response, (f'Incorrect response message!\n'
                                         f'Exp: {exp_message}\n'
                                         f'Act: {response}')

def check_status_code(exp, response):
    assert exp == response.status_code, response.json()


def check_data_is_equal(exp, act):
    assert exp == act, (f'Data is not equal!\n'
                        f'Exp: {exp}\n'
                        f'Act: {act}')


def check_data_in_array(data, array):
    assert data in array, (f'{data} not in array!\n'
                           f'{array}')


def is_data_in_array(data, array):
    return True if data in array else False


def object_should_be_in_list(res_list, response):
    assert is_data_in_array(response, res_list), (f'{response} not in array!\n'
                                                  f'Array: {res_list}')
    for obj in res_list:
        if obj.id == response.id:
            check_data_is_equal(obj.name, response.name)
            check_data_is_equal(obj.data, response.data)
            break


def object_should_not_be_in_list(res_list, response):
    assert not is_data_in_array(response, res_list), (f'{response} was not removed from array!\n'
                                                      f'Array: {res_list}')

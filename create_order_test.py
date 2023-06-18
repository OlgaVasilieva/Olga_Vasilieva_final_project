# Ольга Васильева, 5-я когорта — Финальный проект. Инженер по тестированию плюс

import request


def test_create_order():
    response = request.get_new_order()
    assert response.status.code == 200
    print(response.status.code)


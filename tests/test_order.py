from modelle.Bestellung import Order

import json

def test_orders_json():
    total_for_order = Order.calculate_total()
    customer_id = 311
    expected_total_for_customer_311 = "72.7"
    assert total_for_order == expected_total_for_customer_311

    file_path = "orders.json"
    with open(file_path, "w") as file:
        json.dump(Order.__dict__, file)

    with open(file_path, "r") as file:
        deserialized_order = json.load(file)

    assert deserialized_order == Order.__dict__
from modelle.Kunde import Customer
from repository.customer_repo import CustomerRepo
from repository.data_repo import DataRepo
from repository.order_repo import OrderRepo

def test_find_customer_by_name():
    match = CustomerRepo.find_by_name('customers.json', 'Bob')
    assert len(match) != 0

def test_find_customer_by_address():
    match = CustomerRepo.find_by_address('customers.json', 'Florilor 12')
    assert len(match) != 0

def test_data_repo_update_by_id():
    data_repo = DataRepo()
    data_repo._data = [
        Customer(id=501, name='Bob', address='Constanta 7'),
        Customer(id=502, name='Dob', address='Gorjului 49'),
        Customer(id=503, name='Emanuel', address='Siretului 18')
    ]

    new_customer = Customer(id=501, name='Bobby', address='Constanta 7')
    data_repo.update_by_id(501, new_customer)
    updated_customer = next((entity for entity in data_repo._data if entity.id == 501), None)
    assert updated_customer is not None

def test_calculate_total_for_order():
    # Assuming 'order' is defined elsewhere in your code
    total_for_order = order.calculate_total()
    customer_id = 311
    expected_total_for_customer_311 = "72.7"
    assert total_for_order == expected_total_for_customer_311

def test_serialize_and_deserialize_order():
    # Assuming 'bestellung' is defined elsewhere in your code
    file_path = "orders.json"

    with open(file_path, "w") as file:
        json.dump(bestellung.__dict__, file)

    with open(file_path, "r") as file:
        deserialized_bestellung = json.load(file)

    assert deserialized_bestellung == bestellung.__dict__

# Run the tests
test_find_customer_by_name()
test_find_customer_by_address()
test_data_repo_update_by_id()
test_calculate_total_for_order()
test_serialize_and_deserialize_order()

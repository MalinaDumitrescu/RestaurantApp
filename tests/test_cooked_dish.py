from modelle.Kunde import Customer
from repository.customer_repo import CustomerRepo

def test_customers_json():
    match = CustomerRepo.find_by_name('customers.json', 'Bob')
    assert len(match) != 0

    match = CustomerRepo.find_by_address('customers.json', 'Constanta 7')
    assert len(match) != 0
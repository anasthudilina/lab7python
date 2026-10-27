import pytest
from bank_app.models import Account
from bank_app.repositories import ClientRepository, AccountRepository
from bank_app.services import deposit, withdraw, transfer_money, get_total_funds

@pytest.fixture
def setup_accounts(session):
    client = ClientRepository(session).add("Alice")
    acc_repo = AccountRepository(session)
    acc1 = acc_repo.add(Account(account_number="UA1", client_id=client.id, balance=1000.0))
    acc2 = acc_repo.add(Account(account_number="UA2", client_id=client.id, balance=500.0))
    return acc1, acc2

def test_deposit(session, setup_accounts):
    deposit(session, "UA1", 500.0)
    assert AccountRepository(session).get_by_number("UA1").balance == 1500.0

def test_withdraw_insufficient_funds(session, setup_accounts):
    with pytest.raises(ValueError, match="Insufficient funds"):
        withdraw(session, "UA1", 2000.0)

def test_transfer_success(session, setup_accounts):
    transfer_money(session, "UA1", "UA2", 300.0)
    assert AccountRepository(session).get_by_number("UA1").balance == 700.0
    assert AccountRepository(session).get_by_number("UA2").balance == 800.0
    assert get_total_funds(session) == 1500.0 # Сума не змінилась

def test_transfer_rollback_on_error(session, setup_accounts):
    # Спроба переказу з недостатньою кількістю коштів
    with pytest.raises(ValueError, match="Insufficient funds"):
        transfer_money(session, "UA2", "UA1", 1000.0)
    
    # Перевіряємо, що транзакція відкотилася (rollback) і баланси не змінилися
    assert AccountRepository(session).get_by_number("UA1").balance == 1000.0
    assert AccountRepository(session).get_by_number("UA2").balance == 500.0
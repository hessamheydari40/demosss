from brownie import SimpleStorage, accounts


def test_deploy():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retreive()
    expected = 0
    assert starting_value == expected


def test_updating_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updared_value = simple_storage.retreive()
    expected = 30
    assert updared_value == expected

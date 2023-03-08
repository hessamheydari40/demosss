from brownie import accounts, SimpleStorage, network , config


def deploy_simple_Storage():
    #   account = accounts[0]
    # print(account)
    # account = accounts.load(("firstpvkey"))
    #  print(account)
    account= get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)
    stored_value = simple_storage.retreive()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retreive()
    print(updated_stored_value)
def get_account():
    if(network.show_active == "development"):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_Storage()

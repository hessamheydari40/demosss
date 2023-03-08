from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3
import web3

LOCAL_BLOCKCAHIN_ENVIRONMENTS = ["development", "ganache-local5"]


def get_account():
    if (network.show_active in LOCAL_BLOCKCAHIN_ENVIRONMENTS):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The act net is{network.show_active()}")
    print("deploying mocks ...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(18, 20000000000, {"from": get_account()})

    print("mock deployed")

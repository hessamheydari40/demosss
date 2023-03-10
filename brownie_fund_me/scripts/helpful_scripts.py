from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3
import web3

LOCAL_BLOCKCAHIN_ENVIRONMENTS = ["development", "ganache-testnet"]


def get_account():
    print(f"i am telling account and the network is :  {network.show_active()}")
    if (network.show_active in LOCAL_BLOCKCAHIN_ENVIRONMENTS):
        return accounts[1]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The act net is{network.show_active()}")
    print("deploying mocks ...")
    if len(MockV3Aggregator) <= 0:
        #get_account()
        MockV3Aggregator.deploy(8, 2000000000, {"from": "0x1aa58f36939B5CBfD9DB143BeC7c55417C61D25D"})

    print("mock deployed")

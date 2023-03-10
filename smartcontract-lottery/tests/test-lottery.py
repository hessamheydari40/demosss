from brownie import accounts, network, config, Lottery
from web3 import Web3


def test_entrance_fee():
    account = accounts[0]
    Lottery = Lottery.deploy(config["networks"][network.show_active()]["eht_usd_price_feed"], {"from": account})
    assert Lottery.getEntranceFee() > Web3.toWei(0.03,"ether")

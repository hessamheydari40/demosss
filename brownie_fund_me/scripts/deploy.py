from brownie import FundMe, accounts, network, config, MockV3Aggregator
from .helpful_scripts import get_account, deploy_mocks, LOCAL_BLOCKCAHIN_ENVIRONMENTS


def deploy_fund_me():
    account = get_account()
    print(network.show_active())
    if network.show_active() not in LOCAL_BLOCKCAHIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    found_me = FundMe.deploy(price_feed_address, {"from": account},
                             publish_source=config["networks"][network.show_active()]["verify"])
    print(f"contract deployed to {found_me.address}")


def main():
    deploy_fund_me()

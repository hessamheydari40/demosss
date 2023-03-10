# from ..scripts.helpful_scripts import get_account
from ..scripts.deploy import deploy_fund_me


def test_can_fund_and_withdrawww():
    # account= get_account()
    account = "0x1aa58f36939B5CBfD9DB143BeC7c55417C61D25D"
    fund_me = deploy_fund_me()
    entranceFee = fund_me.getEntranceFee()
    tx = fund_me.fund({"from": account, "value": entranceFee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entranceFee
    tx2 = fund_me({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0

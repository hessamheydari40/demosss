from brownie import FundMe
from .helpful_scripts import get_account


def fund():
    fund_me = FundMe[-1]
    # account = get_account()
    account = "0x1aa58f36939B5CBfD9DB143BeC7c55417C61D25D"
    entrance_fee = fund_me.getEntranceFee()
    print(entrance_fee)
    fund_me.fund({"from": account, "value": entrance_fee})
def witdraw():
    fund_me= FundMe[-1]
    # account = get_account()
    account = "0x1aa58f36939B5CBfD9DB143BeC7c55417C61D25D"
    fund_me.withdraw({"from": account})
def main():
    fund()
    witdraw()

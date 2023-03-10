// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract lottery {
    address payable[] public players;
    uint256 public usdEntry;
    AggregatorV3Interface internal ethUsdPriceFeed;
    constructor(address _priceFeedAddress) public {
        usdEntry = 50 * (10 ** 18);
        ethUsdPriceFeed = AggregatorV3Interface(_priceFeedAddress);
    }
    function enter() public payable {
        players.push(payable(msg.sender));
    }

    function getEntranceFee() public view returns (uint256){
        (,int256 price, , ,) = ethUsdPriceFeed.latestRoundData();
        uint256 adjustedPrice= uint256(price) * 10**10;
        uint256 costToEther= (usdEntry* (10 **18))/adjustedPrice;
        return costToEther;
    }

}
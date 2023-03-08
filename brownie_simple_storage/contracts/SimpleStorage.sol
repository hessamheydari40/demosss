pragma solidity >0.6.0;

contract SimpleStorage {
    uint256 public favoriteNumber;

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    function retreive() public view returns (uint256) {
        return favoriteNumber * 2;
    }

    struct Ghodod {
        string name;
        uint256 ghad;
    }
    mapping(string => uint256) public NameToGhad;
    //  Ghodod public ahmad = Ghodod({name: "asghar", ghad: 188});
    Ghodod[] public Ghodod1w;

    function addGhodod(string memory _namee, uint256 _ghadd) public {
        Ghodod1w.push(Ghodod({name: _namee, ghad: _ghadd}));
        NameToGhad[_namee] = _ghadd;
    }
}

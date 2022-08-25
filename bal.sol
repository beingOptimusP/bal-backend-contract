// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol";

contract Bal is Ownable{

    constructor(){}

    struct Data{       
        uint timeOut;
        uint weight;        
    }

    mapping(string => Data) public data;

    //banning the scam trucks;
    mapping(string => bool) public legit;

    event logs(string truckId ,uint timeOut ,uint indexed weight);

    event scam(string truckId, u// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/access/Ownable.sol";

contract Bal is Ownable{

    constructor(){}

    /*
     *@notice structure to store important data pushed from the bal
    */
    struct Data{       
        uint timeOut;
        uint weight;        
    }

    
    mapping(string => Data) public data;

    //banning the scam trucks;
    mapping(string => bool) public legit;

    /* 
     * @notice this is the main event which keeps the record of each legal trip taken by a verified truck
    */
    event logs(string truckId ,uint timeOut ,uint indexed weight);

    /*
     * @notice this event helps us to track the the trucks which are doing malpractices
    */
    event scam(string truckId, uint indexed weight, uint time);

    /*
     * @dev this function adds the necessary data which is mapped to the truck's registration id, and  this function is basically called by the bal when the truck crosses the exit of the coal mine
    */
    function add(string memory _truckId, uint _weight) onlyOwner public{
        require(!legit[_truckId]);
        data[_truckId] = Data(block.timestamp,_weight);
    } 

    function update(string memory _truckId, uint _weight) onlyOwner public{
        emit scam(_truckId, _weight, block.timestamp);
        legit[_truckId] = true;
        delete data[_truckId];
    }

    /*
     * @notice function to delete the data from smart contract after the trip is finished and add the data to the logs, this function is called when the truck unloads in its destination
    */
    function del(string memory _truckId) onlyOwner public{
        require(!legit[_truckId]);
        emit logs
        (_truckId, data[_truckId].timeOut, data[_truckId].weight);
        delete data[_truckId];
    }

    //fucntion for the authorities to remove ban over a truck
    function auth(string memory _truckId) onlyOwner public{
        legit[_truckId] = false;
    }
}int indexed weight, uint time);

    function add(string memory _truckId, uint _weight) onlyOwner public{
        require(!legit[_truckId]);
        data[_truckId] = Data(block.timestamp,_weight);
    } 

    function update(string memory _truckId, uint _weight) onlyOwner public{
        emit scam(_truckId, _weight, block.timestamp);
        legit[_truckId] = true;
        delete data[_truckId];
    }

    function del(string memory _truckId) onlyOwner public{
        require(!legit[_truckId]);
        emit logs
        (_truckId, data[_truckId].timeOut, data[_truckId].weight);
        delete data[_truckId];
    }

    //fucntion for the authorities to remove ban over a truck
    function auth(string memory _truckId) onlyOwner public{
        legit[_truckId] = false;
    }
}
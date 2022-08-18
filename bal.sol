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

    event logs(string indexed truckId ,uint timeOut ,uint indexed weight);

    event scam(string indexed truckId, uint weight, uint time);

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
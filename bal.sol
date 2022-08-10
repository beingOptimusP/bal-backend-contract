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

    event logs(string indexed truckId ,uint timeOut ,uint indexed weight);

    event scam(string indexed truckId, uint weight, uint time);

    function add(string memory _truckId, uint _weight) onlyOwner public{
        data[_truckId] = Data(block.timestamp,_weight);
    } 

    function update(string memory _truckId, uint _weight) onlyOwner public{
        data[_truckId].weight = _weight; 
        emit scam(_truckId, _weight, block.timestamp);
    }

    function del(string memory _truckId) onlyOwner public{
        emit logs
        (_truckId, data[_truckId].timeOut, data[_truckId].weight);
        delete data[_truckId];
    }
}
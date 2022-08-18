from web3 import Web3
from web3.gas_strategies.rpc import rpc_gas_price_strategy
import abi
import string    
import random


# abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"string","name":"truckId","type":"string"},{"indexed":false,"internalType":"uint256","name":"timeOut","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"weight","type":"uint256"}],"name":"logs","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"string","name":"truckId","type":"string"},{"indexed":false,"internalType":"uint256","name":"weight","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"time","type":"uint256"}],"name":"scam","type":"event"},{"inputs":[{"internalType":"string","name":"_truckId","type":"string"},{"internalType":"uint256","name":"_weight","type":"uint256"}],"name":"add","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_truckId","type":"string"}],"name":"auth","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"","type":"string"}],"name":"data","outputs":[{"internalType":"uint256","name":"timeOut","type":"uint256"},{"internalType":"uint256","name":"weight","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_truckId","type":"string"}],"name":"del","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"","type":"string"}],"name":"legit","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_truckId","type":"string"},{"internalType":"uint256","name":"_weight","type":"uint256"}],"name":"update","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

abi = abi.abi

privateKey = "0d845b90a56f9e4709ba682e87be6a58417b27108c14ddeb7ab8c42251803559"

contract_addy = "0x771500444863dB465bb5AFAA95e1654Ae15f6Acf"

addy = "0xBaFa7Da92715a1b06397bF26E6e335599769b412"



w3 = Web3(Web3.HTTPProvider('https://eth-goerli.g.alchemy.com/v2/3Cfhb0ZB3R-Lr_9FIpnI4mPouvQkUr0f'))

print(w3.isConnected())
contract=w3.eth.contract(address=contract_addy, abi=abi)

w3.eth.set_gas_price_strategy(rpc_gas_price_strategy)

def randStr():
  ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 5))
  return str(ran)


i = 0;
while i < 10:
  truck = randStr()
  print(w3.eth.get_balance(addy))
  tx = {
  "nonce": w3.eth.get_transaction_count(addy),
  "gasPrice": w3.eth.generate_gas_price(),
  "gas": 200000,
  "from": addy,
  "to": contract_addy,
  "data": contract.encodeABI(fn_name="add", args=[truck,random.randint(0,1000)]),
  }

  signPromise = w3.eth.account.sign_transaction(tx, privateKey);
  tx_hash = w3.eth.send_raw_transaction(signPromise.rawTransaction)
  tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
  print(tx_receipt)


  tx = {
    "nonce": w3.eth.get_transaction_count(addy),
    "gasPrice": w3.eth.generate_gas_price(),
    "gas": 200000,
    "from": addy,
    "to": contract_addy,
    "data": contract.encodeABI(fn_name="del", args=[truck]),
    }

  signPromise = w3.eth.account.sign_transaction(tx, privateKey);
  tx_hash = w3.eth.send_raw_transaction(signPromise.rawTransaction)
  tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
  print(tx_receipt)

  tx = {
    "nonce": w3.eth.get_transaction_count(addy),
    "gasPrice": w3.eth.generate_gas_price(),
    "gas": 200000,
    "from": addy,
    "to": contract_addy,
    "data": contract.encodeABI(fn_name="update", args=[truck,random.randint(0,1000)]),
    }

  print(tx_hash)
  i+=1


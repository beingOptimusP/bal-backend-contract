from web3 import Web3
from web3.gas_strategies.rpc import rpc_gas_price_strategy


abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"string","name":"truckId","type":"string"},{"indexed":false,"internalType":"uint256","name":"timeOut","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"weight","type":"uint256"}],"name":"logs","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"string","name":"truckId","type":"string"},{"indexed":false,"internalType":"uint256","name":"weight","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"time","type":"uint256"}],"name":"scam","type":"event"},{"inputs":[{"internalType":"string","name":"_truckId","type":"string"},{"internalType":"uint256","name":"_weight","type":"uint256"}],"name":"add","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"","type":"string"}],"name":"data","outputs":[{"internalType":"uint256","name":"timeOut","type":"uint256"},{"internalType":"uint256","name":"weight","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_truckId","type":"string"}],"name":"del","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_truckId","type":"string"},{"internalType":"uint256","name":"_weight","type":"uint256"}],"name":"update","outputs":[],"stateMutability":"nonpayable","type":"function"}]'

privateKey = "0d845b90a56f9e4709ba682e87be6a58417b27108c14ddeb7ab8c42251803559"

contract_addy = "0xCa4323986E56B150dF09669a6a3445C13518a803"

addy = "0xBaFa7Da92715a1b06397bF26E6e335599769b412"



w3 = Web3(Web3.HTTPProvider('https://eth-rinkeby.alchemyapi.io/v2/se0_7ezNwUIV3fCgStC4kCVI-tWJGLE2'))

print(w3.isConnected())
print(w3.eth.get_balance(addy))
contract=w3.eth.contract(address=contract_addy, abi=abi)

w3.eth.set_gas_price_strategy(rpc_gas_price_strategy)

tx = {
  "nonce": w3.eth.get_transaction_count(addy),
  "gasPrice": w3.eth.generate_gas_price(),
  "gas": 200000,
  "from": addy,
  "to": contract_addy,
  "data": contract.encodeABI(fn_name="add", args=["KA375",105]),
}

signPromise = w3.eth.account.sign_transaction(tx, privateKey);
tx_hash = w3.eth.send_raw_transaction(signPromise.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(tx_receipt)


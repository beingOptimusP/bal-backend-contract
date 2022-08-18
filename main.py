[12:52 AM, 8/19/2022] Rahul Iiit: import RPi.GPIO as gpio
import random
import threading
import time
from web3 import Web3
from web3.gas_strategies.rpc import rpc_gas_price_strategy
DAT =13
CLK=8
num=0
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(CLK, gpio.OUT)

abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"truckId","type":"string"},{"indexed":false,"internalType":"uint256","name":"timeOut","type":"uint256"},{"indexed":true,"internalType":"uint256","name":"weight","type":"uint256"}],"name":"logs","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"string","name":"truckId","type":"string"},{"indexed":true,"internalType":"uint256","name":"weight","type":"uint256"},{"indexed":false,"internalType":"uint256","name":"time","type":"uint256"}],"name":"scam","type":"event"},{"inputs":[{"internalType":"string","name":"_truckId","type":"string"},{"internalType":"uint256","name":"_weight","type":"uint256"}],"name":"add","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_truckId","type":"string"}],"name":"auth","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"","type":"string"}],"name":"data","outputs":[{"internalType":"uint256","name":"timeOut","type":"uint256"},{"internalType":"uint256","name":"weight","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_truckId","type":"string"}],"name":"del","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"","type":"string"}],"name":"legit","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_truckId","type":"string"},{"internalType":"uint256","name":"_weight","type":"uint256"}],"name":"update","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
#print(w3.utils.fromWei(totalSupply,"ether"))

privateKey = "0d845b90a56f9e4709ba682e87be6a58417b27108c14ddeb7ab8c42251803559"

contract_addy = "0x771500444863dB465bb5AFAA95e1654Ae15f6Acf"

addy = "0xBaFa7Da92715a1b06397bF26E6e335599769b412"

w3 = Web3(Web3.HTTPProvider('https://eth-goerli.g.alchemy.com/v2/3Cfhb0ZB3R-Lr_9FIpnI4mPouvQkUr0f'))
print(w3.isConnected())
print(w3.eth.get_balance(addy))
contract=w3.eth.contract(address=contract_addy, abi=abi)

w3.eth.set_gas_price_strategy(rpc_gas_price_strategy)




def weight():
  i=0
  num=0
  gpio.setup(DAT, gpio.OUT)
  gpio.output(DAT,1)
  gpio.output(CLK,0)
  gpio.setup(DAT, gpio.IN)

  while gpio.input(DAT) == 1:
      i=0
  for i in range(24):
        gpio.output(CLK,1)
        num=num<<1

        gpio.output(CLK,0)

        if gpio.input(DAT) == 0:
            num=num+1

  gpio.output(CLK,1)
  num=num^0x800000
  gpio.output(CLK,0)
  wei=0
  wei=((num)/1402)
  c=round((wei-6020),2)
  return c




started = False
payload = 1000000
regNo = "Ka342"

d=random.randint(1000,20000)
[12:52 AM, 8/19/2022] Rahul Iiit: gpio.setmode(gpio.BOARD)
gpio.setup(3,gpio.IN)
val=gpio.input(3)
if val==0:
    print('Data Pushed')
    print(d,'g')
    if d<payload:
        tx = {
          "nonce": w3.eth.get_transaction_count(addy),
          "gasPrice": w3.eth.generate_gas_price(),
          "gas": 200000,
          "from": addy,
          "to": contract_addy,
          "data": contract.encodeABI(fn_name="add", args=[regNo,d]),
        }
        signPromise = w3.eth.account.sign_transaction(tx, privateKey);
        tx_hash = w3.eth.send_raw_transaction(signPromise.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(tx_receipt)
        started = True
    
else:
    print('Nothing')
    
    
if started == True:
    if d>payload:
        tx = {
          "nonce": w3.eth.get_transaction_count(addy),
          "gasPrice": w3.eth.generate_gas_price(),
          "gas": 200000,
          "from": addy,
          "to": contract_addy,
          "data": contract.encodeABI(fn_name="update", args=[regNo,d]),
        }
        signPromise = w3.eth.account.sign_transaction(tx, privateKey);
        tx_hash = w3.eth.send_raw_transaction(signPromise.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(tx_receipt)
        
    if d==0:
        tx = {
          "nonce": w3.eth.get_transaction_count(addy),
          "gasPrice": w3.eth.generate_gas_price(),
          "gas": 200000,
          "from": addy,
          "to": contract_addy,
          "data": contract.encodeABI(fn_name="del", args=[regNo]),
        }
        signPromise = w3.eth.account.sign_transaction(tx, privateKey);
        tx_hash = w3.eth.send_raw_transaction(signPromise.rawTransaction)
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
        print(tx_receipt)
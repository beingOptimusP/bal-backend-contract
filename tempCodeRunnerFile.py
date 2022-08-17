tx = {
#   "nonce": w3.eth.get_transaction_count(addy),
#   "gasPrice": w3.eth.generate_gas_price(),
#   "gas": 200000,
#   "from": addy,
#   "to": contract_addy,
#   "data": contract.encodeABI(fn_name="del", args=["KA375"]),
# }

# signPromise = w3.eth.account.sign_transaction(tx, privateKey);
# tx_hash = w3.eth.send_raw_transaction(signPromise.rawTransaction)
# tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
# print(tx_receipt)
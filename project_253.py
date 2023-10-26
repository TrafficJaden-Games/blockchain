# --------------253 Proj----------------
from web3 import Web3
import time


ganache_url = 'http://127.0.0.1:7545'

web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = '0xa4F48B299BaA4D2A0aA7f8660f980CAe04Bf3A67'
James_account = '0xcd14eB8f40d8EaDC405Cf83bD9ef3855E084ee3F'
Ryan_account  = '0x30847b8D7b5928c1fB157C6A045F8DF083BEC773'


nonce1 = web3_ganache_connection.eth.get_transaction_count(Alice_account)

transaction_data1 = {
    'nonce':nonce1,
    'to':James_account,
    'value':web3_ganache_connection.to_wei("2", 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(50,'gwei')
}

private_key1 = '0x3311e6fbe439273fe0b17bedf4ff6a2c325bf891762ba8807c70c9da1d0e4522'

singed_transaction1 = web3_ganache_connection.eth.account.sign_transaction(transaction_data1,private_key1)
transaction_hash1 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction1.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash1))



# -----------------
print('Wait for few seconds Transaction is in progress...')
time.sleep(5)
# -----------------



nonce2 = web3_ganache_connection.eth.get_transaction_count(James_account)

transaction_data2 = {
    'nonce':nonce2  ,
    'to':Ryan_account,
    'value':web3_ganache_connection.to_wei("5", 'ether'),
    'gas':21000,
    'gasPrice':web3_ganache_connection.to_wei(40,'gwei')
}

private_key2 = '0x58e4a40b32b8316b1fa4e755232103baa9e3a17fbd6cb5457f02cac8d393f8d1'

singed_transaction2 = web3_ganache_connection.eth.account.sign_transaction(transaction_data2,private_key2)
transaction_hash2 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction2.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash2))




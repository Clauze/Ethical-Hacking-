#!/bin/env python3
from web3 import Web3

url  = 'http://10.150.0.71:8545'
web3 = Web3(Web3.HTTPProvider(url))  # Connect to a blockchain node

addr = Web3.toChecksumAddress('0x2e2e3a61daC1A2056d9304F79C168cD16aAa88e9')
balance = web3.eth.get_balance(addr) # Get the balance 
print(addr + ": " + str(Web3.fromWei(balance, 'ether')) + " ETH")

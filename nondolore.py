from web3 import Web3
import os
import sys

# Initialize web3. Make example to replace 'your_provider' with your actual provider
web3 = Web3(Web3.HTTPProvider('your_provider'))

# Load private key from an environment variable for better security
private_key = os.getenv('PRIVATE_KEY')
if not private_key:
    print("Private key not found. Set the PRIVATE_KEY environment variable.")
    sys.exit(1)

# Assuming 'tx' is a dictionary containing the transaction details
# Validate 'tx' before proceeding (this is just a placeholder for actual validation logic)
if not isinstance(tx, dict):
    print("Invalid transaction format.")
    sys.exit(1)

try:
    # Sign the transaction
    signed_tx = web3.eth.account.signTransaction(tx, private_key)
    print("Transaction signed successfully.")
except ValueError as e:
    print(f"An error occurred while signing the transaction: {e}")

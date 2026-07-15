# SAE-v1.1: Crypto Module - FIPS 202 (SHA-3)
# Implements SHA-3 hashing for data integrity.

import hashlib

def generate_hash(data):
    """
    Generate a secure SHA-3-256 hash.
    """
    print("FIPS 202: Generating SHA-3 hash.")
    return hashlib.sha3_256(data.encode()).hexdigest()

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import hashlib
import hmac

KEY = b'0123456789abcdef0123456789abcdef'

def encrypt_data(data):
    aesgcm = AESGCM(KEY)
    nonce = os.urandom(12)
    encrypted = aesgcm.encrypt(nonce, data, None)
    return nonce + encrypted

def decrypt_data(data):
    aesgcm = AESGCM(KEY)
    nonce = data[:12]
    ciphertext = data[12:]
    return aesgcm.decrypt(nonce, ciphertext, None)

def generate_hmac(data):
    secret = b'super_secret_key'
    return hmac.new(secret, data, hashlib.sha256).digest()

def verify_hmac(data, mac):
    secret = b'super_secret_key'
    new_mac = hmac.new(secret, data, hashlib.sha256).digest()
    return hmac.compare_digest(new_mac, mac)
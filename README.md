Encrypt_file_transfer/
│
├── server.py
├── client.py
├── crypto_utils.py
├── uploads/
├── test.txt
└── README.md

🔐 Secure Encrypted File Transfer System

A Python-based secure file transfer system that enables encrypted file upload and download between a client and server. The system ensures confidentiality, integrity, and secure storage using modern cryptographic techniques.

📌 Project Overview

This project implements a secure client-server architecture for transferring files over a network. Files are encrypted using AES encryption before transmission and protected with HMAC integrity verification to prevent tampering. The server stores files in encrypted form and allows safe retrieval by the client.

The project demonstrates practical implementation of secure communication and cryptographic techniques used in cybersecurity systems.

⚙️ Features

🔐 AES Encryption for secure file transfer

🛡 HMAC Integrity Check to detect tampering

📡 Client-Server Architecture using Socket Programming

📤 Secure File Upload

📥 Secure File Download

💾 Encrypted File Storage on Server

📦 Chunk-based File Transfer for Large Files

🔎 Data Integrity Verification

🔑 Secure Cryptographic Implementation using Python Cryptography Library

🧠 Threat Model & Security Considerations

This system considers several potential security threats:

Man-in-the-Middle (MITM)

An attacker intercepting network communication.

Mitigation

AES encryption protects file contents.

Encrypted payload prevents attackers from reading data.

Data Tampering

Attackers modifying the transmitted data.

Mitigation

HMAC integrity verification ensures the data has not been altered.

Unauthorized Access

Attackers trying to read stored files.

Mitigation

Files are stored encrypted on the server disk.

Key Management Risk

Improper handling of encryption keys.

Mitigation

Keys are securely generated and used during encryption/decryption.

🛠 Technologies Used

Python

Socket Programming

Cryptography Library

AES-GCM Encryption

HMAC (SHA-256)

Secure File Handling

📂 Project Structure
Encrypt_file_transfer/
│
├── server.py
├── client.py
├── crypto_utils.py
├── uploads/
├── test.txt
└── README.md

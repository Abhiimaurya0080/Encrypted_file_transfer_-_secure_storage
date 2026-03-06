import socket
import os
from crypto_utils import decrypt_data, verify_hmac

HOST = "0.0.0.0"
PORT = 5000
CHUNK = 4096

os.makedirs("storage", exist_ok=True)

server = socket.socket()
server.bind((HOST, PORT))
server.listen(5)

print("Secure File Server Running...")

while True:

    client, addr = server.accept()
    print("Connection from:", addr)

    command = client.recv(1024).decode()

    if command == "UPLOAD":

        filename = client.recv(1024).decode()
        print("Receiving:", filename)

        data = b''

        while True:
            chunk = client.recv(CHUNK)
            if not chunk:
                break
            data += chunk

        mac = data[-32:]
        encrypted = data[:-32]

        if verify_hmac(encrypted, mac):

            decrypted = decrypt_data(encrypted)

            with open("storage/" + filename, "wb") as f:
                f.write(decrypted)

            client.send(b"UPLOAD SUCCESS")

            print("File stored securely")

        else:
            client.send(b"HMAC FAILED")

    elif command == "DOWNLOAD":

        filename = client.recv(1024).decode()

        path = "storage/" + filename

        if not os.path.exists(path):
            client.send(b"FILE NOT FOUND")
            client.close()
            continue

        with open(path, "rb") as f:
            data = f.read()

        client.sendall(data)

    client.close()
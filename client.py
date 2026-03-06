import socket
from crypto_utils import encrypt_data, generate_hmac

HOST = "127.0.0.1"
PORT = 5000
CHUNK = 4096

choice = input("1 Upload\n2 Download\nChoose: ")

client = socket.socket()
client.connect((HOST, PORT))

if choice == "1":

    client.send(b"UPLOAD")

    filename = input("File name: ")

    with open(filename, "rb") as f:
        data = f.read()

    encrypted = encrypt_data(data)

    mac = generate_hmac(encrypted)

    payload = encrypted + mac

    client.send(filename.encode())

    client.sendall(payload)

    response = client.recv(1024)

    print("Server:", response.decode())

elif choice == "2":

    client.send(b"DOWNLOAD")

    filename = input("File name to download: ")

    client.send(filename.encode())

    data = b''

    while True:
        chunk = client.recv(CHUNK)
        if not chunk:
            break
        data += chunk

    with open("download_" + filename, "wb") as f:
        f.write(data)

    print("File downloaded")

client.close()
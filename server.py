import socket

s = socket.socket()
print('Socket Created...')

s.bind(('localhost',9999))

s.listen(3)
print('Waiting for connection...')

while True:
    c , addr = s.accept()
    name = c.recv(1024).decode()
    print("Conncted with",addr , name)

    c.send(bytes('WELCOME TO DHARMAKSHA INNOVATIVE CREATION LLP','utf-8'))

    c.close()

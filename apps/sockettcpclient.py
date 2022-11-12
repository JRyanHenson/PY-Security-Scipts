import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(("127.0.0.1", 25))
print(mysocket.recv(2048))
mysocket.send("mail from: mark@localhost\n")
print(mysocket.recv(2048))
mysocket.send("rcpt to: recipient@localhost\n")
print(mysocket.recv(2048))
mysocket.send("data\n")
print(mysocket.recv(2048))
mysocket.send("From: Mark Baggett\n")
mysocket.send("Subject: Hello Email\n\n")
mysocket.send("Hello There!\n\n.\n")
print(mysocket.recv(2048))
mysocket.close()
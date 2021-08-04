import socket

host = "4.tcp.ngrok.io"
port = 12850

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
list = (host, port)
client.connect(list)
while True:
		a = str(input("type here:"))
		msg = a.encode("utf-8")
		client.send(msg)

import socket

host = "serve host"
port = 0000#port serve

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
list = (host, port)
client.connect(list)
while True:
		a = str(input("type here:"))
		msg = a.encode("utf-8")
		client.send(msg)

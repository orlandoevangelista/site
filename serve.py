import socket

host = "127.0.0.1"
port = 1500

serve = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
list = (host ,port)
serve.bind(list)
serve.listen(10)
client ,addres = serve.accept()
while True:
	msg = client.recv(2048).decode("ascii")
	print(msg)
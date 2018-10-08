import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 6789
body = "Hello, World! My Python Web Server looks like its working, yay!"

output = f"HTTP/1.1 200 OK\nServer: Cool?\n\
          Content-Type: text/html;charset=UTF-8\nContent-Length: {len(body.encode('utf-8'))}\
          \n\n{body}"

s.bind((host, port))
print(f"Listening on {host}:{port}")
s.listen()
while True:
    c, addr = s.accept()
    data = c.recv(1024)
    print(f'Got connection from {addr}')
    print("Data sent by client: ", data.decode("utf-8"))
    c.sendall(output.encode("utf-8"))
    c.close()

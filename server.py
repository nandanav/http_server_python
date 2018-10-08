import socket
import re

with open("server.conf") as f:
    for line in f:
        if re.match(r"^Listen ", line):
            ipAddr = re.findall(r"\d+.\d+.\d+.\d", line)[0]
            port = int(re.findall(r":\d+", line)[0][1:])
        elif re.match(r"^ServerLocation ", line):
            serverLocation = "".join(re.findall(r"[^ServerLocation ](?=)\w+", line))
        elif re.match(r"^WebsiteFiles ", line):
            websiteFiles = "".join(re.findall(r"[^WebsiteFiles ](?=)\w+", line))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
body = "Hello, World! My Python Web Server looks like its working, yay!"

output = f"HTTP/1.1 200 OK\nServer: Cool?\n\
          Content-Type: text/html;charset=UTF-8\n\
          Content-Length: {len(body.encode('utf-8'))}\
          \n\n{body}"

s.bind((ipAddr, port))

print(f"Listening on {ipAddr}:{port}")
s.listen()
while True:
    c, addr = s.accept()
    data = c.recv(1024)
    print(f'Got connection from {addr}')
    print("Data sent by client: ", data.decode("utf-8"))
    c.sendall(output.encode("utf-8"))
    c.close()

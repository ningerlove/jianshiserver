# -*- coding:utf-8 -*-
import socket

# fetch local ip address
localhost = socket.gethostbyname(socket.gethostname())
print(localhost)

from server import app as application

if __name__ == "__main__":
    application.run(host=localhost,port=7731, debug=True)

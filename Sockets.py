import socket

class SocketServer:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []

    def SocketStart(self, host='127.0.0.1', port=1234, clientMax=5):
        self.socket.bind((host, port))
        self.socket.listen(clientMax)

    def SocketRun(self, func):
        def wrap(*args, **kwargs):
            while True:
                clientsocket, address = self.socket.accept()
                self.clients.append(clientsocket)
                result = func(*args, **kwargs)
            return result
        return wrap



    def SendMsg(self, msg):
        for client in self.clients:
            client.send(bytes(msg, "utf-8"))

class SocketClient:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def Connect(self, host='127.0.0.1', port=1234):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))

    def GetData(self, maxData=1024):
        msg = self.socket.recv(maxData)
        return msg.decode("utf-8")

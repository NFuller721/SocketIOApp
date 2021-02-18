from Sockets import SocketClient

Client = SocketClient()
Client.Connect(port=1000)
while True:
    data = Client.GetData()
    if len(data) > 0:
        print(data)
    else:
        pass

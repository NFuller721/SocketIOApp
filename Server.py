from Sockets import SocketServer
from time import sleep
Server = SocketServer()
Server.SocketStart(port=1000)

@Server.SocketRun
def init():
    Server.SendMsg("Hello There")
    return None

if __name__ == '__main__':
    init()

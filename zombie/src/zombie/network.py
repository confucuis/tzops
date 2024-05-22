from twisted.internet import protocol


class ZombieServer(protocol.Protocol):
    def dataReceived(self, data):
        # 收到客户端发送的数据后，将其打印出来并发送回去
        print("Received:", data)
        self.transport.write(data)


class ZombieFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return ZombieServer()

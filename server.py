from twisted.protocols import basic
from twisted.internet import protocol, reactor

class HTTPEchoProtocol(basic.LineReceiver):
    def __init__(self):
        self.lines = []

    def lineReceived(self, line):
        self.lines.append(line)
        if not line:
            self.sendResponse()

    def sendResponse(self):
        self.sendLine(b'HTTP/1.1 200 OK')
        self.sendLine(b'')

        decoded_lines = ''
        for line in self.lines:
            decoded_lines += line.decode('utf-8')

        responseBody = "You said:\r\n\r\n" + "".join(decoded_lines)
        responseBody = responseBody.encode('utf-8')
        self.transport.write(responseBody)
        self.transport.loseConnection()

class HTTPEchoFactory(protocol.ServerFactory):
    def buildProtocol(self, addr):
        return HTTPEchoProtocol()

def print_server():
    print("You imported me.")
    return

from twisted.application import service, internet

import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import server

# default port in case of the env var was not properly set
ECHO_SERVER_PORT = 8000

proxy_port = int(os.environ.get('ECHO_SERVER_PORT', ECHO_SERVER_PORT))

application = service.Application('TwistedDockerized')
factory = server.HTTPEchoFactory()
server = internet.TCPServer(proxy_port, factory)
server.setServiceParent(application)

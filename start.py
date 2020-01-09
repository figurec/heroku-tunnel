from twisted.web import proxy, http
from twisted.internet import reactor
from twisted.python import log
import sys
import os

log.startLogging(sys.stdout)


class ProxyFactory(http.HTTPFactory):
    protocol = proxy.Proxy


port = 8080
if os.environ.get('PORT'):
    port = os.environ.get('PORT')

reactor.listenTCP(port, ProxyFactory())
reactor.run()

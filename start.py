from twisted.web import proxy, http
from twisted.internet import reactor
from twisted.python import log
import sys
import os

log.startLogging(sys.stdout)
 
class ProxyFactory(http.HTTPFactory):
    protocol = proxy.Proxy
port=5000
if os.environ['PORT']:
 port=os.environ['PORT']
reactor.listenTCP(port, ProxyFactory())
reactor.run()

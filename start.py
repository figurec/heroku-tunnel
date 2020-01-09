from twisted.web import proxy, http
from twisted.internet import reactor
from twisted.python import log
import sys
import os

log.startLogging(sys.stdout)
 
class ProxyFactory(http.HTTPFactory):
    protocol = proxy.Proxy
port=8080
envs=os.environ
if envs['PORT']:
 port=envs['PORT']
reactor.listenTCP(port, ProxyFactory())
reactor.run()

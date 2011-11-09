from twisted.internet import reactor,error

from twistedsnmp import agent,agentprotocol,bsdoidstore


PORT = 20161

def TestAgent():
    oids = { '.1.1.1': 'BAZ'}
    b = bsdoidstore.BSDOIDStore("test.dat", oids)
    return agentprotocol.AgentProtocol(
            snmpVersion='v1',
            agent = agent.Agent(dataStore=b))
    
try:
    reactor.listenUDP(PORT,TestAgent())
    reactor.run()
except error.CannotListenError:
    print "cannot open socket on port %u" % PORT
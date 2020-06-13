import websocket
from threading import Thread
from Queue import Queue 

def startWebSocket(server_address):
	connected= False
	while (connected == False):
		ws = websocket.WebSocket()
		try: 
			ws.connect('ws://'+server_address+':8086')
			print "Connected to web socket server"
			connected= True
			return ws
		except:
			continue
	return ws

def receiveWS(ws, q):
	cont = True
	try:
		while cont:
			message = ws.recv()
			print message
			q.put(message)
	except Exception as e:
		print(e)
		print "Lost websocket connection!"
		cont = False
        
def startSocketQueue(ws):
	socketQ = Queue()
	recvSocket = Thread(target=receiveWS, args=(ws, socketQ,))
	recvSocket.setDaemon(True)
	recvSocket.start()
	return socketQ
	
def getSocket(server_address):
	ws = startWebSocket(server_address)
	return startSocketQueue(ws)

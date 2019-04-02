from PyQt5.QtCore import *
from PyQt5.QtWebChannel import *



#se récupère dans un autre fichier avec sockets_vvnx.add(99,586)
def add(a, b):
    return a + b

@pyqtSlot()    
def reagir_au_signal():
	print("signal arrive")
    
#La macro Q_OBJECT dans les déclarations de classes -> obligatoire si signal ou slot
#https://doc.qt.io/qtforpython/overviews/metaobjects.html

#
#En c++: WebSocketClientWrapper::WebSocketClientWrapper(QWebSocketServer *server, QObject *parent) : QObject(parent) , m_server(server) {
#Q_OBJECT dans la première partie de la déclaration (partie private) ce serait une macro. Meta Object Compiler.
#": QObject(parent) , m_server(server)" ===> initializer list


#https://www.python-course.eu/python3_inheritance.php
    
#webchannel/shared/websockettransport.*
class WebSocketTransport(QWebChannelAbstractTransport):
	
	def textMessageReceivedVvnx(message):
		print(message)
		
	def sendMessage(message):
		self.m_socket.sendTextMessage(message)
	
	def __init__(self, socket):
		print('debug creation WSTransport')
		self.parent = socket
		self.m_socket = socket		
		self.m_socket.textMessageReceived.connect(self.textMessageReceivedVvnx)
		self.m_socket.disconnected.connect(self.deleteLater)
		
	def __del__(self):
		self.m_socket.deleteLater()
	    

#webchannel/shared/websocketclientwrapper.*
class WebSocketClientWrapper(QObject):		
	
	def __init__(self, server):
		print('debug creation WSClientWrapper')
		self.m_server = server
		#self.parent = parent #dérive de QObject qui a un membre parent donc ça devrait passer? sur un malentendu?
		#émettre le signal clientConnected -> signaux en python?, et il faut un websockettransport
		#https://www.riverbankcomputing.com/static/Docs/PyQt5/signals_slots.html
		
		#il le crée automatiquement. je suppose que m_server est vide?
		self.handleNewConnection = pyqtSignal(WebSocketTransport(self.m_server.nextPendingConnection), name = 'clientConnected')	
		self.m_server.newConnection.connect(self.handleNewConnection)
		
		
		
		
	


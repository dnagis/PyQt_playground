#!/usr/bin/python3

#But: openshot (Qt via Python3) pour afficher la timeline (timeline_webview.py) fait communiquer une page html/js avec son code.
#Pour ça, actuellement ils utilisent le module qt webkit  mais j'arrive pas à compiler ce module qui est très ancien
#j'essaie donc de travailler sur webengine qui est le successeur de webkit
#Pour l'instant j'essaie de comprendre, donc je porte en Python3 l'exemple webchannel/standalone fourni avec Qt
#voir morphotox/medley à openshot pour le début du log

#Api Reference des éléments: si tu veux QPushButton par exemple: google "QPushButton class ref"

#Rappel: pour lancer --> QTWEBENGINE_DISABLE_SANDBOX=1 ./webchan_vvnx.py

#Pour les imports, pour savoir quoi importer: python3 -m pip install PyQt5 te donne la path d'install python (/usr/lib64/python3.6/site-packages/PyQt5)
#, si tu cherches un object foobar: google "qtfoobar class api ref" -> te donne en haut le module à ajouter à qmake (exple. QT += foobar),
# tu trouves le nom de la librairie dans le dir d'install -> from PyQt5/Qtfoobar import *

import sys

from PyQt5.QtCore import *
from PyQt5.QtNetwork import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWebSockets import *
from PyQt5.QtWidgets import *


#mon fichier de definitions à part, pour ne pas trop bloater ici
import sockets_vvnx



print("début")

my_app = QApplication(sys.argv)
my_web = QWebEngineView()

#je pense pas que qwebchannel.js soit utilisé ici, dans standalone c'est juste pour checker qu'il soit là. C'est le côté html qui va s'en servir surtout
jsFileInfo = QFileInfo(QDir.currentPath() + "/qwebchannel.js");

server = QWebSocketServer("Mon Server", QWebSocketServer.NonSecureMode);
if not server.listen(QHostAddress.Any, 1234):
	print("erreur")
	
#voir ce socket qui listen: netstat -l
#Active Internet connections (only servers)
#Proto Recv-Q Send-Q Local Address           Foreign Address         State 
#tcp        0      0 :::1234                 :::*                    LISTEN      
      
#server.newConnection.connect(sockets_vvnx.reagir_au_signal)
#socat - TCP:127.0.0.1:12345 --> que dalle... normal, un websocket c'est 
#apparament pas un socket classique. Donc soit tu utilises l'html dans Qt: examples/websockets/echoserver/echoclient.html
#soit tu essaies l'utilitaire en ligne de commande "websocat"

clientWrapper = sockets_vvnx.WebSocketClientWrapper(server)

channel = QWebChannel()

clientWrapper.clientConnected.connect(channel.connectTo)


#QWebEngineView class api ref dit bien "Setting this property clears the view and loads the URL."
my_web.setUrl(QUrl.fromLocalFile("/initrd/mnt/dev_save/packages/PyQt_Playground/index.html")) 
my_web.show()



# sys exit function
sys.exit(my_app.exec_())

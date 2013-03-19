#!/usr/bin/python
from socket import socket, gethostname, AF_INET, SOCK_STREAM
from threading import Thread
import xmlrpclib
import sys

class ListenThread(Thread):
	def __init__(self, target, *args):
		self._target = target
		self._args = args
		Thread.__init__(self)

	def run(self):
		self._target(*self._args)

def convProgress(socket):
	socket.listen(0)
	conn, addr = socket.accept()
	while 1:
		data = conn.recv(4096)
		if not data: break
		print data,
	print "Progress thread exiting!!"
	socket.close()

def createSocket():
	s = socket(AF_INET, SOCK_STREAM)
	s.bind(('',0))
	return (s, s.getsockname()[1])


def main():
	server = xmlrpclib.ServerProxy("http://localhost:8080")
	listenSocket, listenPort = createSocket()

	progressListener = ListenThread(convProgress, listenSocket)
	progressListener.start()
	addr = (gethostname(), listenPort)
	print server.convert(sys.argv[1], sys.argv[2], addr)
	progressListener.join()



if __name__ == '__main__':
	if len(sys.argv) != 3:
		print "Fail! Give me infile and outfile!"
		exit()
	main()

#!/usr/bin/python
from subprocess import call, STDOUT
from socket import create_connection
from SimpleXMLRPCServer import SimpleXMLRPCServer
#from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

def conversion(infile, outfile, addr):
	sock = create_connection(addr)
	cmdline = ["avconv", "-i", infile, "-codec", "copy", outfile]
	ret = call(cmdline, stderr=STDOUT, stdout=sock)
	if ret:
		return "Failure!"
	else:
		return "Success!"

def main():
	server = SimpleXMLRPCServer(("localhost", 8080))
	server.register_introspection_functions()
	server.register_function(conversion, 'convert')
	server.serve_forever()

	


if __name__ == '__main__':
	main()